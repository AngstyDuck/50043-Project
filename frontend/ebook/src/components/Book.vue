<template>
  <div>
    <v-toolbar dark color="primary">
      <v-btn icon dark @click="dialog = false">
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </v-toolbar>
    <v-container class="grey darken-3">
      <v-row>
        <v-col cols="12" md="4">
          <v-img :src="book.imUrl" min-height="130px"></v-img>
          <div class="pricing">
            <div v-if="book.price">
              Price:
              <b>${{book.price}}</b>
            </div>
            <div v-else>Price is not in database</div>
          </div>
        </v-col>
        <v-col cols="12" md="8">
          <div class="book-title">{{book.asin}}</div>
          <v-divider></v-divider>
          <div class="subtitle">Categories</div>
          <div v-for="(category, index) in book.categories" :key="index">
            <div
              class="category"
              v-for="(innerCat, index2) in category"
              :key="index2"
            >{{innerCat}} {{index2 < category.length-1 ? " ➤ " : ""}}</div>
          </div>
          <div v-if="book.related">
            <v-container>
              <v-row class="subtitle">Related books</v-row>
              <v-row>
                <v-col cols="12" md="3" v-for="(related, index) in pagedRelatedBooks" :key="index">
                  <v-img :src="related.imUrl"></v-img>
                </v-col>
              </v-row>
            </v-container>
            <v-pagination v-model="page" :length="parseInt(book.related.also_bought.length/4) +1"></v-pagination>
          </div>
        </v-col>
        <v-col>
          <div class="subtitle">Reviews</div>
          <v-container>
            <v-row>
              <v-col cols="12" md="10">
                <div class="average-title">
                  Average rating:
                  <star-rating
                    :inline="true"
                    :increment="0.1"
                    :star-size="25"
                    read-only
                    :rating="book.averageRating"
                  ></star-rating>
                </div>
              </v-col>
              <v-col cols="12" md="2">
                <v-btn color="blue darken-1" @click="postReviewDialog()">
                  <v-icon left>create</v-icon>Post a review
                </v-btn>
              </v-col>
            </v-row>
          </v-container>
          <v-divider></v-divider>
          <div class="comments">
            <v-container>
              <v-row dense v-for="(review, index) in reviews" :key="index">
                <v-col cols="12">
                  <v-card color="#385F73" class="comment">
                    <v-container>
                      <v-row no-gutters>
                        <v-col>
                          <v-icon>person</v-icon>
                          {{review.reviewerName}}
                        </v-col>
                      </v-row>
                      <v-row no-gutters>{{review.reviewTime}}</v-row>
                      <v-row no-gutters>
                        <star-rating :star-size="20" read-only :rating="review.overall"></star-rating>
                      </v-row>
                      <v-row no-gutters>
                        <b>{{review.summary}}</b>
                      </v-row>
                      <v-row no-gutters>{{review.reviewText}}</v-row>
                      <v-spacer />
                      <v-row>
                        <v-divider></v-divider>
                      </v-row>
                      <v-row no-gutters>
                        <v-col cols="12" md="2">
                          <div
                            v-if="review.helpful[0] > 0"
                          >{{review.helpful[0]}} {{review.helpful[0]==1 ? "person" : "people"}} found this helpful</div>
                        </v-col>
                        <v-col cols="12" md="2">
                          <v-card-actions>
                            <v-btn
                              depressed
                              right
                              :disabled="review.helpfulDisable"
                              large
                              rounded
                              v-on:click="helpfulButton(index)"
                            >{{review.helpfulDisable?"Thank you":"Helpful"}}</v-btn>
                          </v-card-actions>
                        </v-col>
                      </v-row>
                    </v-container>
                  </v-card>
                </v-col>
              </v-row>
            </v-container>
          </div>
        </v-col>
      </v-row>
    </v-container>
    <v-container>
      <v-row>
        <v-col cols="12" md="3" />
        <v-col cols="12" md="6">
          <v-btn block x-large color="blue darken-1" @click="postReviewDialog()">
            <v-icon left>create</v-icon>Post a review
          </v-btn>
        </v-col>
        <v-col cols="12" md="3" />
      </v-row>
    </v-container>
    <div>
      <v-dialog v-model="reviewDialog" persistent max-width="600px">
        <v-card>
          <v-card-title>
            <span class="headline">Post a review</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row no-gutters>
                <v-col cols="12">Overall rating</v-col>
              </v-row>
              <v-row>
                <v-col cols="12">
                  <star-rating :star-size="40" v-model="reviewPost.overall"></star-rating>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    label="Add a headline"
                    required
                    hint="What's the most important to know?"
                    persistent-hint
                    v-model="reviewPost.summary"
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-textarea
                    name="input-7-1"
                    label="Write your review"
                    hint="What did you like or dislike? Was the book what you expected?"
                    persistent-hint
                    v-model="reviewPost.reviewText"
                  ></v-textarea>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-text-field
                    label="Username"
                    required
                    hint="What do you want to be known as?"
                    persistent-hint
                    v-model="reviewPost.reviewerName"
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="closeDialog = true">Cancel</v-btn>
            <v-btn color="blue darken-1" @click="dialog = false">Post Review</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-dialog v-model="closeDialog" max-width="290">
        <v-card>
          <v-card-title class="headline">Cancel review post?</v-card-title>

          <v-card-text>Any typed data will be erased. Do you wish to cancel the post?</v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="cancelReview()">Yes</v-btn>
            <v-btn color="blue darken-1" @click="closeDialog = false">No</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </div>
</template>

<style scoped>
.category {
  display: inline-block;
}

.book-title {
  font-size: 2.4rem;
  font-weight: 500;
}

.subtitle {
  font-size: 2.2rem;
  font-weight: 450;
}

.average-title {
  font-size: 1.8rem;
}

.comments {
  /* height: 50%;
  overflow-y: auto; */
}

.comment {
  background-color: brown;
}

.pricing {
  font-size: 1.7rem;
  text-align: center;
}
</style>

<script>
import StarRating from "vue-star-rating";
export default {
  components: {
    StarRating
  },
  computed: {
    pagedRelatedBooks() {
      if (this.book.related) {
        return this.book.related.also_bought.slice(
          (this.page - 1) * 4 > this.book.related.also_bought.length
            ? this.book.related.also_bought.length
            : (this.page - 1) * 4,
          this.page * 4
        );
      }
      else {
        return []
      }
    }
  },
  props: {
    book: Object
  },
  data: () => ({
    page: 1,
    reviewDialog: false,
    closeDialog: false,
    reviewPost: {
      overall: 0.0,
      summary: "",
      reviewText: "",
      reviewerName: ""
    },
    reviews: [
      {
        reviewerID: "A1F6404F1VG29J",
        asin: "B000F83SZQ",
        reviewerName: "Avidreader",
        helpful: [0, 0],
        reviewText:
          "I enjoy vintage books and movies so I enjoyed reading this book.  The plot was unusual.  Don't think killing someone in self-defense but leaving the scene and the body without notifying the police or hitting someone in the jaw to knock them out would wash today.Still it was a good read for me.",
        overall: 5.0,
        summary: "Nice vintage story",
        unixReviewTime: 1399248000,
        reviewTime: "05 5, 2014",
        helpfulDisable: false
      },
      {
        reviewerID: "AN0N05A9LIJEQ",
        asin: "B000F83SZQ",
        reviewerName: "critters",
        helpful: [2, 2],
        reviewText:
          "This book is a reissue of an old one; the author was born in 1910. It's of the era of, say, Nero Wolfe. The introduction was quite interesting, explaining who the author was and why he's been forgotten; I'd never heard of him.The language is a little dated at times, like calling a gun a &#34;heater.&#34;  I also made good use of my Fire's dictionary to look up words like &#34;deshabille&#34; and &#34;Canarsie.&#34; Still, it was well worth a look-see.",
        overall: 4.0,
        summary: "Different...",
        unixReviewTime: 1388966400,
        reviewTime: "01 6, 2014",
        helpfulDisable: false
      },
      {
        reviewerID: "A795DMNCJILA6",
        asin: "B000F83SZQ",
        reviewerName: "dot",
        helpful: [2, 2],
        reviewText:
          "This was a fairly interesting read.  It had old- style terminology.I was glad to get  to read a story that doesn't have coarse, crasslanguage.  I read for fun and relaxation......I like the free ebooksbecause I can check out a writer and decide if they are intriguing,innovative, and have enough of the command of Englishthat they can convey the story without crude language.",
        overall: 4.0,
        summary: "Oldie",
        unixReviewTime: 1396569600,
        reviewTime: "04 4, 2014",
        helpfulDisable: false
      },
      {
        reviewerID: "A1FV0SX13TWVXQ",
        asin: "B000F83SZQ",
        reviewerName: 'Elaine H. Turley "Montana Songbird"',
        helpful: [1, 1],
        reviewText:
          "I'd never read any of the Amy Brewster mysteries until this one..  So I am really hooked on them now.",
        overall: 5.0,
        summary: "I really liked it.",
        unixReviewTime: 1392768000,
        reviewTime: "02 19, 2014",
        helpfulDisable: false
      },
      {
        reviewerID: "A3SPTOKDG7WBLN",
        asin: "B000F83SZQ",
        reviewerName: "Father Dowling Fan",
        helpful: [0, 1],
        reviewText:
          "If you like period pieces - clothing, lingo, you will enjoy this mystery.  Author had me guessing at least 2/3 of the way through.",
        overall: 4.0,
        summary: "Period Mystery",
        unixReviewTime: 1395187200,
        reviewTime: "03 19, 2014",
        helpfulDisable: false
      },
      {
        reviewerID: "A1RK2OCZDSGC6R",
        asin: "B000F83SZQ",
        reviewerName: "ubavka seirovska",
        helpful: [0, 0],
        reviewText:
          "A beautiful in-depth character description makes it like a fast pacing movie. It is a pity Mr Merwin did not write 30 instead only 3 of the Amy Brewster mysteries.",
        overall: 4.0,
        summary: "Review",
        unixReviewTime: 1401062400,
        reviewTime: "05 26, 2014",
        helpfulDisable: false
      },
      {
        reviewerID: "A2HSAKHC3IBRE6",
        asin: "B000F83SZQ",
        reviewerName: "Wolfmist",
        helpful: [0, 0],
        reviewText:
          "I enjoyed this one tho I'm not sure why it's called An Amy Brewster Mystery as she's not in it very much. It was clean, well written and the characters well drawn.",
        overall: 4.0,
        summary: "Nice old fashioned story",
        unixReviewTime: 1402358400,
        reviewTime: "06 10, 2014",
        helpfulDisable: false
      },
      {
        reviewerID: "A3DE6XGZ2EPADS",
        asin: "B000F83SZQ",
        reviewerName: "WPY",
        helpful: [1, 1],
        reviewText:
          "Never heard of Amy Brewster. But I don't need to like Amy Brewster to like this book. Actually, Amy Brewster is a side kick in this story, who added mystery to the story not the one resolved it. The story brings back the old times, simple life, simple people and straight relationships.",
        overall: 4.0,
        summary: "Enjoyable reading and reminding the old times",
        unixReviewTime: 1395446400,
        reviewTime: "03 22, 2014",
        helpfulDisable: false
      }
    ]
  }),
  methods: {
    helpfulButton(index) {
      this.$set(
        this.reviews[index].helpful,
        0,
        this.reviews[index].helpful[0] + 1
      );
      this.reviews[index].helpful[1]++;
      this.reviews[index].helpfulDisable = true;
    },
    postReviewDialog() {
      this.reviewDialog = true;
    },
    cancelReview() {
      this.reviewDialog = false;
      this.closeDialog = false;
      this.reviewPost.overall = 0.0;
      this.reviewPost.summary = "";
      this.reviewPost.reviewText = "";
      this.reviewPost.reviewerName = "";
    }
  }
};
</script>
