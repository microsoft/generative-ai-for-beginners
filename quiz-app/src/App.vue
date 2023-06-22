<template>
  <div>
    <nav>
      <router-link class="navlink" to="/">Home</router-link>
      <label for="locale">locale</label>
      <select v-model="native_name">
        <option v-for="lan in iso_639_1_map_keys" :key="lan">
          {{ lan }}
        </option>
      </select>
    </nav>
    <div id="app">
      <h1>{{ $t("title") }}</h1>
      <router-view>
        <Quiz />
      </router-view>
    </div>
  </div>
</template>

<script>
import Quiz from "@/components/Quiz.vue";
import messages from "@/assets/translations";

export default {
  name: "App",
  i18n: { messages },
  components: {
    Quiz,
  },
  data() {
    return {
      native_name: "English",

      // Native names are from
      // https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
      iso_639_1_map: {
        "العربية": "ar",
        "বাংলা": "bn",
        "English": "en",
        "中文 - 大陆简体": "zh-cn",
      },
    };
  },
  computed: {
    iso_639_1_map_keys() {
      return Object.keys(this.iso_639_1_map);
    }
  },
  watch: {
    native_name(val) {
      this.$root.$i18n.locale = this.iso_639_1_map[val];
    },
  },
  created() {
    if (this.$route.query.loc) {
      this.locale = this.$route.query.loc;
    }
  },
};
</script>

<style>
html {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #252d4a;
}
nav {
  background-color: #252d4a;
  padding: 1em;
  margin-bottom: 20px;
}

nav a {
  color: white;
  text-align: right;
}

.link {
  display: list-item;
}

h1,
h2,
h3,
.message {
  text-align: center;
}
.error {
  color: red;
}
.card {
  width: 60%;
  border: #252d4a solid;
  border-radius: 5px;
  margin: auto;
  padding: 1em;
}
.btn {
  min-width: 50%;
  font-size: 16px;
  text-align: center;
  cursor: pointer;
  margin-bottom: 5px;
  width: 50%;
  font-size: 16px;
  color: #ffffff;
  background-color: #252d4a;
  border-radius: 5px;
  padding: 5px;
  justify-content: flex-start;
  align-items: center;
}
.ans-btn {
  justify-content: center;
  display: flex;
  margin: 4px auto;
}
</style>
