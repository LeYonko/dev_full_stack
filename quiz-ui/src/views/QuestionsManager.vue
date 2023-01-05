<template>
    <QuestionDisplayVue :question="currentQuestion" @answer-selected="answerClickedHandler"/>
</template>

<script>

import quizApiService from "@/services/QuizApiService";
import QuestionDisplayVue from "@/components/QuestionsDisplay.vue";
import ParticipationStorageService from "@/services/ParticipationStorageService";

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
            userChoise: [],
        }
    },
    components : {
        QuestionDisplayVue
    },
    async created() {
        console.log("Composant Question manager 'created'");
        this.loadQuestionByPosition();
        //
        try{
            var score = await quizApiService.getQuizInfo();
            this.numberOfQuestions = score.data['size'];
        } catch(error){
            
        }
        //
    },
    methods:{
        async loadQuestionByPosition(){
            if(this.currentQuestionPosition <= this.numberOfQuestions){
                try{
                    var question = await quizApiService.getQuestion(this.currentQuestionPosition);
                    console.log(question);
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
            this.currentQuestionPosition+=1; //maj de la position de currrent question en l'incrémentant de 1
            await this.loadQuestionByPosition();
            console.log(this.userChoise); //on affiche la réponse choisi
            if (this.currentQuestionPosition > this.numberOfQuestions){
                this.endQuiz();
            }
        },
        async endQuiz(){
            // à implémenter
            var player = ParticipationStorageService.getPlayerName();
            var data = {
                "playerName": player,
                "answers": this.userChoise,
                //ParticipationStorageService.saveParticipationScore(data);
            }
            var result = await quizApiService.addParticipation(data);
            console.log("score2", result);
            ParticipationStorageService.saveParticipationScore(result.data["score"]);
            this.$router.push('/scoresPage');

        }
    }
}

</script>