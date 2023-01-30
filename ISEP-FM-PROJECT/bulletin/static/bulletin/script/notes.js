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

    tbodylistStudent = document.getElementById('listetudiant')
    // Get the modal For the add 
     modal = document.getElementById("myModal");

    // Get the buttons that open the modal
    var btn = document.getElementsByClassName("myBtn");
    
    /**BOUTON DE FERMETURE NOTES */
    // GET the button that closes the modal
    spanClose = document.getElementsByClassName("close")[0];
    //When the user clicks on span (x), close the modal
    spanClose.onclick = function(){
      /**VIDAGE DU CONTENEUR DE LISTE DES ETUDIANTS */
      //console.log(tbodylistStudent);
    tbodylistStudent.innerHTML=""

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

    /**AJOUT DYNAMIQUE DES REGLES DE VALIDATION AUX INPUT DU FORMULAIRE */
    /*btn[i].onclick=function(){
      
    }*/
  
  /**ITERATION AFIN D'OBTENIR LES LISTES DES ETUDIANTS INSCRITS DANS LES MATIERES */
  for(let i=0; i<btn.length; i++){
    btn[i].onclick = function(){

      if(myArr[i].code_UE.startsWith("EPS1")){
        getetudiantStapsNiveau1()
      }else if(myArr[i].code_UE.startsWith("MDS1")){
        getetudiantMDSNiveau1()
      }else if(myArr[i].code_UE.startsWith("EPS2")){
        getetudiantStapsNiveau2()
      }else if(myArr[i].code_UE.startsWith("MAS")){
        getAllEtudiantNiveau3()
      }else if(myArr[i].code_UE.startsWith("EVE")){
        getetudiantEVENiveau3()
      }else if(myArr[i].code_UE.startsWith("MSO")){
        getetudiantMSONiveau3()
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

    const listUe = document.getElementById("list-ue")

    for(let i=0; i <myArr.length; i++){
        if(myArr[i].semestre_id == 1){
          imgSemestrePath = "/static/bulletin/icones/number_1.png"
        }else if(myArr[i].semestre_id == 2){
          imgSemestrePath = "/static/bulletin/icones/number_2.png"
        }else if(myArr[i].semestre_id == 3){
          imgSemestrePath = "/static/bulletin/icones/number_3.png"
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
     listeTitle.innerText=`BORDOREAU DE NOTES UE --${idUe}-- ANNEE 202X-202X`

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
        tabledata4Input.setAttribute('placeholder', `Note CC ${myEtudiantStaps1[i].matricule}  ${idUe}`)
        tabledata4Input.setAttribute('name',`CC ${myEtudiantStaps1[i].matricule} ${idUe}`)
        tabledata4Input.setAttribute('id',`CC ${myEtudiantStaps1[i].matricule}${idUe}`)
        //tabledata4Input.setAttribute('required', '')
        tabledata4Input.setAttribute('class','noteField')
        //tabledata4Input

        const tabledata4 = document.createElement('td')
        tabledata4.appendChild(tabledata4Input)

        const tabledata5Input = document.createElement('input')
        tabledata5Input.type="text"
        tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantStaps1[i].matricule} ${idUe}`)
        tabledata5Input.setAttribute('name',`SN ${myEtudiantStaps1[i].matricule} ${idUe}`)
        //tabledata5Input.setAttribute('required', '')
        tabledata5Input.setAttribute('class','noteField')
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
    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send(); 
}

/** REQUEST ETUDIANTS MDS NIVEAU 1 */
function getetudiantMDSNiveau1(){
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantMDS1/";

xmlhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
     myEtudiantMDS1 = JSON.parse(this.responseText);

     /** Ajout des lignes pour insertion des notes des étudiants */
     /**Changement du TITRE Du modal */
     listeTitle = document.getElementById('listetudiant-title')
     listeTitle.innerText=`BORDOREAU DE NOTES UE --${idUe}-- ANNEE 202X-202X`
     tbodyMDS1 = document.getElementById('listetudiant')

      for(let i=0; i<myEtudiantMDS1.length; i++){
        const tabledata1 = document.createElement('td')
        tabledata1.setAttribute('scope', 'row')
        tabledata1.innerText = myEtudiantMDS1[i].id

        const tabledata2 = document.createElement('td')
        tabledata2.innerText = myEtudiantMDS1[i].matricule

        var nom = myEtudiantMDS1[i].nom +' '+myEtudiantMDS1[i].prenom
        const tabledata3 = document.createElement('td')
        tabledata3.innerText = nom

        const tabledata4Input = document.createElement('input')
        tabledata4Input.type="text"
        
        tabledata4Input.setAttribute('placeholder', `Note CC ${myEtudiantMDS1[i].matricule}  ${idUe}`)
        tabledata4Input.setAttribute('name',`CC ${myEtudiantMDS1[i].matricule} ${idUe}`)
        tabledata4Input.setAttribute('id',`CC ${myEtudiantMDS1[i].matricule} ${idUe}`)
        //tabledata4Input.setAttribute('required', '');
        tabledata4Input.setAttribute('class','noteField')

        const tabledata4 = document.createElement('td')
        tabledata4.appendChild(tabledata4Input)

        const tabledata5Input = document.createElement('input')
        tabledata5Input.type="text"
        tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantMDS1[i].matricule} ${idUe}`)
        tabledata5Input.setAttribute('name',`SN ${myEtudiantMDS1[i].matricule} ${idUe}`)
        //tabledata5Input.setAttribute('required','');
        tabledata5Input.setAttribute('class','noteField')
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
     
    }
  }
  xmlhttp.open("GET", url, true);
  xmlhttp.send(); 
}

/**  REQUEST ETUDIANT STAPS NIVEAU 2 */
function getetudiantStapsNiveau2(){
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantStaps2/";

xmlhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
     myEtudiantStaps2 = JSON.parse(this.responseText);

     /** Ajout des lignes pour insertion des notes des étudiants */
     /**Changement du TITRE Du modal */
     listeTitle = document.getElementById('listetudiant-title')
     //console.log(listeTitle);
     //listeTitle.innerHTML=""

     listeTitle.innerText=`BORDOREAU DE NOTES UE --${idUe}-- ANNEE 202X-202X`

      for(let i=0; i<myEtudiantStaps2.length; i++){
        const tabledata1 = document.createElement('td')
        tabledata1.setAttribute('scope', 'row')
        tabledata1.innerText = myEtudiantStaps2[i].id

        const tabledata2 = document.createElement('td')
        tabledata2.innerText = myEtudiantStaps2[i].matricule

        var nom = myEtudiantStaps2[i].nom +' '+myEtudiantStaps2[i].prenom
        const tabledata3 = document.createElement('td')
        tabledata3.innerText = nom

        const tabledata4Input = document.createElement('input')
        tabledata4Input.type="text"
        tabledata4Input.setAttribute('placeholder', `Note CC ${myEtudiantStaps2[i].matricule}  ${idUe}`)
        tabledata4Input.setAttribute('name',`CC ${myEtudiantStaps2[i].matricule} ${idUe}`)
        tabledata4Input.setAttribute('id',`CC ${myEtudiantStaps2[i].matricule} ${idUe}`)
        //tabledata4Input.setAttribute('required','')
        tabledata4Input.setAttribute('class','noteField')

        const tabledata4 = document.createElement('td')
        tabledata4.appendChild(tabledata4Input)

        const tabledata5Input = document.createElement('input')
        tabledata5Input.type="text"
        tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantStaps2[i].matricule} ${idUe}`)
        tabledata5Input.setAttribute('name',`SN ${myEtudiantStaps2[i].matricule} ${idUe}`)
        //tabledata5Input.setAttribute('required','');
        tabledata5Input.setAttribute('class','noteField')
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
     
    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send(); 
}

/**REQUEST ETUDIANT NIVEAU 3 */
function getAllEtudiantNiveau3(){
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantNiveau3/";

xmlhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
     myEtudiantNiveau3 = JSON.parse(this.responseText);

     /** Ajout des lignes pour insertion des notes des étudiants */
     /**Changement du TITRE Du modal */
     listeTitle = document.getElementById('listetudiant-title')
     listeTitle.innerText=`BORDOREAU DE NOTES UE --${idUe}-- ANNEE 202X-202X`

      for(let i=0; i<myEtudiantNiveau3.length; i++){
        const tabledata1 = document.createElement('td')
        tabledata1.setAttribute('scope', 'row')
        tabledata1.innerText = myEtudiantNiveau3[i].id

        const tabledata2 = document.createElement('td')
        tabledata2.innerText = myEtudiantNiveau3[i].matricule

        var nom = myEtudiantNiveau3[i].nom +' '+myEtudiantNiveau3[i].prenom
        const tabledata3 = document.createElement('td')
        tabledata3.innerText = nom

        const tabledata4Input = document.createElement('input')
        tabledata4Input.type="text"
        //console.log(element.parentElement.parentElement.parentElement.parentElement.children[0].innerText);
        tabledata4Input.setAttribute('placeholder', `Note CC ${myEtudiantNiveau3[i].matricule}  ${idUe}`)
        tabledata4Input.setAttribute('name',`CC ${myEtudiantNiveau3[i].matricule} ${idUe}`)
        tabledata4Input.setAttribute('id',`CC ${myEtudiantMDS1[i].matricule} ${idUe}`)
       //tabledata4Input.setAttribute('required','')
        tabledata4Input.setAttribute('class','noteField')

        const tabledata4 = document.createElement('td')
        tabledata4.appendChild(tabledata4Input)

        const tabledata5Input = document.createElement('input')
        tabledata5Input.type="text"
        tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantNiveau3[i].matricule} ${idUe}`)
        tabledata5Input.setAttribute('name',`SN ${myEtudiantNiveau3[i].matricule} ${idUe}`)
       //tabledata5Input.setAttribute('required', '');
        tabledata5Input.setAttribute('class','noteField')
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
     
    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send(); 
}

/** REQUEST ETUDIANTS EVE */
function getetudiantEVENiveau3(){
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantNiveau3EVE/";

xmlhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
     myEtudiantNiveau3EVE = JSON.parse(this.responseText);

     /** Ajout des lignes pour insertion des notes des étudiants */
     /**Changement du TITRE Du modal */
     listeTitle = document.getElementById('listetudiant-title')
     listeTitle.innerText=`BORDOREAU DE NOTES UE --${idUe}-- ANNEE 202X-202X`

      for(let i=0; i<myEtudiantNiveau3EVE.length; i++){
        const tabledata1 = document.createElement('td')
        tabledata1.setAttribute('scope', 'row')
        tabledata1.innerText = myEtudiantNiveau3EVE[i].id

        const tabledata2 = document.createElement('td')
        tabledata2.innerText = myEtudiantNiveau3EVE[i].matricule

        var nom = myEtudiantNiveau3EVE[i].nom +' '+myEtudiantNiveau3EVE[i].prenom
        const tabledata3 = document.createElement('td')
        tabledata3.innerText = nom

        const tabledata4Input = document.createElement('input')
        tabledata4Input.type="text"
        //console.log(element.parentElement.parentElement.parentElement.parentElement.children[0].innerText);
        tabledata4Input.setAttribute('placeholder', `Note CC ${myEtudiantNiveau3EVE[i].matricule}  ${idUe}`)
        tabledata4Input.setAttribute('name',`CC ${myEtudiantNiveau3EVE[i].matricule} ${idUe}`)
        tabledata4Input.setAttribute('id',`CC ${myEtudiantMDS1[i].matricule} ${idUe}`)
        //tabledata4Input.setAttribute('required','')
        tabledata4Input.setAttribute('class','noteField')

        const tabledata4 = document.createElement('td')
        tabledata4.appendChild(tabledata4Input)

        const tabledata5Input = document.createElement('input')
        tabledata5Input.type="text"
        tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantNiveau3EVE[i].matricule} ${idUe}`)
        tabledata5Input.setAttribute('name',`SN ${myEtudiantNiveau3EVE[i].matricule} ${idUe}`)
        //tabledata5Input.setAttribute('required','');
        tabledata5Input.setAttribute('class','noteField')
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
     
    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send(); 
}

/** REQUEST ETUDIANTS MSO */
function getetudiantMSONiveau3(){
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantNiveau3MSO/";

xmlhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
     myEtudiantNiveau3MSO = JSON.parse(this.responseText);

     /** Ajout des lignes pour insertion des notes des étudiants */
     /**Changement du TITRE Du modal */
     listeTitle = document.getElementById('listetudiant-title')
     listeTitle.innerText=`BORDOREAU DE NOTES UE --${idUe}-- ANNEE 202X-202X`

      for(let i=0; i<myEtudiantNiveau3MSO.length; i++){
        const tabledata1 = document.createElement('td')
        tabledata1.setAttribute('scope', 'row')
        tabledata1.innerText = myEtudiantNiveau3MSO[i].id

        const tabledata2 = document.createElement('td')
        tabledata2.innerText = myEtudiantNiveau3MSO[i].matricule

        var nom = myEtudiantNiveau3MSO[i].nom +' '+myEtudiantNiveau3MSO[i].prenom
        const tabledata3 = document.createElement('td')
        tabledata3.innerText = nom

        const tabledata4Input = document.createElement('input')
        tabledata4Input.type="text"
        //console.log(element.parentElement.parentElement.parentElement.parentElement.children[0].innerText);
        tabledata4Input.setAttribute('placeholder', `Note CC ${myEtudiantNiveau3MSO[i].matricule}  ${idUe}`)
        tabledata4Input.setAttribute('name',`CC ${myEtudiantNiveau3MSO[i].matricule} ${idUe}`)
        tabledata4Input.setAttribute('id',`CC ${myEtudiantMDS1[i].matricule} ${idUe}`)
        //tabledata4Input.setAttribute('required', '')
        tabledata4Input.setAttribute('class','noteField')

        const tabledata4 = document.createElement('td')
        tabledata4.appendChild(tabledata4Input)

        const tabledata5Input = document.createElement('input')
        tabledata5Input.type="text"
        tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantNiveau3MSO[i].matricule} ${idUe}`)
        tabledata5Input.setAttribute('name',`SN ${myEtudiantNiveau3MSO[i].matricule} ${idUe}`)
        //tabledata5Input.setAttribute('required', '')
        tabledata5Input.setAttribute('class','noteField')
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
     
    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send(); 
}

/** SEND DATA TO THE SERVER */
$(function () {
  dataString = $("#myForm").serializeArray()
  options = {
    //data : dataString,
    //target:"",
    url:'ajoutNoteEtudiant/',
    type:"POST",
    success: "",
  }
    /**Validation par classe */
  jQuery.validator.addClassRules("noteField", {
    required: true,
  });

  $("form").submit(function(e){
    e.preventDefault();

    console.log('OK');
     
  }).validate({
    submitHandler: function(form){
      
        $("#myForm").ajaxSubmit(options)
        tbodylistStudent.innerHTML=""

        modal.style.display = "none";
        alert(`LES NOTES ONT ETE ENREGISTREES AVEC SUCCESS`)
    }
  });
})
