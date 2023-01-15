<template>
    <div class="ml-2 mt-2">
        <span class="font-semibold text-xl">Page récapitulative</span>
    </div>
    <br>
    <div class="ml-3 flex">
        <svg class="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z" clip-rule="evenodd"></path></svg>
        Player name : {{ this.username }}
    </div>
    <div v-if="this.score == 10">
        <div class="ml-3 flex">
            <svg class="w-6 h-6 mr-2 flex" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M5 2a1 1 0 011 1v1h1a1 1 0 010 2H6v1a1 1 0 01-2 0V6H3a1 1 0 010-2h1V3a1 1 0 011-1zm0 10a1 1 0 011 1v1h1a1 1 0 110 2H6v1a1 1 0 11-2 0v-1H3a1 1 0 110-2h1v-1a1 1 0 011-1zM12 2a1 1 0 01.967.744L14.146 7.2 17.5 9.134a1 1 0 010 1.732l-3.354 1.935-1.18 4.455a1 1 0 01-1.933 0L9.854 12.8 6.5 10.866a1 1 0 010-1.732l3.354-1.935 1.18-4.455A1 1 0 0112 2z" clip-rule="evenodd"></path></svg>
            Score : {{ this.score }}
        </div>
    </div>
    <div v-else-if="this.score > 6 && this.score < 10">
        <div class="ml-3 flex">
            <svg class="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
            Score : {{ this.score }}
        </div>
    </div>
    <div v-else-if="this.score > 3 && this.score < 7">
        <div class="ml-3 flex">
            <svg class="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM7 9a1 1 0 100-2 1 1 0 000 2zm7-1a1 1 0 11-2 0 1 1 0 012 0zm-.464 5.535a1 1 0 10-1.415-1.414 3 3 0 01-4.242 0 1 1 0 00-1.415 1.414 5 5 0 007.072 0z" clip-rule="evenodd"></path></svg>
            Score : {{ this.score }}
        </div>
    </div>
    <div v-else>
        <div class="ml-3 flex">
            <svg class="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM7 9a1 1 0 100-2 1 1 0 000 2zm7-1a1 1 0 11-2 0 1 1 0 012 0zm-7.536 5.879a1 1 0 001.415 0 3 3 0 014.242 0 1 1 0 001.415-1.415 5 5 0 00-7.072 0 1 1 0 000 1.415z" clip-rule="evenodd"></path></svg>
            Score : {{ this.score }}
        </div>
    </div>
    <div class="ml-5 mt-5">
      <button type="button" @click="home" class="text-sm px-5 py-5 border-2 rounded-lg text-black border-blue-600 hover:bg-opacity-40 hover:bg-blue-400 bg-sky-500/50">
          Page d'accueil
      </button>
    </div>
    <br>
    <div class="ml-2 mt-2">
        <span class="font-semibold text-xl">Réponses</span>
    </div>
    <br>
    <div v-for="question, idx in this.allQuestions" class="ml-2">
        Question : {{ question.title}}
        <br>
        <div v-if="this.scoreColor[idx] == '0'">
            <div class="text-sm ml-6 mr-6 px-4 py-2 border-2 rounded-lg text-black border-blue-500 bg-red-200">
                Votre réponse : {{ question.possibleAnswers[this.allAnswers[idx]-1].text }}
                <br>
                Bonne réponse : {{ question.possibleAnswers[this.allGoodAnswers[idx]-1].text }}
            </div>
        </div>
        <div v-else>
            <div class="text-sm ml-6 mr-6 px-4 py-2 border-2 rounded-lg text-black border-blue-500 bg-green-200">
                Votre réponse : {{ question.possibleAnswers[this.allAnswers[idx]-1].text }}
                <br>
                Bonne réponse : {{ question.possibleAnswers[this.allGoodAnswers[idx]-1].text }}
            </div>
        </div>
        <br>
    </div>
</template>

<script>
import ParticipationStorageService from "@/services/ParticipationStorageService.js"
import quizApiService from "@/services/QuizApiService";

export default{
    data(){
        return{
            username: " ",
            score: " ",
            //
            allAnswers: [],
            allQuestions: [],
            allGoodAnswers: [],
            scoreColor: [],
            currentQuestionPosition: 1,
            numberOfQuestions:1,
            //
        };
    },
    async created(){
        this.username = ParticipationStorageService.getPlayerName();
        this.score = ParticipationStorageService.getParticipationScore();
        var score = await quizApiService.getQuizInfo();
        this.numberOfQuestions = score.data['size'];
        var sizeGoodAnswers = this.listSize(ParticipationStorageService.getGoodAnswers());
        this.allGoodAnswers = this.transformIntoList(ParticipationStorageService.getGoodAnswers(), sizeGoodAnswers, 0, 4); //good answers
        this.scoreColor = this.transformIntoList(ParticipationStorageService.getGoodAnswers(), sizeGoodAnswers, 2, 4);
        var sizeAnswers = this.listSize(ParticipationStorageService.getParticipationAnswers());
        this.allAnswers = this.transformIntoList(ParticipationStorageService.getParticipationAnswers(), sizeAnswers, 0, 2);
        this.loadAllQuestions();
    },
    methods:{
        home(){
            ParticipationStorageService.clear();
            this.$router.push("/");
        },
        listSize(val){
            var cpt = 0;
            for (var elem in val){
                cpt = cpt + 1;
            }
            return cpt;
        },
        transformIntoList(val, size, start, step){
            var list=[]
            for (var i = start; i < size; i = i + step){
                list.push(val[i])
            }
            return list
        },
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
    }
}
</script>