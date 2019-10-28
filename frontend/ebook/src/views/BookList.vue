<template>
  <div>
    <v-dialog v-if="selectedBook" v-model="bookDialog" min-height="900" width="1700">
      <Book :book="selectedBook" />
    </v-dialog>
    <v-container>
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
</template>

<style scoped>
.book {
  padding: 0 10px;
}
</style>

<script>
import Book from "../components/Book.vue";

export default {
  components: {
    Book
  },
  data: () => ({
    bookDialog: false,
    books: [],
    selectedBook: null
  }),
  methods: {
    getBooks() {
      this.$store.dispatch("store/book_list", {}).then(response => {
        if (response != 0) {
          this.books = response.books;
        } else {
          console.log("Error retrieving book_list");
        }
      });
    },
    selectBook(book) {
      this.selectedBook = book;
      console.log(this.selectedBook)
      this.bookDialog = true;
    }
  },
  mounted() {
    this.getBooks();
  }
};
</script>
