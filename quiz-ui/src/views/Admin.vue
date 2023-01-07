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
                <div class="form-group mb-6">
                    <input vmodel="username" type="text" class="form-control block
                        w-full
                        px-3
                        py-1.5
                        font-normal
                        text-gray-700
                        bg-white bg-clip-padding
                        rounded
                        focus:border-blue-600"
                        placeholder="Identifiant">
                    <br />
                    <input v-model="password" type="password" class="form-control block
                        w-full
                        px-3
                        py-1.5
                        font-normal
                        text-gray-700
                        bg-white bg-clip-padding
                        rounded
                        focus:border-blue-600"
                        placeholder="Mot de passe">
                </div>
            </p>
            <p>
                <button type="button" @click="Connection" class="
                  w-full
                  px-6
                  py-3
                  bg-blue-600
                  text-white
                  font-medium
                  text-xs
                  uppercase
                  rounded
                  hover:bg-blue-700">Connexion</button>
            </p>
        </form>
    </div>
    <br>
    <div v-if="showErrorMsg">
        <div class=" ml-2 mr-2 text-sm px-5 py-5 border-2 rounded-lg text-black border-blue-600 hover:bg-opacity-40 hover:bg-blue-400 bg-sky-500/50">
            Mauvais mdp
        </div>
    </div>
  </template>

<script>

import quizApiService from "@/services/QuizApiService";
import ParticipationStorageService from '../services/ParticipationStorageService';

export default {
  name: "AdminPage",
  data() {
    return {
      id: "",
      password: "",
      showErrorMsg: false,
    }
  },
  methods: {
    async Connection(){

        try{
            var validation = await quizApiService.postLogin({
                "id": this.id,
                "password": this.password
            });
            if(typeof validation == 'undefined'){
                this.showErrorMsg = true;
            }
            else{
                var token = validation.data["token"];
                ParticipationStorageService.saveToken(token);
                console.log(token);
                this.$router.push('/adminInterface');
            }
        }catch(error){
            console.log("error", error);
        }
        
        
    }
  }
};



</script>