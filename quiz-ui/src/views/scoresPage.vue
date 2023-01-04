<template>
    <h1>
        {{ this.username }}, ton score est de {{ this.score }}!!
    </h1>
    <h2>
        Clique sur ce bouton pour revenir à la page d'accueil !
    </h2>
    <button type="button" @click="home"> Page d'accueil </button>
</template>

<script>
import ParticipationStorageService from "@/services/ParticipationStorageService.vue"

export default{
    data(){
        return{
            username: " ",
            score: " "

        };
    },
    created(){
        this.username = ParticipationStorageService.getPlayerName();
        this.score = ParticipationStorageService.getParticipationScore();
    },
    methods:{
        home(){
            this.$router.push("/");
        }

    }
}


</script>