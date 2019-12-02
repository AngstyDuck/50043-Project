<template>
  <div>
    <v-dialog v-if="selectedBook" v-model="bookDialog" min-height="900" width="1700">
      <Book :book="selectedBook" />
    </v-dialog>
    <div class="loading" v-if="loadingBookList">
      <v-progress-circular :size="90" :width="7" color="primary" indeterminate></v-progress-circular>
      <div>Loading books...</div>
    </div>
    <v-container v-else>
      <v-row>
        <v-col v-for="category in categories" v-bind:key="category.category">
          <v-btn @click="filterClick(category.category)" text>{{ category.category }}</v-btn>
        </v-col>
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
      <v-row v-if="collectionLoading">
        <v-col>
          <div class="loading-collection">
            <v-progress-circular :size="90" :width="7" color="primary" indeterminate></v-progress-circular>
            <div>Loading collection...</div>
          </div>
        </v-col>
      </v-row>
    </v-container>
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
</style>

<script>
import Book from "../components/Book.vue";
import EventBus from "../EventBus";

export default {
  watch: {
    '$route' (to,from) {
      this.filtertext = to.params.filtertext;
      this.getBooks();
    }
  },
  components: {
    Book
  },
  data: () => ({
    bookDialog: false,
    books: [],
    selectedBook: null,
    loadingBookList: false,
    filtertext: "",
    categories: [],
    category: "",
    collectionLoading: false,
    fetchLength: 21
  }),
  methods: {
    filterClick(category) {
      this.category = category
      if (this.$router.currentRoute.path != "/filter"+ this.category ) {
        this.$router.push({ path: "/filter/" + this.category });
      } else {
        location.reload();
      }
    },
    getFilterList() {
      this.$store.dispatch("store/categories", {}).then(response => {
        if (response != 0) {
          this.categories = response.categories;
          console.log(response.categories);
        } else {
          console.log("Error retrieving categories");
          console.log(this.categories);
        }
      });
    },
    getBooks(filtertext) {
      this.collectionLoading = true;
      const payload = { filtertext: this.filtertext };
      this.$store.dispatch("store/filter_books", {
          params: {
            start_list: this.books.length,
            end_list: this.books.length + this.fetchLength - 1,
            filtertext: this.filtertext
          }
        }).then(response => {
        if (response != 0) {
          this.books.push.apply(this.books,response.books);
          this.collectionLoading = false;
          console.log(this.books);
        } else {
          console.log("Error retrieving searched books_list");
          console.log(this.filtertext);
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
  created() {
    this.filtertext = this.$route.params.filtertext;
  },
  mounted() {
    this.getBooks();
    this.getFilterList();
    EventBus.$on("CHANGE_BOOK", payload => {
      this.selectBook(payload);
    });
    EventBus.$on("CLOSE_BOOK_DIALOG", payload => {
      this.bookDialog = false;
    });
    EventBus.$on("GET_BOT_ROW_BOOKS", payload => {
      if (!this.collectionLoading) {
        this.getBooks();
      }
    });
  }
};
</script>
