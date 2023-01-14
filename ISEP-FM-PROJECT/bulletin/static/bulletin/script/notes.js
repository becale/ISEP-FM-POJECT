title = document.getElementById('listetudiant-title')
console.log(title);

/** GET THE ID OF Buttons */
function getButtonId(){
  // Create event listener
    document.addEventListener('click', (e) =>
      {
        // Retrieve id from clicked element
        if (e.target.id !== '' && e.target.tagName == 'BUTTON'){
            //console.log(e.target.parentElement.parentElement.parentElement.parentElement.children[0].innerText);
            idUe = e.target.parentElement.parentElement.parentElement.parentElement.children[0].innerText
            //
        }
        else{// If element has no id
          console.log(`object doesn't have ID`);
          console.log(idUe);
        }
      }
    );
}
getButtonId()


/********************************** MODAL *************************************************/
function modal(){
      // Get the modal For the add 
    var modal = document.getElementById("myModal");
     listeTitle = document.getElementsByTagName('h2')
    //console.log(listeTitle.innerText=`LISTE DES ETUDIANTS INSCRITS A L'UE ${idUe} POUR L'ANNEE 202X-202X`)


    // Get the buttons that open the modal
    var btn = document.getElementsByClassName("myBtn");

    /**BOUTON DE FERMETURE NOTES */
    // GET the button that closes the modal
    var spanClose = document.getElementsByClassName("close")[0];
    //When the user clicks on span (x), close the modal
    spanClose.onclick = function(){
      /**VIDAGE DU CONTENEUR DE LISTE DES ETUDIANTS */
      tbodyStaps1.innerHTML=""
      modal.style.display = "none";
    }

/*****BOUTON DE MODIFICATION NOTES */
// Get the buttons that open the modal
//var btn1 = document.getElementsByClassName("myBtn-1");

//var btn = document.getElementById("myBtn");
// GET the button that closes the modal
//var spanClose = document.getElementsByClassName("close")[0];
// when the user clicks the button, open the modal
/*for(let i=0; i<btn1.length; i++){
btn1[i].onclick = function(){
  modal.style.display = "block"
  };
}*/

/**ITERATION AFIN D'OBTENIR LES LISTES DES ETUDIANTS INSCRITS DANS LES MATIERES */
for(let i=0; i<btn.length; i++){
  btn[i].onclick = function(){
    if(myArr[i].code_UE.startsWith("EPS 1")){
      getetudiantStapsNiveau1()
    }else if(test.startsWith("EPS 2")){
      //getetudiantStapsNiveau2()
    }else if(test.startsWith("MDS 1")){
      //getetudiantMDSNiveau1()
    }else if(test.startsWith("MAS ")){
      //getAllEtudiantNiveau3()
    }else if(test.startsWith("EVE")){
      //getetudiantEVENiveau3()
    }else if(test.startsWith("MSO")){
      //getetudiantMSONiveau3()
    }
      modal.style.display = "block"
    };
  }
}

/******************************** REQUEST *************************************************************/
function getUe(){
  var xmlhttp = new XMLHttpRequest();
var url = "http://localhost:8000/UeAPI/";

xmlhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
     myArr = JSON.parse(this.responseText);
     //console.log(myArr);
    
    const listUe = document.getElementById("list-ue")

    for(let i=0; i <myArr.length; i++){
        if(myArr[i].semestre_id == 1){
          imgSemestrePath = "/static/bulletin/icones/number_1.png"
        }else if(myArr[i].semestre_id == 2){
          imgSemestrePath = "/static/bulletin/icones/number_2.png"
        }
        var imgSemestre = document.createElement('img')
        imgSemestre.setAttribute('src',imgSemestrePath)
        imgSemestre.setAttribute('alt','One')

        const numeroSemestre = document.createElement('div')
        numeroSemestre.setAttribute("id", "numero-semestre")
        numeroSemestre.appendChild(imgSemestre)

        const codeMatiere = document.createElement('div')
        codeMatiere.setAttribute("id", "code-matiere")
        var codeMatiereValeur = document.createTextNode(myArr[i].code_UE)
        codeMatiere.appendChild(codeMatiereValeur)

        const numeroSemestreCodeMatiere = document.createElement("div")
        numeroSemestreCodeMatiere.setAttribute('id', "numero-semestre-code-matiere")
        numeroSemestreCodeMatiere.appendChild(numeroSemestre)
        numeroSemestreCodeMatiere.appendChild(codeMatiere)

        /** MILIEU CARD */
        const intituleMatiere = document.createElement('div')
        intituleMatiere.setAttribute('id','intitule-matiere')
        var UeTitle = document.createTextNode(myArr[i].intitule_UE)
        intituleMatiere.appendChild(UeTitle)

        /** FIN CARD */
        /*const imgbtn = document.createElement('img')
        let addPathImg = "/static/bulletin/icones/add.png"
        imgbtn.setAttribute("src", addPathImg)*/

        const myBtn = document.createElement('button')
        myBtn.setAttribute('id', `myBtn${i}`)
        myBtn.setAttribute('class', 'myBtn')

        const imgbtn1 = document.createElement('img')
        let addPathImg1 = "/static/bulletin/icones/edit.png"
        imgbtn1.setAttribute("src", addPathImg1)

        const myBtn1 = document.createElement('button')
        myBtn1.setAttribute('id', `myBtn`)
        myBtn1.setAttribute('class', 'myBtn-1')
        myBtn1.appendChild(imgbtn1)

        const add = document.createElement('div')
        add.setAttribute("id", "add")
        add.appendChild(myBtn)

        const modify = document.createElement('div')
        modify.setAttribute("id", "modify")
        modify.appendChild(myBtn1)

        const bigBoy = document.createElement('div')
        bigBoy.setAttribute('id', `big-boy`)
        bigBoy.appendChild(add)
        bigBoy.appendChild(modify)

        const addModifyMatiere = document.createElement('div')
        addModifyMatiere.setAttribute("id", "add-modify-matiere")
        addModifyMatiere.appendChild(bigBoy)

        const matiere= document.createElement("div")
        matiere.setAttribute("class", "matiere")
        matiere.setAttribute("id", `matiere${i}`)
        matiere.appendChild(numeroSemestreCodeMatiere)
        matiere.appendChild(intituleMatiere)
        matiere.appendChild(addModifyMatiere)

        listUe.appendChild(matiere)
      }
      
      modal()
    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send(); 
}
getUe()

/** REQUEST ETUDIANTS STAPTS NIVEAU 1 */
function getetudiantStapsNiveau1(){
  var xmlhttp = new XMLHttpRequest();
var url = "http://localhost:8000/etudiantStaps1/";

xmlhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
     myEtudiantStaps1 = JSON.parse(this.responseText);

     /** Ajout des lignes pour insertion des notes des étudiants */
     /**Changement du TITRE Du modal */
     listeTitle = document.getElementById('listetudiant-title')
     console.log(listeTitle);
     listeTitle.innerHTML=""

     //listeTitle.innerText=`LISTE DES ETUDIANTS INSCRITS A L'UE ${idUe} POUR L'ANNEE 202X-202X`
     tbodyStaps1 = document.getElementById('listetudiant')

    /*if(1/*tbodyStaps1.childElementCount*/ /*<= 0){*/
      for(let i=0; i<myEtudiantStaps1.length; i++){
        const tabledata1 = document.createElement('td')
        tabledata1.setAttribute('scope', 'row')
        tabledata1.innerText = myEtudiantStaps1[i].id

        const tabledata2 = document.createElement('td')
        tabledata2.innerText = myEtudiantStaps1[i].matricule

        var nom = myEtudiantStaps1[i].nom +' '+myEtudiantStaps1[i].prenom
        const tabledata3 = document.createElement('td')
        tabledata3.innerText = nom

        const tabledata4Input = document.createElement('input')
        tabledata4Input.type="text"
        //console.log(element.parentElement.parentElement.parentElement.parentElement.children[0].innerText);
        tabledata4Input.setAttribute('placeholder', `Note CC ${myEtudiantStaps1[i].matricule}  ${idUe}`)
        tabledata4Input.setAttribute('name',`CC ${myEtudiantStaps1[i].matricule} ${idUe}`)

        const tabledata4 = document.createElement('td')
        tabledata4.appendChild(tabledata4Input)

        const tabledata5Input = document.createElement('input')
        tabledata5Input.type="text"
        tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantStaps1[i].matricule} ${idUe}`)
        tabledata5Input.setAttribute('name',`SN ${myEtudiantStaps1[i].matricule} ${idUe}`)
        const tabledata5 = document.createElement('td')
        tabledata5.appendChild(tabledata5Input)

        const ligne = document.createElement('tr')
        ligne.appendChild(tabledata1);
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4);
        ligne.appendChild(tabledata5);


        /** TBODDY du modal afin d'ajouter les étudiants par filière */
        const listStudent = document.getElementById('listetudiant')
        listStudent.appendChild(ligne)
     }
    /*}*/
     
    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send(); 
}

