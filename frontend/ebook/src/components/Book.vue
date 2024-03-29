<template>
  <div>
    <v-toolbar dark color="primary">
      <v-btn icon dark @click="closeBookDialog()">
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </v-toolbar>
    <div class="loading" v-if="fullLoading">
      <v-progress-circular :size="90" :width="7" color="primary" indeterminate></v-progress-circular>
      <div>Loading book...</div>
    </div>
    <v-container class="grey darken-3" v-else>
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
          <div class="book-title" v-if="book.title">{{book.title}}</div>
          <div class="book-title" v-else>{{book.asin}}</div>
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
                  <v-card @click="changeBook(related.asin)" class="mx-auto">
                    <v-img :src="related.imUrl"></v-img>
                    <!-- <v-card-title>{{ asin }}</v-card-title> -->
                  </v-card>
                </v-col>
              </v-row>
            </v-container>
            <v-pagination v-model="page" :length="parseInt(book.related.length/4) +1"></v-pagination>
          </div>
        </v-col>
        <v-col>
          <v-container>
            <v-row v-if="book.description">
              <v-col cols="12">
                <div class="subtitle">Description</div>
              </v-col>
              <v-col cols="12">
                <div>{{book.description}}</div>
              </v-col>
            </v-row>
            <v-row no-gutters>
              <v-col cols="12">
                <div class="subtitle">Reviews</div>
              </v-col>
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
          <div class="loading" v-if="loadingReviewList">
            <div>Loading reviews...</div>
            <v-progress-linear :height="20" striped color="primary" indeterminate></v-progress-linear>
          </div>
          <div class="comments" v-else>
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
                              v-on:click="helpfulButton(review)"
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
            <v-btn color="blue darken-1" @click="postNewReview()">Post Review</v-btn>
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
.loading {
  background-color: rgb(73, 73, 73);
}

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
.loading {
  left: 40%;
  text-align: center;
  padding-top: 20px;
  font-size: 2rem;
}
</style>

<script>
import StarRating from "vue-star-rating";
import EventBus from "../EventBus";

export default {
  components: {
    StarRating
  },
  computed: {
    pagedRelatedBooks() {
      if (this.book.related) {
        return this.book.related.slice(
          (this.page - 1) * 4 > this.book.related.length
            ? this.book.related.length
            : (this.page - 1) * 4,
          this.page * 4
        );
      } else {
        return [];
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
    loadingReviewList: true,
    fullLoading: false,
    reviewPost: {
      overall: 0.0,
      summary: "",
      reviewText: "",
      reviewerName: ""
    },
    reviews: []
  }),
  mounted() {
    EventBus.$on("FULL_LOADING_TRUE", payload => {
      console.log("loading");
      this.fullLoading = true;
    });
    EventBus.$on("FULL_LOADING_FALSE", payload => {
      console.log("not loading");
      this.fullLoading = false;
    });
    EventBus.$on("LOAD_REVIEWS", book => {
      this.loadingReviewList = true;
      this.reviews = [];
      this.getReviewList(book.asin);
    });
  },
  methods: {
    closeBookDialog() {
      EventBus.$emit("CLOSE_BOOK_DIALOG", "");
    },
    changeBook(asin) {
      EventBus.$emit("CHANGE_BOOK", asin);
    },
    helpfulButton(review) {
      this.$set(review.helpful, 0, review.helpful[0] + 1);
      review.helpful[1]++;
      review.helpfulDisable = true;
      const payload = {
        asin: review.asin,
        reviewerName: review.reviewerName,
        reviewerID: review.reviewerID
      };
      this.$store.dispatch("store/helpful_review", payload).then(response => {
        if (response != 0) {
        } else {
          console.log("Error marking review as helpful");
        }
      });
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
    },
    postNewReview() {
      var payload = this.reviewPost;
      payload.asin = this.book.asin;
      console.log(payload);
      this.$store.dispatch("store/post_new_review", payload).then(response => {
        if (response != 0) {
          this.loadingReviewList = true;
          this.cancelReview();
          this.getReviewList(this.book.asin);
        } else {
          console.log("Error posting review");
        }
      });
    },
    getReviewList(asin) {
      this.$store
        .dispatch("store/review_list", { asin: asin })
        .then(response => {
          if (response != 0) {
            this.reviews = response.reviews;
            this.loadingReviewList = false;
          } else {
            console.log("Error retrieving review_list");
          }
        });
    }
  }
};
</script>
