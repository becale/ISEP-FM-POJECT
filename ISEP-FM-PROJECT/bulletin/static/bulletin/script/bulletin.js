/** GET THE ID OF Buttons */
function getButtonId(){
    // Create event listener
      document.addEventListener('click', (e) =>
        {
          // Retrieve id from clicked element
          if (e.target.id !== '' && e.target.tagName == 'BUTTON'){
            //idUe = ""
              //console.log(e.target.parentElement.parentElement.parentElement.parentElement.children[0].innerText);
              idUe = e.target.parentElement.parentElement.parentElement.children[0].innerText//.parentElement.children[0].innerText
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
        console.log(btn[i].parentElement.parentElement.parentElement.children[0].innerText);
        if (btn[i].parentElement.parentElement.parentElement.children[0].innerText == "STAPS1"){
            getetudiantStapsNiveau1()
        }else if(btn[i].parentElement.parentElement.parentElement.children[0].innerText == "GESTION"){
            getetudiantMDSNiveau1()
        }else if(btn[i].parentElement.parentElement.parentElement.children[0].innerText == "STAPS2"){
            getetudiantStapsNiveau2()
        }else if(btn[i].parentElement.parentElement.parentElement.children[1].innerText == "MANAGEMENT STRATEGIQUE DES EVENEMENTS SPORTIFS"){
            getetudiantMSONiveau3()
        }
      /*if(1/*idUe=="EPS1"){
        getetudiantStapsNiveau1()
      /*}else if(idUe="GESTION"){
        getetudiantMDSNiveau1()
      /*}else if(myArr[i].code_UE.startsWith("EPS2")){
        getetudiantStapsNiveau2()
      }else if(myArr[i].code_UE.startsWith("MAS")){
        getAllEtudiantNiveau3()
      }else if(myArr[i].code_UE.startsWith("EVE")){
        getetudiantEVENiveau3()
      }else if(myArr[i].code_UE.startsWith("MSO")){
        getetudiantMSONiveau3()
      }*/
        modal.style.display = "block"
      /*};*/
    }  
 }
}

/**
 * FONCTION CHARGEE DE LA CREATION DES SEMESTRES-SPECIALITES 
 */
function createSemestre() { 
    filiereSpe1=["GESTION","STAPS1"];
    specialite=["MANAGEMENT DU SPORT","EDUCATION PHYSIQUE ET SPORTIVE"]
    filiereSpe2="STAPS2";
    specialite2="EDUCATION PHYSIQUE ET SPORTIVE";

    filiereSpe3="LP3MOIS"
    specialite3=["EVENEMENTIEL","MANAGEMENT STRATEGIQUE DES EVENEMENTS SPORTIFS"]

    const listUe = document.getElementById("list-ue")

    //Semestre N01 STAPS ET GESTION
    for(let i=0; i<filiereSpe1.length; i++){
        /*if(i==1){
            */imgSemestrePath = "/static/bulletin/icones/number_1.png"
        /*}else if(i==2){
            /*imgSemestrePath = "/static/bulletin/icones/number_2.png"
        }*/
        var imgSemestre = document.createElement('img')
          imgSemestre.setAttribute('src',imgSemestrePath)
          imgSemestre.setAttribute('alt','One')

        const numeroSemestre = document.createElement('div')
        numeroSemestre.setAttribute("id", "numero-semestre")
        numeroSemestre.appendChild(imgSemestre)

        const codeMatiere = document.createElement('div')
        codeMatiere.setAttribute("id", "code-matiere")
        var codeMatiereValeur = document.createTextNode(filiereSpe1[i])
        codeMatiere.appendChild(codeMatiereValeur)

        const numeroSemestreCodeMatiere = document.createElement("div")
        numeroSemestreCodeMatiere.setAttribute('id', "numero-semestre-code-matiere")
        numeroSemestreCodeMatiere.appendChild(numeroSemestre)
        numeroSemestreCodeMatiere.appendChild(codeMatiere)


        const intituleMatiere = document.createElement('div')
        intituleMatiere.setAttribute('id','intitule-matiere')
        var UeTitle = document.createTextNode(specialite[i])
        intituleMatiere.appendChild(UeTitle)

        //Ajout Bouton Génération Bulletins
        const genererBull = document.createElement("button")
        genererBull.setAttribute("id", `myBtn${i}`)
        genererBull.setAttribute("class", 'myBtn')
        genererBull.innerHTML = "APPERCU BULLETIN(S)";

        const bigBoy = document.createElement('div')
        bigBoy.setAttribute('id', `big-boy`)
        bigBoy.appendChild(genererBull)

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

    //Semestres N0 2 STAPS ET GESTION
    for(let i=0; i<filiereSpe1.length; i++){
        /*if(i==1){
            */imgSemestrePath = "/static/bulletin/icones/number_2.png"
        /*}else if(i==2){
            /*imgSemestrePath = "/static/bulletin/icones/number_2.png"
        }*/
        var imgSemestre = document.createElement('img')
          imgSemestre.setAttribute('src',imgSemestrePath)
          imgSemestre.setAttribute('alt','One')

        const numeroSemestre = document.createElement('div')
        numeroSemestre.setAttribute("id", "numero-semestre")
        numeroSemestre.appendChild(imgSemestre)

        const codeMatiere = document.createElement('div')
        codeMatiere.setAttribute("id", "code-matiere")
        var codeMatiereValeur = document.createTextNode(filiereSpe1[i])
        codeMatiere.appendChild(codeMatiereValeur)

        const numeroSemestreCodeMatiere = document.createElement("div")
        numeroSemestreCodeMatiere.setAttribute('id', "numero-semestre-code-matiere")
        numeroSemestreCodeMatiere.appendChild(numeroSemestre)
        numeroSemestreCodeMatiere.appendChild(codeMatiere)


        const intituleMatiere = document.createElement('div')
        intituleMatiere.setAttribute('id','intitule-matiere')
        var UeTitle = document.createTextNode(specialite[i])
        intituleMatiere.appendChild(UeTitle)

        //Ajout Bouton Génération Bulletins
        const genererBull = document.createElement("button")
        genererBull.setAttribute("id", `myBtn${i+2}`)
        genererBull.setAttribute("class", 'myBtn')
        genererBull.innerHTML = "APPERCU BULLETIN(S)";

        const bigBoy = document.createElement('div')
        bigBoy.setAttribute('id', `big-boy`)
        bigBoy.appendChild(genererBull)

        const addModifyMatiere = document.createElement('div')
        addModifyMatiere.setAttribute("id", "add-modify-matiere")
        addModifyMatiere.appendChild(bigBoy)

        const matiere= document.createElement("div")
        matiere.setAttribute("class", "matiere")
        matiere.setAttribute("id", `matiere${i+2}`)
        matiere.appendChild(numeroSemestreCodeMatiere)
        matiere.appendChild(intituleMatiere)
        matiere.appendChild(addModifyMatiere)

        listUe.appendChild(matiere)
    } 

    /**
     * SEMESTRES 3 & 4
     */
    for(let i=0; i<=2; i++){
        if(i==0){
            imgSemestrePath = "/static/bulletin/icones/number_3.png"
        }else if(i==1){
            imgSemestrePath = "/static/bulletin/icones/four_4.png"
        }if(i==2){break}
        var imgSemestre = document.createElement('img')
          imgSemestre.setAttribute('src',imgSemestrePath)
          imgSemestre.setAttribute('alt','One')

          const numeroSemestre = document.createElement('div')
          numeroSemestre.setAttribute("id", "numero-semestre")
          numeroSemestre.appendChild(imgSemestre)

          const codeMatiere = document.createElement('div')
        codeMatiere.setAttribute("id", "code-matiere")
        var codeMatiereValeur = document.createTextNode(filiereSpe2)
        codeMatiere.appendChild(codeMatiereValeur)

        const numeroSemestreCodeMatiere = document.createElement("div")
        numeroSemestreCodeMatiere.setAttribute('id', "numero-semestre-code-matiere")
        numeroSemestreCodeMatiere.appendChild(numeroSemestre)
        numeroSemestreCodeMatiere.appendChild(codeMatiere)

        const intituleMatiere = document.createElement('div')
        intituleMatiere.setAttribute('id','intitule-matiere')
        var UeTitle = document.createTextNode(specialite2)
        intituleMatiere.appendChild(UeTitle)

        const genererBull = document.createElement('button');
        genererBull.innerHTML="APPERCU BULLETIN(S)";
        genererBull.setAttribute("id", `myBtn${i+4}`)
        genererBull.setAttribute("class", 'myBtn')

        const bigBoy = document.createElement('div')
        bigBoy.setAttribute('id', `big-boy`)
        bigBoy.appendChild(genererBull)

        const addModifyMatiere = document.createElement('div')
        addModifyMatiere.setAttribute("id", "add-modify-matiere")
        addModifyMatiere.appendChild(bigBoy)

        const matiere= document.createElement("div")
        matiere.setAttribute("class", "matiere")
        matiere.setAttribute("id", `matiere${i+4}`)
        matiere.appendChild(numeroSemestreCodeMatiere)
        matiere.appendChild(intituleMatiere)
        matiere.appendChild(addModifyMatiere)

        listUe.appendChild(matiere)
    }

    /**
     * SEMESTRES 5 
     */
    for(let i=0; i<=2; i++){
        if(i==2){break}
        imgSemestrePath = "/static/bulletin/icones/five_5.png"
        var imgSemestre = document.createElement('img')
        imgSemestre.setAttribute('src',imgSemestrePath)
        imgSemestre.setAttribute('alt','One')

        const numeroSemestre = document.createElement('div')
        numeroSemestre.setAttribute("id", "numero-semestre")
        numeroSemestre.appendChild(imgSemestre)

        const codeMatiere = document.createElement('div')
        codeMatiere.setAttribute("id", "code-matiere")
        var codeMatiereValeur = document.createTextNode(filiereSpe3)
        codeMatiere.appendChild(codeMatiereValeur)

        const numeroSemestreCodeMatiere = document.createElement("div")
        numeroSemestreCodeMatiere.setAttribute('id', "numero-semestre-code-matiere")
        numeroSemestreCodeMatiere.appendChild(numeroSemestre)
        numeroSemestreCodeMatiere.appendChild(codeMatiere)

        const intituleMatiere = document.createElement('div')
        intituleMatiere.setAttribute('id','intitule-matiere')
        var UeTitle = document.createTextNode(specialite3[i])
        intituleMatiere.appendChild(UeTitle)

        const genererBull = document.createElement('button');
        genererBull.innerHTML="APPERCU BULLETIN(S)";
        genererBull.setAttribute("id", `myBtn${i+6}`)
        genererBull.setAttribute("class", 'myBtn')

        const bigBoy = document.createElement('div')
        bigBoy.setAttribute('id', `big-boy`)
        bigBoy.appendChild(genererBull)

        const addModifyMatiere = document.createElement('div')
        addModifyMatiere.setAttribute("id", "add-modify-matiere")
        addModifyMatiere.appendChild(bigBoy)

        const matiere= document.createElement("div")
        matiere.setAttribute("class", "matiere")
        matiere.setAttribute("id", `matiere${i+6}`)
        matiere.appendChild(numeroSemestreCodeMatiere)
        matiere.appendChild(intituleMatiere)
        matiere.appendChild(addModifyMatiere)

        listUe.appendChild(matiere)
    }

    /**
     * SEMESTRES 6 
     */
    for(let i=0; i<=2; i++){
        if(i==2){break}
        imgSemestrePath = "/static/bulletin/icones/number_6.png"
        var imgSemestre = document.createElement('img')
        imgSemestre.setAttribute('src',imgSemestrePath)
        imgSemestre.setAttribute('alt','One')

        const numeroSemestre = document.createElement('div')
        numeroSemestre.setAttribute("id", "numero-semestre")
        numeroSemestre.appendChild(imgSemestre)

        const codeMatiere = document.createElement('div')
        codeMatiere.setAttribute("id", "code-matiere")
        var codeMatiereValeur = document.createTextNode(filiereSpe3)
        codeMatiere.appendChild(codeMatiereValeur)

        const numeroSemestreCodeMatiere = document.createElement("div")
        numeroSemestreCodeMatiere.setAttribute('id', "numero-semestre-code-matiere")
        numeroSemestreCodeMatiere.appendChild(numeroSemestre)
        numeroSemestreCodeMatiere.appendChild(codeMatiere)

        const intituleMatiere = document.createElement('div')
        intituleMatiere.setAttribute('id','intitule-matiere')
        var UeTitle = document.createTextNode(specialite3[i])
        intituleMatiere.appendChild(UeTitle)

        const genererBull = document.createElement('button');
        genererBull.innerHTML="APPERCU BULLETIN(S)";
        genererBull.setAttribute("id", `myBtn${i+7}`)
        genererBull.setAttribute("class", 'myBtn')

        const bigBoy = document.createElement('div')
        bigBoy.setAttribute('id', `big-boy`)
        bigBoy.appendChild(genererBull)

        const addModifyMatiere = document.createElement('div')
        addModifyMatiere.setAttribute("id", "add-modify-matiere")
        addModifyMatiere.appendChild(bigBoy)

        const matiere= document.createElement("div")
        matiere.setAttribute("class", "matiere")
        matiere.setAttribute("id", `matiere${i+8}`)
        matiere.appendChild(numeroSemestreCodeMatiere)
        matiere.appendChild(intituleMatiere)
        matiere.appendChild(addModifyMatiere)

        listUe.appendChild(matiere)
    }

    /**POSITION DE LA FONCTION MODAL */
    modal()
}

createSemestre()

/**
 * REQUETES
 */
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
  
       listeTitle.innerText=`LISTE DES ETUDIANTS INSCRITS EN --${idUe}-- ANNEE 202X-202X`
  
        for(let i=0; i<myEtudiantStaps1.length; i++){

          const tabledata2 = document.createElement('td')
          tabledata2.innerText = myEtudiantStaps1[i].matricule
          tabledata2.setAttribute('class', 'columnL')
  
          var nom = myEtudiantStaps1[i].nom +' '+myEtudiantStaps1[i].prenom
          const tabledata3 = document.createElement('td')
          tabledata3.innerText = nom
  
          const tabledata4Input = document.createElement('button')
          tabledata4Input.setAttribute('name',`${myEtudiantStaps1[i].matricule}`)
          tabledata4Input.setAttribute('id',`${myEtudiantStaps1[i].matricule}`)
          tabledata4Input.innerText = `GENERER BULLETIN ${myEtudiantStaps1[i].nom}`
  
          const tabledata4 = document.createElement('td')
          tabledata4.appendChild(tabledata4Input)
          tabledata4.setAttribute('class','columnR')
          tabledata4.disabled = true
  
          const ligne = document.createElement('tr')
          ligne.appendChild(tabledata2);
          ligne.appendChild(tabledata3);
          ligne.appendChild(tabledata4);

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
       listeTitle.innerText=`LISTE DES ETUDIANTS INSCRITS EN --${idUe}-- ANNEE 202X-202X`
  
        for(let i=0; i<myEtudiantMDS1.length; i++){

          const tabledata2 = document.createElement('td')
          tabledata2.innerText = myEtudiantMDS1[i].matricule
          tabledata2.setAttribute('class', 'columnL')
  
          var nom = myEtudiantMDS1[i].nom +' '+myEtudiantMDS1[i].prenom
          const tabledata3 = document.createElement('td')
          tabledata3.innerText = nom
  
          const tabledata4Input = document.createElement('button')
          tabledata4Input.setAttribute('name',`${myEtudiantMDS1[i].matricule}`)
          tabledata4Input.setAttribute('id',`${myEtudiantMDS1[i].matricule}`)
          tabledata4Input.innerText = `GENERER BULLETIN ${myEtudiantMDS1[i].nom}`
  
          const tabledata4 = document.createElement('td')
          tabledata4.appendChild(tabledata4Input)
          tabledata4.setAttribute('class','columnR')
          tabledata4.disabled = true
  
          const ligne = document.createElement('tr')
          ligne.appendChild(tabledata2);
          ligne.appendChild(tabledata3);
          ligne.appendChild(tabledata4);

          /** TBODDY du modal afin d'ajouter les étudiants par filière */
          const listStudent = document.getElementById('listetudiant')
          listStudent.appendChild(ligne)
       }
      }
    };
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
  
       listeTitle = document.getElementById('listetudiant-title')
  
       listeTitle.innerText=`LISTE DES ETUDIANTS INSCRITS EN --${idUe}-- ANNEE 202X-202X`
  
        for(let i=0; i<myEtudiantStaps2.length; i++){

          const tabledata2 = document.createElement('td')
          tabledata2.innerText = myEtudiantStaps2[i].matricule
          tabledata2.setAttribute('class', 'columnL')
  
          var nom = myEtudiantStaps2[i].nom +' '+myEtudiantStaps2[i].prenom
          const tabledata3 = document.createElement('td')
          tabledata3.innerText = nom
  
          const tabledata4Input = document.createElement('button')
          tabledata4Input.setAttribute('name',`${myEtudiantStaps2[i].matricule}`)
          tabledata4Input.setAttribute('id',`${myEtudiantStaps2[i].matricule}`)
          tabledata4Input.innerText = `GENERER BULLETIN ${myEtudiantStaps2[i].nom}`
  
          const tabledata4 = document.createElement('td')
          tabledata4.appendChild(tabledata4Input)
          tabledata4.setAttribute('class','columnR')
          tabledata4.disabled = true
  
          const ligne = document.createElement('tr')
          ligne.appendChild(tabledata2);
          ligne.appendChild(tabledata3);
          ligne.appendChild(tabledata4);

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
  
       listeTitle.innerText=`LISTE DES ETUDIANTS INSCRITS EN --${idUe}-- ANNEE 202X-202X`
  
        for(let i=0; i<myEtudiantNiveau3EVE.length; i++){

          const tabledata2 = document.createElement('td')
          tabledata2.innerText = myEtudiantNiveau3EVE[i].matricule
          tabledata2.setAttribute('class', 'columnL')
  
          var nom = myEtudiantNiveau3EVE[i].nom +' '+myEtudiantNiveau3EVE[i].prenom
          const tabledata3 = document.createElement('td')
          tabledata3.innerText = nom
  
          const tabledata4Input = document.createElement('button')
          tabledata4Input.setAttribute('name',`${myEtudiantNiveau3EVE[i].matricule}`)
          tabledata4Input.setAttribute('id',`${myEtudiantNiveau3EVE[i].matricule}`)
          tabledata4Input.innerText = `GENERER BULLETIN ${myEtudiantNiveau3EVE[i].nom}`
  
          const tabledata4 = document.createElement('td')
          tabledata4.appendChild(tabledata4Input)
          tabledata4.setAttribute('class','columnR')
          tabledata4.disabled = true
  
          const ligne = document.createElement('tr')
          ligne.appendChild(tabledata2);
          ligne.appendChild(tabledata3);
          ligne.appendChild(tabledata4);

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
  
       listeTitle.innerText=`LISTE DES ETUDIANTS INSCRITS EN --${idUe}-- ANNEE 202X-202X`
  
        for(let i=0; i<myEtudiantNiveau3MSO.length; i++){

          const tabledata2 = document.createElement('td')
          tabledata2.innerText = myEtudiantNiveau3MSO[i].matricule
          tabledata2.setAttribute('class', 'columnL')
  
          var nom = myEtudiantNiveau3MSO[i].nom +' '+myEtudiantNiveau3MSO[i].prenom
          const tabledata3 = document.createElement('td')
          tabledata3.innerText = nom
  
          const tabledata4Input = document.createElement('button')
          tabledata4Input.setAttribute('name',`${myEtudiantNiveau3MSO[i].matricule}`)
          tabledata4Input.setAttribute('id',`${myEtudiantNiveau3MSO[i].matricule}`)
          tabledata4Input.innerText = `GENERER BULLETIN ${myEtudiantNiveau3MSO[i].nom}`
  
          const tabledata4 = document.createElement('td')
          tabledata4.appendChild(tabledata4Input)
          tabledata4.setAttribute('class','columnR')
          tabledata4.disabled = true
  
          const ligne = document.createElement('tr')
          ligne.appendChild(tabledata2);
          ligne.appendChild(tabledata3);
          ligne.appendChild(tabledata4);

          /** TBODDY du modal afin d'ajouter les étudiants par filière */
          const listStudent = document.getElementById('listetudiant')
          listStudent.appendChild(ligne)
       }
       
      }
  };
  xmlhttp.open("GET", url, true);
  xmlhttp.send(); 
  }