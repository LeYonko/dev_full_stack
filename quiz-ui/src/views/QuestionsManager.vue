<template>
    <QuestionDisplayVue :question="currentQuestion" :numberOfQuestion="numberOfQuestions" @answer-selected="answerClickedHandler"/>
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
        //console.log("Composant Question manager 'created'");
        this.loadQuestionByPosition();
        try{
            var score = await quizApiService.getQuizInfo();
            this.numberOfQuestions = score.data['size'];
        } catch(error){
            console.log(error);
        }
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
                    console.log(error);
                }
            }
            else{
                this.endQuiz();
            }
        },
        async answerClickedHandler(position){
            this.userChoise.push(position);
            this.currentQuestionPosition+=1;
            await this.loadQuestionByPosition();
            //console.log(this.userChoise); //on affiche la réponse choisi
            if (this.currentQuestionPosition > this.numberOfQuestions){
                this.endQuiz();
            }
        },
        async endQuiz(){
            var player = ParticipationStorageService.getPlayerName();
            var data = {
                "playerName": player,
                "answers": this.userChoise,
            }
            var result = await quizApiService.addParticipation(data);
            //console.log("score", result);
            ParticipationStorageService.saveParticipationScore(result.data["score"]);
            ParticipationStorageService.saveParticipationAnswers(this.userChoise);
            ParticipationStorageService.saveGoodAnswers(result.data["answersSummaries"]);
            this.$router.push('/scoresPage');

        }
    }
}

</script>