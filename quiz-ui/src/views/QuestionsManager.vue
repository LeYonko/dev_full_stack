<template>
    <h1> Question manager</h1>
    <QuestionDisplayVue :question="currentQuestion" @choice="answerClickedHandler"/>
</template>

<script>

import quizApiService from "@/services/QuizApiService";
import QuestionDisplayVue from "@/components/QuestionsDisplay.vue";
//import ParticipationStorageService from "../../services/ParticipationStorageService";

export default {
    data(){
        return{
            currentQuestion: {
                questionTitle: "",
                questionText: "",
                possibleAnswer: [],
            },
            currentQuestionPosition: 1,
            numberOfQuestions:1,
            userChoise: []
            }
        },
    components : {
        QuestionDisplayVue
    },
    async created() {
        console.log("Composant Question manager 'created'");
        await this.loadQuestionByPosition();
    },
    methods:{
        async loadQuestionByPosition(){
            if(this.currentQuestionPosition <= this.numberOfQuestions){
                try{
                    var question = await quizApiService.getQuestion(this.currentQuestionPosition);
                    this.currentQuestion=question.data;
                    }
                    catch(error){

                    }
                }
                else{

                }
            },
        async answerClickedHandler(position){
            this.userChoise.push(position);
            this.currentQuestionPosition+1; //maj de la position de currrent question en l'incrémentant de 1
            await this.loadQuestionByPosition();
            console.log(this.userChoise); //on affiche la réponse choisi
        },
        async endQuiz(){
            // à implémenter
            
        }
    }
}

</script>