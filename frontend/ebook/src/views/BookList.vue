<template>
<body>
  <v-row no-gutters>
    <v-col cols="12" sm="2">
      <Book/>
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
    <v-row no-gutters>
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
</body>
</template>

<style scoped>

.book {
  margin: 5px;
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
