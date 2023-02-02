"use strict";

/** GET THE ID OF Buttons */
function getButtonId() {
  // Create event listener
  document.addEventListener('click', function (e) {
    // Retrieve id from clicked element
    if (e.target.id !== '' && (e.target.tagName == 'A' || e.target.tagName == 'BUTTON')
    /*e.target.tagName == 'BUTTON'*/
    ) {
        //idUe = ""
        //console.log(e.target.parentElement.parentElement.parentElement.parentElement.children[0].innerText);
        idUe = e.target.parentElement.parentElement.parentElement.children[0].innerText; //.parentElement.children[0].innerText

        console.log(idUe);
        return idUe;
      } else {
      // If element has no id
      console.log("object is neither button, nor anchor doesn't have ID");
    }
  }); //document.getElementsByTagName('')
}

getButtonId();
/********************************** MODAL *************************************************/

function modal() {
  tbodylistStudent = document.getElementById('listetudiant'); // Get the modal For the add 

  modal = document.getElementById("myModal"); // Get the buttons that open the modal

  var btn = document.getElementsByClassName("myBtn");
  /**BOUTON DE FERMETURE NOTES */
  // GET the button that closes the modal

  spanClose = document.getElementsByClassName("close")[0]; //When the user clicks on span (x), close the modal

  spanClose.onclick = function () {
    /**VIDAGE DU CONTENEUR DE LISTE DES ETUDIANTS */
    //console.log(tbodylistStudent);
    tbodylistStudent.innerHTML = "";
    modal.style.display = "none";
  };
  /**ITERATION AFIN D'OBTENIR LES LISTES DES ETUDIANTS INSCRITS DANS LES MATIERES */


  var _loop = function _loop(i) {
    btn[i].onclick = function () {
      bouton = btn[i].parentElement.parentElement.parentElement.children[0].innerText;

      if (btn[i].parentElement.parentElement.parentElement.children[0].innerText == "STAPS1") {
        getetudiantStapsNiveau1();
      } else if (btn[i].parentElement.parentElement.parentElement.children[0].innerText == "GESTION") {
        getetudiantMDSNiveau1(); //SendSetSpecialityMatricule(bouton)//
      } else if (btn[i].parentElement.parentElement.parentElement.children[0].innerText == "STAPS2") {
        getetudiantStapsNiveau2();
      } else if (btn[i].parentElement.parentElement.parentElement.children[1].innerText == "MANAGEMENT STRATEGIQUE DES EVENEMENTS SPORTIFS") {
        getetudiantMSONiveau3();
      } else if (btn[i].parentElement.parentElement.parentElement.children[1].innerText == "EVENEMENTIEL") {
        getetudiantEVENiveau3();
      }

      modal.style.display = "block";
    };
  };

  for (var i = 0; i < btn.length; i++) {
    _loop(i);
  }
}
/**
 * FONCTION CHARGEE DE LA CREATION DES SEMESTRES-SPECIALITES 
 */


function createSemestre() {
  filiereSpe1 = ["GESTION", "STAPS1"];
  specialite = ["MANAGEMENT DU SPORT", "EDUCATION PHYSIQUE ET SPORTIVE"];
  filiereSpe2 = "STAPS2";
  specialite2 = "EDUCATION PHYSIQUE ET SPORTIVE";
  filiereSpe3 = "LP3MOIS";
  specialite3 = ["EVENEMENTIEL", "MANAGEMENT STRATEGIQUE DES EVENEMENTS SPORTIFS"];
  var listUe = document.getElementById("list-ue"); //Semestre N01 STAPS ET GESTION

  for (var i = 0; i < filiereSpe1.length; i++) {
    /*if(i==1){
        */
    imgSemestrePath = "/static/bulletin/icones/number_1.png";
    /*}else if(i==2){
        /*imgSemestrePath = "/static/bulletin/icones/number_2.png"
    }*/

    var imgSemestre = document.createElement('img');
    imgSemestre.setAttribute('src', imgSemestrePath);
    imgSemestre.setAttribute('alt', 'One');
    var numeroSemestre = document.createElement('div');
    numeroSemestre.setAttribute("id", "numero-semestre");
    numeroSemestre.appendChild(imgSemestre);
    var codeMatiere = document.createElement('div');
    codeMatiere.setAttribute("id", "code-matiere");
    var codeMatiereValeur = document.createTextNode(filiereSpe1[i]);
    codeMatiere.appendChild(codeMatiereValeur);
    var numeroSemestreCodeMatiere = document.createElement("div");
    numeroSemestreCodeMatiere.setAttribute('id', "numero-semestre-code-matiere");
    numeroSemestreCodeMatiere.appendChild(numeroSemestre);
    numeroSemestreCodeMatiere.appendChild(codeMatiere);
    var intituleMatiere = document.createElement('div');
    intituleMatiere.setAttribute('id', 'intitule-matiere');
    var UeTitle = document.createTextNode(specialite[i]);
    intituleMatiere.appendChild(UeTitle); //Ajout Bouton Génération Bulletins

    var genererBull = document.createElement("a"); //console.log(bouton);

    genererBull.setAttribute("id", "generateLink".concat(i));
    /*filiere = getButtonId()
    console.log(`${filiere} OK`);*/
    //genererBull.setAttribute("href", "BullS1EPS")

    /*genererBull.setAttribute("class","btn-primary")*/

    /*genererBull.setAttribute("id", `myBtn${i}`)
    genererBull.setAttribute("class", 'myBtn')*/

    genererBull.innerHTML = "APPERCU BULLETIN(S)";
    var bigBoy = document.createElement('div');
    bigBoy.setAttribute('id', "big-boy");
    bigBoy.appendChild(genererBull);
    var addModifyMatiere = document.createElement('div');
    addModifyMatiere.setAttribute("id", "add-modify-matiere");
    addModifyMatiere.appendChild(bigBoy);
    var matiere = document.createElement("div");
    matiere.setAttribute("class", "matiere");
    matiere.setAttribute("id", "matiere".concat(i));
    matiere.appendChild(numeroSemestreCodeMatiere);
    matiere.appendChild(intituleMatiere);
    matiere.appendChild(addModifyMatiere);
    listUe.appendChild(matiere);
    genererBull.setAttribute("href", "BullS1EPS/".concat(genererBull.parentElement.parentElement.parentElement.children[0].innerText));
  } //Semestres N0 2 STAPS ET GESTION


  for (var _i = 0; _i < filiereSpe1.length; _i++) {
    /*if(i==1){
        */
    imgSemestrePath = "/static/bulletin/icones/number_2.png";
    /*}else if(i==2){
        /*imgSemestrePath = "/static/bulletin/icones/number_2.png"
    }*/

    var imgSemestre = document.createElement('img');
    imgSemestre.setAttribute('src', imgSemestrePath);
    imgSemestre.setAttribute('alt', 'One');

    var _numeroSemestre = document.createElement('div');

    _numeroSemestre.setAttribute("id", "numero-semestre");

    _numeroSemestre.appendChild(imgSemestre);

    var _codeMatiere = document.createElement('div');

    _codeMatiere.setAttribute("id", "code-matiere");

    var codeMatiereValeur = document.createTextNode(filiereSpe1[_i]);

    _codeMatiere.appendChild(codeMatiereValeur);

    var _numeroSemestreCodeMatiere = document.createElement("div");

    _numeroSemestreCodeMatiere.setAttribute('id', "numero-semestre-code-matiere");

    _numeroSemestreCodeMatiere.appendChild(_numeroSemestre);

    _numeroSemestreCodeMatiere.appendChild(_codeMatiere);

    var _intituleMatiere = document.createElement('div');

    _intituleMatiere.setAttribute('id', 'intitule-matiere');

    var UeTitle = document.createTextNode(specialite[_i]);

    _intituleMatiere.appendChild(UeTitle); //Ajout Bouton Génération Bulletins


    var _genererBull = document.createElement("button");

    _genererBull.setAttribute("id", "myBtn".concat(_i + 2));

    _genererBull.setAttribute("class", 'myBtn');

    _genererBull.innerHTML = "APPERCU BULLETIN(S)";

    var _bigBoy = document.createElement('div');

    _bigBoy.setAttribute('id', "big-boy");

    _bigBoy.appendChild(_genererBull);

    var _addModifyMatiere = document.createElement('div');

    _addModifyMatiere.setAttribute("id", "add-modify-matiere");

    _addModifyMatiere.appendChild(_bigBoy);

    var _matiere = document.createElement("div");

    _matiere.setAttribute("class", "matiere");

    _matiere.setAttribute("id", "matiere".concat(_i + 2));

    _matiere.appendChild(_numeroSemestreCodeMatiere);

    _matiere.appendChild(_intituleMatiere);

    _matiere.appendChild(_addModifyMatiere);

    listUe.appendChild(_matiere);
  }
  /**
   * SEMESTRES 3 & 4
   */


  for (var _i2 = 0; _i2 <= 2; _i2++) {
    if (_i2 == 0) {
      imgSemestrePath = "/static/bulletin/icones/number_3.png";
    } else if (_i2 == 1) {
      imgSemestrePath = "/static/bulletin/icones/four_4.png";
    }

    if (_i2 == 2) {
      break;
    }

    var imgSemestre = document.createElement('img');
    imgSemestre.setAttribute('src', imgSemestrePath);
    imgSemestre.setAttribute('alt', 'One');

    var _numeroSemestre2 = document.createElement('div');

    _numeroSemestre2.setAttribute("id", "numero-semestre");

    _numeroSemestre2.appendChild(imgSemestre);

    var _codeMatiere2 = document.createElement('div');

    _codeMatiere2.setAttribute("id", "code-matiere");

    var codeMatiereValeur = document.createTextNode(filiereSpe2);

    _codeMatiere2.appendChild(codeMatiereValeur);

    var _numeroSemestreCodeMatiere2 = document.createElement("div");

    _numeroSemestreCodeMatiere2.setAttribute('id', "numero-semestre-code-matiere");

    _numeroSemestreCodeMatiere2.appendChild(_numeroSemestre2);

    _numeroSemestreCodeMatiere2.appendChild(_codeMatiere2);

    var _intituleMatiere2 = document.createElement('div');

    _intituleMatiere2.setAttribute('id', 'intitule-matiere');

    var UeTitle = document.createTextNode(specialite2);

    _intituleMatiere2.appendChild(UeTitle);

    var _genererBull2 = document.createElement('button');

    _genererBull2.innerHTML = "APPERCU BULLETIN(S)";

    _genererBull2.setAttribute("id", "myBtn".concat(_i2 + 4));

    _genererBull2.setAttribute("class", 'myBtn');

    var _bigBoy2 = document.createElement('div');

    _bigBoy2.setAttribute('id', "big-boy");

    _bigBoy2.appendChild(_genererBull2);

    var _addModifyMatiere2 = document.createElement('div');

    _addModifyMatiere2.setAttribute("id", "add-modify-matiere");

    _addModifyMatiere2.appendChild(_bigBoy2);

    var _matiere2 = document.createElement("div");

    _matiere2.setAttribute("class", "matiere");

    _matiere2.setAttribute("id", "matiere".concat(_i2 + 4));

    _matiere2.appendChild(_numeroSemestreCodeMatiere2);

    _matiere2.appendChild(_intituleMatiere2);

    _matiere2.appendChild(_addModifyMatiere2);

    listUe.appendChild(_matiere2);
  }
  /**
   * SEMESTRES 5 
   */


  for (var _i3 = 0; _i3 <= 2; _i3++) {
    if (_i3 == 2) {
      break;
    }

    imgSemestrePath = "/static/bulletin/icones/five_5.png";
    var imgSemestre = document.createElement('img');
    imgSemestre.setAttribute('src', imgSemestrePath);
    imgSemestre.setAttribute('alt', 'One');

    var _numeroSemestre3 = document.createElement('div');

    _numeroSemestre3.setAttribute("id", "numero-semestre");

    _numeroSemestre3.appendChild(imgSemestre);

    var _codeMatiere3 = document.createElement('div');

    _codeMatiere3.setAttribute("id", "code-matiere");

    var codeMatiereValeur = document.createTextNode(filiereSpe3);

    _codeMatiere3.appendChild(codeMatiereValeur);

    var _numeroSemestreCodeMatiere3 = document.createElement("div");

    _numeroSemestreCodeMatiere3.setAttribute('id', "numero-semestre-code-matiere");

    _numeroSemestreCodeMatiere3.appendChild(_numeroSemestre3);

    _numeroSemestreCodeMatiere3.appendChild(_codeMatiere3);

    var _intituleMatiere3 = document.createElement('div');

    _intituleMatiere3.setAttribute('id', 'intitule-matiere');

    var UeTitle = document.createTextNode(specialite3[_i3]);

    _intituleMatiere3.appendChild(UeTitle);

    var _genererBull3 = document.createElement('button');

    _genererBull3.innerHTML = "APPERCU BULLETIN(S)";

    _genererBull3.setAttribute("id", "myBtn".concat(_i3 + 6));

    _genererBull3.setAttribute("class", 'myBtn');

    var _bigBoy3 = document.createElement('div');

    _bigBoy3.setAttribute('id', "big-boy");

    _bigBoy3.appendChild(_genererBull3);

    var _addModifyMatiere3 = document.createElement('div');

    _addModifyMatiere3.setAttribute("id", "add-modify-matiere");

    _addModifyMatiere3.appendChild(_bigBoy3);

    var _matiere3 = document.createElement("div");

    _matiere3.setAttribute("class", "matiere");

    _matiere3.setAttribute("id", "matiere".concat(_i3 + 6));

    _matiere3.appendChild(_numeroSemestreCodeMatiere3);

    _matiere3.appendChild(_intituleMatiere3);

    _matiere3.appendChild(_addModifyMatiere3);

    listUe.appendChild(_matiere3);
  }
  /**
   * SEMESTRES 6 
   */


  for (var _i4 = 0; _i4 <= 2; _i4++) {
    if (_i4 == 2) {
      break;
    }

    imgSemestrePath = "/static/bulletin/icones/number_6.png";
    var imgSemestre = document.createElement('img');
    imgSemestre.setAttribute('src', imgSemestrePath);
    imgSemestre.setAttribute('alt', 'One');

    var _numeroSemestre4 = document.createElement('div');

    _numeroSemestre4.setAttribute("id", "numero-semestre");

    _numeroSemestre4.appendChild(imgSemestre);

    var _codeMatiere4 = document.createElement('div');

    _codeMatiere4.setAttribute("id", "code-matiere");

    var codeMatiereValeur = document.createTextNode(filiereSpe3);

    _codeMatiere4.appendChild(codeMatiereValeur);

    var _numeroSemestreCodeMatiere4 = document.createElement("div");

    _numeroSemestreCodeMatiere4.setAttribute('id', "numero-semestre-code-matiere");

    _numeroSemestreCodeMatiere4.appendChild(_numeroSemestre4);

    _numeroSemestreCodeMatiere4.appendChild(_codeMatiere4);

    var _intituleMatiere4 = document.createElement('div');

    _intituleMatiere4.setAttribute('id', 'intitule-matiere');

    var UeTitle = document.createTextNode(specialite3[_i4]);

    _intituleMatiere4.appendChild(UeTitle);

    var _genererBull4 = document.createElement('button');

    _genererBull4.innerHTML = "APPERCU BULLETIN(S)";

    _genererBull4.setAttribute("id", "myBtn".concat(_i4 + 7));

    _genererBull4.setAttribute("class", 'myBtn');

    var _bigBoy4 = document.createElement('div');

    _bigBoy4.setAttribute('id', "big-boy");

    _bigBoy4.appendChild(_genererBull4);

    var _addModifyMatiere4 = document.createElement('div');

    _addModifyMatiere4.setAttribute("id", "add-modify-matiere");

    _addModifyMatiere4.appendChild(_bigBoy4);

    var _matiere4 = document.createElement("div");

    _matiere4.setAttribute("class", "matiere");

    _matiere4.setAttribute("id", "matiere".concat(_i4 + 8));

    _matiere4.appendChild(_numeroSemestreCodeMatiere4);

    _matiere4.appendChild(_intituleMatiere4);

    _matiere4.appendChild(_addModifyMatiere4);

    listUe.appendChild(_matiere4);
  }
  /**POSITION DE LA FONCTION MODAL */


  modal();
}

createSemestre();
/**
 * REQUETES
 */

/** REQUEST ETUDIANTS STAPTS NIVEAU 1 */

function getetudiantStapsNiveau1() {
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantStaps1/";

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      myEtudiantStaps1 = JSON.parse(this.responseText);
      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */

      listeTitle = document.getElementById('listetudiant-title');
      listeTitle.innerText = "LISTE DES ETUDIANTS INSCRITS EN --".concat(idUe, "-- ANNEE 202X-202X");
      dataList = {};

      var _loop2 = function _loop2(i) {
        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantStaps1[i].matricule;
        tabledata2.setAttribute('class', 'columnL');
        nom = myEtudiantStaps1[i].nom + ' ' + myEtudiantStaps1[i].prenom;
        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('button');
        tabledata4Input.setAttribute('name', "".concat(myEtudiantStaps1[i].matricule));
        tabledata4Input.setAttribute('id', "".concat(myEtudiantStaps1[i].matricule));
        tabledata4Input.innerText = "GENERER BULLETIN ".concat(myEtudiantStaps1[i].nom);

        tabledata4Input.onclick = function () {
          GetUniqueMatricule({
            nom: myEtudiantStaps1[i].nom,
            matricule: myEtudiantStaps1[i].matricule
          });
        };

        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        tabledata4.setAttribute('class', 'columnR');
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4);
        /** TBODDY du modal afin d'ajouter les étudiants par filière */

        var listStudent = document.getElementById('listetudiant');
        listStudent.appendChild(ligne);
        dataList[i] = {
          /*nom:myEtudiantStaps1[i].nom ,*/
          nom: myEtudiantStaps1[i].matricule
        };
      };

      for (var i = 0; i < myEtudiantStaps1.length; i++) {
        var nom;

        _loop2(i);
      }

      dataToSend = dataList;
      var submitBullSpecialite = document.getElementById('submit');

      submitBullSpecialite.onclick = function () {
        GetSetSpecialityMatricule(dataToSend);
      };
    }
  };

  xmlhttp.open("GET", url, true);
  xmlhttp.send();
}
/** REQUEST ETUDIANTS MDS NIVEAU 1 */


function getetudiantMDSNiveau1() {
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantMDS1/";

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      myEtudiantMDS1 = JSON.parse(this.responseText);
      console.log(myEtudiantMDS1);
      SendSetSpecialityMatricule(myEtudiantMDS1);
      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */

      listeTitle = document.getElementById('listetudiant-title');
      listeTitle.innerText = "LISTE DES ETUDIANTS INSCRITS EN --".concat(idUe, "-- ANNEE 202X-202X");

      var _loop3 = function _loop3(i) {
        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantMDS1[i].matricule;
        tabledata2.setAttribute('class', 'columnL');
        nom = myEtudiantMDS1[i].nom + ' ' + myEtudiantMDS1[i].prenom;
        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('button');
        tabledata4Input.setAttribute('name', "".concat(myEtudiantMDS1[i].matricule));
        tabledata4Input.setAttribute('id', "".concat(myEtudiantMDS1[i].matricule));
        tabledata4Input.innerText = "GENERER BULLETIN ".concat(myEtudiantMDS1[i].nom);

        tabledata4Input.onclick = function () {
          GetUniqueMatricule({
            nom: myEtudiantMDS1[i].nom,
            matricule: myEtudiantMDS1[i].matricule
          });
        };

        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        tabledata4.setAttribute('class', 'columnR');
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4);
        /** TBODDY du modal afin d'ajouter les étudiants par filière */

        var listStudent = document.getElementById('listetudiant');
        listStudent.appendChild(ligne);
      };

      for (var i = 0; i < myEtudiantMDS1.length; i++) {
        var nom;

        _loop3(i);
      }
    }
  };

  xmlhttp.open("GET", url, true);
  xmlhttp.send();
}
/**  REQUEST ETUDIANT STAPS NIVEAU 2 */


function getetudiantStapsNiveau2() {
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantStaps2/";

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      myEtudiantStaps2 = JSON.parse(this.responseText);
      listeTitle = document.getElementById('listetudiant-title');
      listeTitle.innerText = "LISTE DES ETUDIANTS INSCRITS EN --".concat(idUe, "-- ANNEE 202X-202X");

      var _loop4 = function _loop4(i) {
        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantStaps2[i].matricule;
        tabledata2.setAttribute('class', 'columnL');
        nom = myEtudiantStaps2[i].nom + ' ' + myEtudiantStaps2[i].prenom;
        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('button');
        tabledata4Input.setAttribute('name', "".concat(myEtudiantStaps2[i].matricule));
        tabledata4Input.setAttribute('id', "".concat(myEtudiantStaps2[i].matricule));
        tabledata4Input.innerText = "GENERER BULLETIN ".concat(myEtudiantStaps2[i].nom);

        tabledata4Input.onclick = function () {
          GetUniqueMatricule({
            nom: myEtudiantStaps2[i].nom,
            matricule: myEtudiantStaps2[i].matricule
          });
        };

        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        tabledata4.setAttribute('class', 'columnR');
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4);
        /** TBODDY du modal afin d'ajouter les étudiants par filière */

        var listStudent = document.getElementById('listetudiant');
        listStudent.appendChild(ligne);
      };

      for (var i = 0; i < myEtudiantStaps2.length; i++) {
        var nom;

        _loop4(i);
      }
    }
  };

  xmlhttp.open("GET", url, true);
  xmlhttp.send();
}
/** REQUEST ETUDIANTS EVE */


function getetudiantEVENiveau3() {
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantNiveau3EVE/";

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      myEtudiantNiveau3EVE = JSON.parse(this.responseText);
      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */

      listeTitle = document.getElementById('listetudiant-title');
      listeTitle.innerText = "LISTE DES ETUDIANTS INSCRITS EN --".concat(idUe, "-- ANNEE 202X-202X");

      var _loop5 = function _loop5(i) {
        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantNiveau3EVE[i].matricule;
        tabledata2.setAttribute('class', 'columnL');
        nom = myEtudiantNiveau3EVE[i].nom + ' ' + myEtudiantNiveau3EVE[i].prenom;
        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('button');
        tabledata4Input.setAttribute('name', "".concat(myEtudiantNiveau3EVE[i].matricule));
        tabledata4Input.setAttribute('id', "".concat(myEtudiantNiveau3EVE[i].matricule));
        tabledata4Input.innerText = "GENERER BULLETIN ".concat(myEtudiantNiveau3EVE[i].nom);

        tabledata4Input.onclick = function () {
          GetUniqueMatricule({
            nom: myEtudiantNiveau3EVE[i].nom,
            matricule: myEtudiantNiveau3EVE[i].matricule
          });
        };

        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        tabledata4.setAttribute('class', 'columnR');
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4);
        /** TBODDY du modal afin d'ajouter les étudiants par filière */

        var listStudent = document.getElementById('listetudiant');
        listStudent.appendChild(ligne);
      };

      for (var i = 0; i < myEtudiantNiveau3EVE.length; i++) {
        var nom;

        _loop5(i);
      }
    }
  };

  xmlhttp.open("GET", url, true);
  xmlhttp.send();
}
/** REQUEST ETUDIANTS MSO */


function getetudiantMSONiveau3() {
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantNiveau3MSO/";

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      myEtudiantNiveau3MSO = JSON.parse(this.responseText);
      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */

      listeTitle = document.getElementById('listetudiant-title');
      listeTitle.innerText = "LISTE DES ETUDIANTS INSCRITS EN --".concat(idUe, "-- ANNEE 202X-202X");

      var _loop6 = function _loop6(i) {
        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantNiveau3MSO[i].matricule;
        tabledata2.setAttribute('class', 'columnL');
        nom = myEtudiantNiveau3MSO[i].nom + ' ' + myEtudiantNiveau3MSO[i].prenom;
        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('button');
        tabledata4Input.setAttribute('name', "".concat(myEtudiantNiveau3MSO[i].matricule));
        tabledata4Input.setAttribute('id', "".concat(myEtudiantNiveau3MSO[i].matricule));
        tabledata4Input.innerText = "GENERER BULLETIN ".concat(myEtudiantNiveau3MSO[i].nom);

        tabledata4Input.onclick = function () {
          GetUniqueMatricule({
            nom: myEtudiantNiveau3MSO[i].nom,
            matricule: myEtudiantNiveau3MSO[i].matricule
          });
        };

        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        tabledata4.setAttribute('class', 'columnR'); //tabledata4.disabled = true

        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4);
        /** TBODDY du modal afin d'ajouter les étudiants par filière */

        var listStudent = document.getElementById('listetudiant');
        listStudent.appendChild(ligne);
      };

      for (var i = 0; i < myEtudiantNiveau3MSO.length; i++) {
        var nom;

        _loop6(i);
      }
    }
  };

  xmlhttp.open("GET", url, true);
  xmlhttp.send();
}
/**
  * REQUETES BULLETINS
*/


function GetUniqueMatricule(data) {
  $.ajax({
    type: 'GET',
    url: "http://localhost:8000/BulletinUnique/",
    data: data,
    success: console.log("Request sent with Success") //dataType:,

  }); //Ajout d'une ligne pour fermer le modal après soumission de la requête
}

function GetSetSpecialityMatricule(data) {
  $.ajax({
    type: 'POST',
    url: "http://localhost:8000/BulletinSpecialite/",
    data: data,
    success: console.log("Request sent with Success") //dataType:,

  }); //Ajout d'une ligne pour fermer le modal après soumission de la requête
}

function SendSetSpecialityMatricule(donnee) {
  $.ajax({
    type: 'GET',
    url: "BullS1EPS/",
    data: donnee,
    success: console.log("Request sent with Success") //dataType:,

  }); //Ajout d'une ligne pour fermer le modal après soumission de la requête
}