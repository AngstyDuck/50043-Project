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
          <v-img :src="book.imUrl" aspec-ratio="1.2" min-height="130px"></v-img>
        </v-col>
        <v-col cols="12" md="8">
          <div class="title">{{book.asin}}</div>
          <v-divider></v-divider>
          <div v-for="(category, index) in book.categories" :key="index">
            <div
              class="category"
              v-for="(innerCat, index2) in category"
              :key="index2"
            >{{innerCat}} {{index2 < category.length-1 ? " ➤ " : ""}}</div>
          </div>
        </v-col>
        <v-col>
          <div class="comments">
            <v-container class="comment" v-for="(review, index) in reviews" :key="index">
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
                  <v-btn
                    depressed
                    rounded
                    right
                    :disabled="review.helpfulDisable"
                    v-on:click="helpfulButton(index)"
                  >Helpful</v-btn>
                </v-col>
              </v-row>
            </v-container>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<style scoped>
.category {
  display: inline-block;
}
.comments {
  height: 50%;
  overflow-y: auto;
}

.comment {
  background-color: brown;
}
</style>

<script>
import StarRating from "vue-star-rating";
export default {
  components: {
    StarRating
  },
  data: () => ({
    book: {
      asin: "B002HWRR78",
      price: 0.99,
      imUrl:
        "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
      related: {
        also_bought: [
          "B0070YQGSO",
          "B005O54264",
          "B008SIT1P6",
          "B00ATFFVMS",
          "B00272NHLS",
          "B003GIRQD2",
          "B00DP7HXXC",
          "B00IPXYZSC",
          "B005JFRQ80",
          "B00IU8I3XU",
          "B00B62F3VM",
          "B0026RIIP4",
          "B002CZQL6I",
          "B00D8HIQRG",
          "B00BE7XCUS",
          "B0046A9SIK",
          "B00B7WPAMI",
          "B009D6P0MK",
          "B00DJDZMXK",
          "B0053YQAKW",
          "B00ET69DE0",
          "B00BB2DUI0",
          "B003T9V9A4",
          "B00H59NEAW",
          "B00B4ZPIUC",
          "B00IKXWCGO",
          "B002CQU5LY",
          "B00BZHBO02",
          "B00IPWTP60",
          "B008CVWOBM",
          "B005FY66EA",
          "B002CQU5J6",
          "B00AW5BYOY",
          "B00IMROX88",
          "B0083Q18B8",
          "B00F8F7PU0",
          "B00B5L0S14",
          "B009VLZB6C",
          "B00BKFX6ZA",
          "B00635I88C",
          "B006WQ8J2W",
          "B00BNMX7AY",
          "B00AIWQ400",
          "B0080827BY",
          "B003V8BSA4",
          "B00BDOKY44",
          "B00B3MKN1A",
          "B007HEGXSK",
          "B00AJVBAMM",
          "B007T9WU9Y",
          "B00BWX099Q",
          "B00BXPNTU4",
          "B002JM2C4E",
          "B00G9GOOF6",
          "B000FCKGLG",
          "B004YTPAP8",
          "B006X3889S",
          "B003PDN61O",
          "B003DTMU3A",
          "B00B1WRQYE",
          "B00BSFCO8C",
          "B003O2SHDS",
          "B00B7RAKDC",
          "B004XD99XE",
          "B006WQFDRG",
          "B00DJUA972",
          "B000FBFMZC",
          "B00BYJJNZ4",
          "B0072V4BE6",
          "B00AWFKQVG",
          "B003HKRBYI",
          "B00B7A188K",
          "B00ALKPW4S",
          "B00B40DYMQ",
          "B004Z4IYK0",
          "B009HX6M30",
          "B002FSTJBQ",
          "B003U2TEJI",
          "B003J359J2",
          "B007ZDMP76",
          "B002Y5VSUU",
          "B003EV6Q5U",
          "B008XL1BQU",
          "B008Y1CNDE",
          "B00AA19M3A",
          "B004L62D40",
          "B007R6BN1K",
          "B003DXAB64",
          "B009AE7BI6",
          "B004JHYTZ2"
        ],
        buy_after_viewing: [
          "B00ATFFVMS",
          "B003GIRQD2",
          "B0026RIIP4",
          "B0070YQGSO"
        ]
      },
      categories: [
        ["Books", "Christian Books & Bibles"],
        ["Books", "Literature & Fiction", "Classics"],
        [
          "Kindle Store",
          "Kindle Short Reads",
          "One hour (33-43 pages)",
          "Religion & Spirituality"
        ],
        [
          "Kindle Store",
          "Kindle eBooks",
          "Religion & Spirituality",
          "Christian Books & Bibles"
        ]
      ]
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
      // const Vue = window.vue;
      this.$set(
        this.reviews[index].helpful,
        0,
        this.reviews[index].helpful[0] + 1
      );
      this.reviews[index].helpful[1]++;
      this.reviews[index].helpfulDisable = true;
      // Send POST to backend
      // console.log(this.reviews);
    }
  }
};
</script>
