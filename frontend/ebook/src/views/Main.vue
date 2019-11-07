<template>
  <div>
    <v-dialog v-if="selectedBook" v-model="bookDialog" min-height="900" width="1700">
      <Book :book="selectedBook" />
    </v-dialog>
    <div class="loading" v-if="loadingBookList">
      <v-progress-circular :size="90" :width="7" color="primary" indeterminate></v-progress-circular>
      <div>Loading books...</div>
    </div>
    <div v-else>
      <div class="top-row">
        <v-container>
          <v-row>
            <v-col class="section-title">New Releases</v-col>
          </v-row>
          <v-row>
            <v-col
              v-for="book in pagedReleaseBooks"
              v-bind:key="book.asin"
              cols="12"
              xs="6"
              sm="4"
              md="3"
              lg="2"
            >
              <v-hover v-slot:default="{ hover }">
                <v-card
                  :elevation="hover ? 12 : 2"
                  @click="selectBook(book)"
                  class="mx-auto"
                  max-width="344"
                >
                  <v-img :src="book.imUrl" min-height="130px"></v-img>
                  <!-- <v-card-title>{{ asin }}</v-card-title> -->
                </v-card>
              </v-hover>
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col>
              <v-pagination v-model="pageRelease" :length="parseInt(releaseBooks.length/6) +1"></v-pagination>
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col class="section-title">Bestselling Books</v-col>
          </v-row>
          <v-row>
            <v-col
              v-for="book in pagedBestBooks"
              v-bind:key="book.asin"
              cols="12"
              xs="6"
              sm="4"
              md="3"
              lg="2"
            >
              <v-hover v-slot:default="{ hover }">
                <v-card
                  :elevation="hover ? 12 : 2"
                  @click="selectBook(book)"
                  class="mx-auto"
                  max-width="344"
                >
                  <v-img :src="book.imUrl" min-height="130px"></v-img>
                  <!-- <v-card-title>{{ asin }}</v-card-title> -->
                </v-card>
              </v-hover>
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col>
              <v-pagination v-model="pageBest" :length="parseInt(bestBooks.length/6) +1"></v-pagination>
            </v-col>
          </v-row>
        </v-container>
      </div>
      <v-container class="bot-row">
        <v-row>
          <v-col class="section-title">Browse our collection</v-col>
        </v-row>
        <v-row>
          <v-col v-for="book in books" v-bind:key="book.asin" cols="12" xs="6" sm="4" md="3" lg="2">
            <v-hover v-slot:default="{ hover }">
              <v-card
                :elevation="hover ? 12 : 2"
                @click="selectBook(book)"
                class="mx-auto"
                max-width="344"
              >
                <v-img :src="book.imUrl" min-height="130px"></v-img>
                <!-- <v-card-title>{{ asin }}</v-card-title> -->
              </v-card>
            </v-hover>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<style scoped>
.book {
  padding: 0 10px;
}
.loading {
  position: absolute;
  left: 40%;
  text-align: center;
  padding-top: 20%;
  font-size: 2rem;
}
.top-row {
  background-color: rgb(62,62,62);
  width: 100%;
  padding: 0;
}
.section-title {
  font-size: 2rem;
  font-weight: 400;
}
</style>

<script>
import Book from "../components/Book.vue";
import EventBus from "../EventBus";

export default {
  components: {
    Book
  },
  computed: {
    pagedBestBooks() {
      if (this.bestBooks) {
        return this.bestBooks.slice(
          (this.pageBest - 1) * 6 > this.bestBooks.length
            ? this.bestBooks.length
            : (this.pageBest - 1) * 6,
          this.pageBest * 6
        );
      } else {
        return [];
      }
    },
    pagedReleaseBooks() {
      if (this.releaseBooks) {
        return this.releaseBooks.slice(
          (this.pageRelease - 1) * 6 > this.releaseBooks.length
            ? this.releaseBooks.length
            : (this.pageRelease - 1) * 6,
          this.pageRelease * 6
        );
      } else {
        return [];
      }
    }
  },
  data: () => ({
    pageBest: 1,
    pageRelease: 1,
    bookDialog: false,
    books: [],
    selectedBook: null,
    loadingBookList: true,
    releaseBooks: [
      {
        title:
          "Faux Leather Kindle Sleeve Case for Kindle (Fits 9.7&quot; Display, Latest Generation Kindle DX) - Yellow (Smooth finish)",
        asin: "B002HWRIIQ",
        averageRating: 4.6,
        imUrl:
          "http://ecx.images-amazon.com/images/I/513mtcKv9HL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
        categories: [
          ["Books", "Business & Money", "Job Hunting & Careers", "Guides"],
          ["Books", "Business & Money", "Job Hunting & Careers", "Job Hunting"],
          ["Books", "Business & Money", "Job Hunting & Careers", "Resumes"],
          [
            "Kindle Store",
            "KindlQe eBooks",
            "Business & Money",
            "Job Hunting & Careers",
            "Career Guides"
          ],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Business & Money",
            "Job Hunting & Careers",
            "Job Hunting"
          ],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Business & Money",
            "Job Hunting & Careers",
            "Resumes"
          ]
        ]
      },
      {
        asin: "B002HWRKES",
        price: 0.99,
        averageRating: 3.6,
        imUrl:
          "http://ecx.images-amazon.com/images/I/51KA6TO1xdL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
        related: [
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          }
        ],
        categories: [
          ["Books", "Christian Books & Bibles"],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Religion & Spirituality",
            "Christian Books & Bibles"
          ]
        ]
      },
      {
        asin: "B002HWRKPM",
        averageRating: 2.5,
        description:
          "A 20 year fan of the Montreal Canadiens, transplanted to the west coast, follows both of his teams the Sharks and the Habs.I obviously have too much free time.Kindle blogs are fully downloaded onto your Kindle so you can read them even when you're not wirelessly connected. And unlike RSS readers which often only provide headlines, blogs on Kindle give you full text content and images, and are updated wirelessly throughout the day.",
        categories: [["Kindle Store", "Kindle Blogs", "Sports"]]
      },
      {
        asin: "B002HWRR78",
        price: 0.99,
        averageRating: 4.2,
        imUrl:
          "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
        related: [
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          }
        ],
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
      {
        title:
          "Faux Leather Kindle Sleeve Case for Kindle (Fits 9.7&quot; Display, Latest Generation Kindle DX) - Yellow (Smooth finish)",
        asin: "B002HWRIIQ",
        averageRating: 4.6,
        imUrl:
          "http://ecx.images-amazon.com/images/I/513mtcKv9HL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
        categories: [
          ["Books", "Business & Money", "Job Hunting & Careers", "Guides"],
          ["Books", "Business & Money", "Job Hunting & Careers", "Job Hunting"],
          ["Books", "Business & Money", "Job Hunting & Careers", "Resumes"],
          [
            "Kindle Store",
            "KindlQe eBooks",
            "Business & Money",
            "Job Hunting & Careers",
            "Career Guides"
          ],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Business & Money",
            "Job Hunting & Careers",
            "Job Hunting"
          ],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Business & Money",
            "Job Hunting & Careers",
            "Resumes"
          ]
        ]
      },
      {
        asin: "B002HWRKES",
        price: 0.99,
        averageRating: 3.6,
        imUrl:
          "http://ecx.images-amazon.com/images/I/51KA6TO1xdL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
        related: [
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          }
        ],
        categories: [
          ["Books", "Christian Books & Bibles"],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Religion & Spirituality",
            "Christian Books & Bibles"
          ]
        ]
      },
      {
        asin: "B002HWRKPM",
        averageRating: 2.5,
        description:
          "A 20 year fan of the Montreal Canadiens, transplanted to the west coast, follows both of his teams the Sharks and the Habs.I obviously have too much free time.Kindle blogs are fully downloaded onto your Kindle so you can read them even when you're not wirelessly connected. And unlike RSS readers which often only provide headlines, blogs on Kindle give you full text content and images, and are updated wirelessly throughout the day.",
        categories: [["Kindle Store", "Kindle Blogs", "Sports"]]
      },
      {
        asin: "B002HWRR78",
        price: 0.99,
        averageRating: 4.2,
        imUrl:
          "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
        related: [
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          }
        ],
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
      }
    ],
    bestBooks: [
      {
        title:
          "Faux Leather Kindle Sleeve Case for Kindle (Fits 9.7&quot; Display, Latest Generation Kindle DX) - Yellow (Smooth finish)",
        asin: "B002HWRIIQ",
        averageRating: 4.6,
        imUrl:
          "http://ecx.images-amazon.com/images/I/513mtcKv9HL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
        categories: [
          ["Books", "Business & Money", "Job Hunting & Careers", "Guides"],
          ["Books", "Business & Money", "Job Hunting & Careers", "Job Hunting"],
          ["Books", "Business & Money", "Job Hunting & Careers", "Resumes"],
          [
            "Kindle Store",
            "KindlQe eBooks",
            "Business & Money",
            "Job Hunting & Careers",
            "Career Guides"
          ],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Business & Money",
            "Job Hunting & Careers",
            "Job Hunting"
          ],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Business & Money",
            "Job Hunting & Careers",
            "Resumes"
          ]
        ]
      },
      {
        asin: "B002HWRKES",
        price: 0.99,
        averageRating: 3.6,
        imUrl:
          "http://ecx.images-amazon.com/images/I/51KA6TO1xdL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
        related: [
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          }
        ],
        categories: [
          ["Books", "Christian Books & Bibles"],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Religion & Spirituality",
            "Christian Books & Bibles"
          ]
        ]
      },
      {
        asin: "B002HWRKPM",
        averageRating: 2.5,
        description:
          "A 20 year fan of the Montreal Canadiens, transplanted to the west coast, follows both of his teams the Sharks and the Habs.I obviously have too much free time.Kindle blogs are fully downloaded onto your Kindle so you can read them even when you're not wirelessly connected. And unlike RSS readers which often only provide headlines, blogs on Kindle give you full text content and images, and are updated wirelessly throughout the day.",
        categories: [["Kindle Store", "Kindle Blogs", "Sports"]]
      },
      {
        asin: "B002HWRR78",
        price: 0.99,
        averageRating: 4.2,
        imUrl:
          "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
        related: [
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          }
        ],
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
      {
        title:
          "Faux Leather Kindle Sleeve Case for Kindle (Fits 9.7&quot; Display, Latest Generation Kindle DX) - Yellow (Smooth finish)",
        asin: "B002HWRIIQ",
        averageRating: 4.6,
        imUrl:
          "http://ecx.images-amazon.com/images/I/513mtcKv9HL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
        categories: [
          ["Books", "Business & Money", "Job Hunting & Careers", "Guides"],
          ["Books", "Business & Money", "Job Hunting & Careers", "Job Hunting"],
          ["Books", "Business & Money", "Job Hunting & Careers", "Resumes"],
          [
            "Kindle Store",
            "KindlQe eBooks",
            "Business & Money",
            "Job Hunting & Careers",
            "Career Guides"
          ],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Business & Money",
            "Job Hunting & Careers",
            "Job Hunting"
          ],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Business & Money",
            "Job Hunting & Careers",
            "Resumes"
          ]
        ]
      },
      {
        asin: "B002HWRKES",
        price: 0.99,
        averageRating: 3.6,
        imUrl:
          "http://ecx.images-amazon.com/images/I/51KA6TO1xdL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
        related: [
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          }
        ],
        categories: [
          ["Books", "Christian Books & Bibles"],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Religion & Spirituality",
            "Christian Books & Bibles"
          ]
        ]
      },
      {
        asin: "B002HWRKPM",
        averageRating: 2.5,
        description:
          "A 20 year fan of the Montreal Canadiens, transplanted to the west coast, follows both of his teams the Sharks and the Habs.I obviously have too much free time.Kindle blogs are fully downloaded onto your Kindle so you can read them even when you're not wirelessly connected. And unlike RSS readers which often only provide headlines, blogs on Kindle give you full text content and images, and are updated wirelessly throughout the day.",
        categories: [["Kindle Store", "Kindle Blogs", "Sports"]]
      },
      {
        asin: "B002HWRR78",
        price: 0.99,
        averageRating: 4.2,
        imUrl:
          "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
        related: [
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          },
          {
            asin: "B0070YQGSO",
            imUrl:
              "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
          }
        ],
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
      }
    ]
  }),
  methods: {
    getBooks() {
      this.$store.dispatch("store/book_list", {}).then(response => {
        if (response != 0) {
          this.books = response.books;
          this.loadingBookList = false;
        } else {
          console.log("Error retrieving book_list");
        }
      });
    },
    selectBook(book) {
      this.selectedBook = book;
      EventBus.$emit("SELECT_BOOK", book);
      console.log(this.selectedBook);
      this.bookDialog = true;
    }
  },
  mounted() {
    this.getBooks();

    EventBus.$on("CHANGE_BOOK", payload => {
      this.selectBook(payload);
    });
    EventBus.$on("CLOSE_BOOK_DIALOG", payload => {
      this.bookDialog = false;
    });
  }
};
</script>
