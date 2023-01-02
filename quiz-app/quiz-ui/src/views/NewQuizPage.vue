<template>
  <div class="newQuiz">
    <h1> Register Page </h1>
  </div>
  <form>
    <p>
      <label for="username"> Saisissez votre nom : </label>
      <br />
      <input v-model="username" type="text" placeholder="Username">
      <!-- Vérification du bon fonctionnement du v-binding
        <p>{{ username }}</p>
      -->
      <br />
      <br />
    </p>
    <p>
      <button type="button" @click="launchNewQuiz">Start</button>
    </p>
  </form>

</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      username: ''
    };
  },
  methods: {
    launchNewQuiz() {
      console.log("Launch new quiz with", this.username);
      participationStorageService.savePlayerName(this.username);
      const playerName = participationStorageService.getPlayerName();
      this.$router.push('/questions');
    },
  }
};
</script>


<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
