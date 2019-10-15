<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12" sm="2">
          <Book />
        </v-col>
        <v-col cols="12" sm="2">
          <Book />
        </v-col>
        <v-col cols="12" sm="2">
          <Book />
        </v-col>
        <v-col cols="12" sm="2">
          <Book />
        </v-col>
        <v-col cols="12" sm="2">
          <Book />
        </v-col>
        <v-col cols="12" sm="2">
          <Book />
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" sm="2">
          <Book />
        </v-col>
        <v-col cols="12" sm="2">
          <Book />
        </v-col>
        <v-col cols="12" sm="2">
          <Book />
        </v-col>
        <v-col cols="12" sm="2">
          <Book />
        </v-col>
        <v-col cols="12" sm="2">
          <Book />
        </v-col>
        <v-col cols="12" sm="2">
          <Book />
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
import Book from "../components/Book";

export default {
  components: {
    Book
  }
};
</script>
