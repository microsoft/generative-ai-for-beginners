<template>
  <div>
    <router-link
      v-for="q in questions"
      :key="q.id"
      :to="`quiz/${q.id}`"
      class="link"
    >
      {{ q.title }}
    </router-link>
  </div>
</template>

<script>
import messages from "@/assets/translations";

export default {
  name: "Home",
  computed: {
    questions() {
      return this.$t("quizzes");
    },
  },
  i18n: { messages },
};
</script>