<template>
  <div>
    <v-dialog v-model="dialog" min-height="900" width="1700">
      <Book/>
    </v-dialog>
    <v-container>
      <v-row>
        <v-col v-for="book in books" v-bind:key="book.asin" cols="12" xs="6" sm="4" md="3" lg="2">
          <v-hover v-slot:default="{ hover }">
            <v-card
              :elevation="hover ? 12 : 2"
              @click="this.console.log('hi')"
              class="mx-auto"
              max-width="344"
            >
              <v-img :src="book.imUrl" aspec-ratio="1.2" min-height="130px"></v-img>
              <!-- <v-card-title>{{ asin }}</v-card-title> -->
            </v-card>
          </v-hover>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<style scoped>
.book {
  padding: 0 10px;
}
</style>

<script>
import Book from"../components/Book.vue"

export default {
  components: {
    Book
  },
  data: () => ({
    dialog: false,
    books: [
      {
        asin: "B000FA5NSO",
        imUrl:
          "http://ecx.images-amazon.com/images/I/51N45B6jq8L._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
        related: { also_viewed: ["B000FBF81K", "B000FA5KKA"] },
        categories: [
          ["Books", "Literature & Fiction"],
          ["Books", "Science Fiction & Fantasy", "Science Fiction"],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Science Fiction & Fantasy",
            "Science Fiction"
          ]
        ]
      },
      {
        asin: "B000FA5UXC",
        imUrl:
          "http://ecx.images-amazon.com/images/I/51q4iur5ukL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
        related: {
          also_bought: [
            "B004SPL1I8",
            "B00942QL3K",
            "B000FA5Q8Q",
            "B003E4CYVW",
            "B003P9XMEE"
          ]
        },
        categories: [
          ["Books", "Literature & Fiction"],
          [
            "Books",
            "Science Fiction & Fantasy",
            "Science Fiction",
            "High Tech"
          ],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Science Fiction & Fantasy",
            "Science Fiction",
            "Hard Science Fiction"
          ]
        ],
        description:
          "Madoc Tamlin is a man with an unusual problem. He wakes to find himself a thousand years in the future, in a space station on the far side of the sun. Or so he is told by the mysterious, sexless human who greets him. Madoc assures himself that he's still in his own time, trapped in advanced virtual reality by one of his foes, because if he isn't, he has no idea why he was cryogenically frozen--which would mean that he was a dangerous criminal. And he doesn't remember that either! Plus, the notorious serial killer Christine Caine has been defrosted to join him, and they, along with their strange rescuer, have just been captured in an impossible space battle by an unknown enemy.The Omega Expeditionis the sixth and concluding volume of Brian Stableford's grand future history, which explores the possibilities and perils of emortality  (near-immortality). This is one of the most thoughtful, complex, and ambitious series ever produced in science fiction, and its final novel, a standalone work, masterfully orchestrates the numerous characters, themes, plot lines, and ideas to a bold conclusion. But newcomers to the series really shouldn't start withThe Omega Expedition. Read the novels of this future history in the author's intended order, detailed in his informative introduction toThe Omega Expedition. Start withThe Cassandra Complex.--Cynthia Ward"
      },
      {
        asin: "B000FA5T4W",
        price: 12.46,
        imUrl:
          "http://ecx.images-amazon.com/images/I/51eWyBr8A3L._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
        related: {
          also_bought: [
            "B004RKXHGS",
            "B004ULMJH2",
            "B00BI37JDY",
            "B00FN4NN3Y",
            "B007IUGLYO",
            "B007JCNNGK",
            "B0044KLPOW"
          ],
          buy_after_viewing: [
            "B004RKXHGS",
            "B00BI37JDY",
            "B00710A0V6",
            "B004478AMA"
          ]
        },
        categories: [
          ["Books", "Business & Money", "Accounting"],
          [
            "Books",
            "Business & Money",
            "Personal Finance",
            "Budgeting & Money Management"
          ],
          ["Kindle Store", "Kindle eBooks", "Business & Money", "Accounting"],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Business & Money",
            "Personal Finance",
            "Budgeting & Money Management"
          ],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Professional & Technical",
            "Accounting & Finance",
            "Accounting"
          ]
        ]
      },
      {
        asin: "B000FA5SHK",
        imUrl:
          "http://ecx.images-amazon.com/images/I/51c7mqORjsL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
        categories: [
          ["Books", "Science & Math", "Behavioral Sciences"],
          ["Books", "Self-Help", "Relationships", "Love & Romance"],
          ["Books", "Self-Help", "Sex"],
          [
            "Kindle Store",
            "Kindle eBooks",
            "Health, Fitness & Dieting",
            "Relationships",
            "Love & Romance"
          ],
          ["Kindle Store", "Kindle eBooks", "Health, Fitness & Dieting", "Sex"]
        ]
      }
    ]
  })
};
</script>
