<template>
    <div class="newsQuiz ml-2 mt-2">
      <h1>
          <span class="font-semibold text-xl">Page de connexion administrateur</span>
      </h1>
      <br>
    </div>
    <div class="block p-5 rounded-lg bg-gradient-to-r from-violet-400 to-fuchsia-400 max-w-sm ml-5">
      <form>
          <p>
              <label for="password"> Saisissez le mot de passe : </label>
              <br>
              <br>
              <div class="form-group mb-6">
                  <input vmodel="password" type="text" class="form-control block
                  w-full
                  px-3
                  py-1.5
                  font-normal
                  text-gray-700
                  bg-white bg-clip-padding
                  rounded
                  focus:border-blue-600"
                  placeholder="Password">
              </div>
          </p>
          <p>
              <button type="button" @clickk="launchNewQuiz" class="
                  w-full
                  px-6
                  py-3
                  bg-blue-600
                  text-white
                  font-medium
                  text-xs
                  uppercase
                  rounded
                  hover:bg-blue-700">Connexion
              </button>
          </p>
      </form>
    </div>
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
        //console.log("Launch new quiz with", this.username);
        participationStorageService.savePlayerName(this.username);
        const playerName = participationStorageService.getPlayerName();
        this.$router.push('/questions');
      },
    }
  };
  </script>