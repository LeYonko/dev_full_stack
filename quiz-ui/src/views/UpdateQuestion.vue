<template>
    <div class="ml-2">
        <div class="addQuestion mt-2">
            <span class="font-semibold text-xl">Ajout d'une question</span>
        </div>
        <br>
        <form>
        <p>
            <label class="style"> Intitulé de la question : </label>
            <br />
            <input v-model="title" type="text" placeholder="Intitulé question">
            <br />
            <br>
            <label class="style"> Texte de la question : </label>
            <br />
            <input v-model="text" type="text" placeholder="Texte question">
            <br />
            <br />
            <label for="style"> Position : </label>
            <br />
            <input v-model="position" type="number" placeholder="Position">
            <br>
        </p>
        <p>
            <br>
            <label class="style"> Réponse 1: 
                <input v-model="choix1" type="text" placeholder="Réponse 1">
                <label for="checkbox"> La bonne réponse : </label>
                <input v-model="choixBooleen1" :disabled="choixBooleen2 || choixBooleen3 || choixBooleen4" type="checkbox" :value="1">
            </label>
            <br/>
            <br/>
            <label class="style"> Réponse 2: 
                <input v-model="choix2" type="text" placeholder="Réponse 2">
                <label for="checkbox"> La bonne réponse : </label>
                <input v-model="choixBooleen2" :disabled="choixBooleen1 || choixBooleen3 || choixBooleen4" type="checkbox" :value="2">
            </label>
            <br/>
            <br/>
            <label class="style"> Réponse 3: 
                <input v-model="choix3" type="text" placeholder="Réponse 3">
                <label for="checkbox"> La bonne réponse : </label>
                <input v-model="choixBooleen3" :disabled="choixBooleen1 || choixBooleen2 || choixBooleen4" type="checkbox" :value="3">
            </label>
            <br/>
            <br/>
            <label class="style"> Réponse 4: 
                <input v-model="choix4" type="text" placeholder="Réponse 4">
                <label for="checkbox"> La bonne réponse : </label>
                <input v-model="choixBooleen4" :disabled="choixBooleen1 || choixBooleen2 || choixBooleen3" type="checkbox" :value="4">
            </label>
            <br/>
            <br/>
            <label class="style"> Image question </label>
            <br>
            <br>
            <ImageUpload @file-change="imageFileChangedHandler" />
        </p>
        <br>  
        <button type="button" class="text-sm px-4 py-2 border-2 rounded-lg text-white bg-blue-500 border-blue-500 hover:bg-blue-400" @click="send">Modifier</button>
        </form>
        <br>
        <br>
        <button type="button">
            <RouterLink to="/adminInterface" class="text-sm px-4 py-2 border-2 rounded-lg text-white bg-blue-500 border-blue-500 hover:bg-blue-400">Retour</RouterLink>
        </button>
    </div>
</template>

<script>
import quizApiService from '@/services/QuizApiService';
import ParticipationStorageService from '../services/ParticipationStorageService';
import ImageUpload from '../components/ImageUpload.vue';

export default{
    data(){
        return{ 
            text: "",
            title: "",
            image: "",
            position: '',
            possibleAnswers: [],
            choix1: "",
            choix2: "",
            choix3: "",
            choix4: "",
            choixBooleen1: false,
            choixBooleen2: false,
            choixBooleen3: false,
            choixBooleen4: false,
        }
    },
    components : {
        ImageUpload
    },
    methods:{
        imageFileChangedHandler(b64String) {
            this.image = b64String;
        },
        async send(){
            var data = this.questionCreation();
            console.log(data);
            var token = ParticipationStorageService.getToken();
            var question = await quizApiService.getQuestion(this.position);
            var reponse = await quizApiService.updateQuestion(data, question.data["id"], token);
            if (reponse == undefined){
                this.$router.push("/admin");
            }
            else{
                this.$router.push("/adminInterface");
            }
        },
        questionCreation(){
            var reponse = {
                "text" : this.text,
                "title" : this.title,
                "image": this.image,
                "position": this.position,
                "possibleAnswers": [
                    {
                        "text": this.choix1,
                        "isCorrect": this.choixBooleen1
                    },
                    {
                        "text": this.choix2,
                        "isCorrect": this.choixBooleen2
                    },
                    {
                        "text": this.choix3,
                        "isCorrect": this.choixBooleen3
                    },
                    {
                        "text": this.choix4,
                        "isCorrect": this.choixBooleen4
                    }
                ]
            };
            return reponse;
        }
        }
    }


</script>