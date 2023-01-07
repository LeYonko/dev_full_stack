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
    <div class="ml-2">
        <br>
        <br>
        <RouterLink to="/addQuestion" class="text-sm px-4 py-2 border-2 rounded-lg text-white border-white bg-blue-500 hover:bg-opacity-40 hover:bg-white">Ajout question</RouterLink>
        <br>
        <br>
        <br>
        <RouterLink to="/deleteQuestion" class="text-sm px-4 py-2 border-2 rounded-lg text-white border-white bg-blue-500 hover:bg-opacity-40 hover:bg-white">Supprimer une question</RouterLink>
        <br>
        <br>
        <br>
        <RouterLink to="/updateQuestion" class="text-sm px-4 py-2 border-2 rounded-lg text-white border-white bg-blue-500 hover:bg-opacity-40 hover:bg-white">Update question</RouterLink>
        <br>
        <br>
        <br>
        <RouterLink to="/deleteAllQuestions" class="text-sm px-4 py-2 border-2 rounded-lg text-white border-white bg-blue-500 hover:bg-opacity-40 hover:bg-white">Supprimer toutes les questions</RouterLink>
        <br>
        <br>
        <br>
        <RouterLink to="/deleteAllParticipations" class="text-sm px-4 py-2 border-2 rounded-lg text-white border-white bg-blue-500 hover:bg-opacity-40 hover:bg-white">Supprimer tous les participants</RouterLink>
    </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default{
    data(){
        return{
            currentQuestionPosition: 1,
            allQuestions: [],
            numberOfQuestions:1,
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
        }
    }
}
</script>