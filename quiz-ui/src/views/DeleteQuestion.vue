<template>
    <div class="ml-2 mt-2">
        <span class="font-semibold text-xl">Toutes les questions</span>
    </div>
    <br>
    <div v-for="question, idx in this.allQuestions" class="ml-2">
        Question {{ question.position }} : {{ question.title}}
        <br>
    </div>
    <br>
    <br>
    <div class="ml-2">
        <label class="style"> Position de la question à supprimer : </label>
        <br />
        <br />
        <input v-model="position" type="text" placeholder="Position">
        <br />
    </div>
    <br />
    <button type="button" class="text-sm ml-2 px-4 py-2 border-2 rounded-lg text-white bg-blue-500 border-blue-500 hover:bg-blue-400" @click="deleteOneQuestion">Supprimer</button>
    <br>
    <br>
    <button type="button">
        <RouterLink to="/adminInterface" class="text-sm ml-2 px-4 py-2 border-2 rounded-lg text-white bg-blue-500 border-blue-500 hover:bg-blue-400">Retour</RouterLink>
    </button>
</template>


<script>
import quizApiService from "@/services/QuizApiService";
import ParticipationStorageService from '../services/ParticipationStorageService';

export default{
    data(){
        return{
            position: "",
            allQuestions: [],
            numberOfQuestions: 1,
            currentQuestionPosition: 1,
            //
        };
    },
    async created(){
        var score = await quizApiService.getQuizInfo();
        this.numberOfQuestions = score.data['size'];
        this.loadAllQuestions();
    },
    methods:{
        async loadAllQuestions(){
            try{
                this.currentQuestionPosition = 1;
                for(this.currentQuestionPosition; this.currentQuestionPosition <= this.numberOfQuestions; this.currentQuestionPosition++){
                    var question = await quizApiService.getQuestion(this.currentQuestionPosition);
                    this.allQuestions.push(question.data);
                }
            }
            catch(error){

            }
        },
        async deleteOneQuestion(){
            var token = ParticipationStorageService.getToken();
            var question = await quizApiService.getQuestion(this.position);
            var reponse = await quizApiService.deleteQuestion(question.data["id"], token);
            if (reponse == undefined){
                this.$router.push("/admin");
            }
            else{
                this.$router.push("/adminInterface");
            }
        }
    }
}
</script>