"use strict";

title = document.getElementById('listetudiant-title');
console.log(title);
/** GET THE ID OF Buttons */

function getButtonId() {
  // Create event listener
  document.addEventListener('click', function (e) {
    // Retrieve id from clicked element
    if (e.target.id !== '' && e.target.tagName == 'BUTTON') {
      //console.log(e.target.parentElement.parentElement.parentElement.parentElement.children[0].innerText);
      idUe = e.target.parentElement.parentElement.parentElement.parentElement.children[0].innerText; //
    } else {
      // If element has no id
      console.log("object doesn't have ID");
      console.log(idUe);
    }
  });
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
  /**After Submit */


  var formCloseReset = document.getElementById('submit');
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

  var _loop = function _loop(i) {
    btn[i].onclick = function () {
      if (myArr[i].code_UE.startsWith("EPS 1")) {
        getetudiantStapsNiveau1();
      } else if (myArr[i].code_UE.startsWith("MDS 1")) {
        getetudiantMDSNiveau1();
      } else if (myArr[i].code_UE.startsWith("EPS 2")) {
        getetudiantStapsNiveau2();
      } else if (myArr[i].code_UE.startsWith("MAS ")) {
        getAllEtudiantNiveau3();
      } else if (myArr[i].code_UE.startsWith("EVE")) {
        getetudiantEVENiveau3();
      } else if (myArr[i].code_UE.startsWith("MSO")) {
        getetudiantMSONiveau3();
      }

      modal.style.display = "block";
    };
  };

  for (var i = 0; i < btn.length; i++) {
    _loop(i);
  }
}
/******************************** REQUEST *************************************************************/


function getUe() {
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/UeAPI/";

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      myArr = JSON.parse(this.responseText);
      var listUe = document.getElementById("list-ue");

      for (var i = 0; i < myArr.length; i++) {
        if (myArr[i].semestre_id == 1) {
          imgSemestrePath = "/static/bulletin/icones/number_1.png";
        } else if (myArr[i].semestre_id == 2) {
          imgSemestrePath = "/static/bulletin/icones/number_2.png";
        } else if (myArr[i].semestre_id == 3) {
          imgSemestrePath = "/static/bulletin/icones/number_3.png";
        }

        var imgSemestre = document.createElement('img');
        imgSemestre.setAttribute('src', imgSemestrePath);
        imgSemestre.setAttribute('alt', 'One');
        var numeroSemestre = document.createElement('div');
        numeroSemestre.setAttribute("id", "numero-semestre");
        numeroSemestre.appendChild(imgSemestre);
        var codeMatiere = document.createElement('div');
        codeMatiere.setAttribute("id", "code-matiere");
        var codeMatiereValeur = document.createTextNode(myArr[i].code_UE);
        codeMatiere.appendChild(codeMatiereValeur);
        var numeroSemestreCodeMatiere = document.createElement("div");
        numeroSemestreCodeMatiere.setAttribute('id', "numero-semestre-code-matiere");
        numeroSemestreCodeMatiere.appendChild(numeroSemestre);
        numeroSemestreCodeMatiere.appendChild(codeMatiere);
        /** MILIEU CARD */

        var intituleMatiere = document.createElement('div');
        intituleMatiere.setAttribute('id', 'intitule-matiere');
        var UeTitle = document.createTextNode(myArr[i].intitule_UE);
        intituleMatiere.appendChild(UeTitle);
        /** FIN CARD */

        /*const imgbtn = document.createElement('img')
        let addPathImg = "/static/bulletin/icones/add.png"
        imgbtn.setAttribute("src", addPathImg)*/

        var myBtn = document.createElement('button');
        myBtn.setAttribute('id', "myBtn".concat(i));
        myBtn.setAttribute('class', 'myBtn');
        var imgbtn1 = document.createElement('img');
        var addPathImg1 = "/static/bulletin/icones/edit.png";
        imgbtn1.setAttribute("src", addPathImg1);
        var myBtn1 = document.createElement('button');
        myBtn1.setAttribute('id', "myBtn");
        myBtn1.setAttribute('class', 'myBtn-1');
        myBtn1.appendChild(imgbtn1);
        var add = document.createElement('div');
        add.setAttribute("id", "add");
        add.appendChild(myBtn);
        var modify = document.createElement('div');
        modify.setAttribute("id", "modify");
        modify.appendChild(myBtn1);
        var bigBoy = document.createElement('div');
        bigBoy.setAttribute('id', "big-boy");
        bigBoy.appendChild(add);
        bigBoy.appendChild(modify);
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
      }

      modal();
    }
  };

  xmlhttp.open("GET", url, true);
  xmlhttp.send();
}

getUe();
/** REQUEST ETUDIANTS STAPTS NIVEAU 1 */

function getetudiantStapsNiveau1() {
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantStaps1/";

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      myEtudiantStaps1 = JSON.parse(this.responseText);
      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */

      listeTitle = document.getElementById('listetudiant-title'); //console.log(listeTitle);
      //listeTitle.innerHTML=""

      listeTitle.innerText = "BORDOREAU DE NOTES UE --".concat(idUe, "-- ANNEE 202X-202X");

      for (var i = 0; i < myEtudiantStaps1.length; i++) {
        var tabledata1 = document.createElement('td');
        tabledata1.setAttribute('scope', 'row');
        tabledata1.innerText = myEtudiantStaps1[i].id;
        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantStaps1[i].matricule;
        var nom = myEtudiantStaps1[i].nom + ' ' + myEtudiantStaps1[i].prenom;
        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('input');
        tabledata4Input.type = "text";
        tabledata4Input.setAttribute('placeholder', "Note CC ".concat(myEtudiantStaps1[i].matricule, "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "CC ".concat(myEtudiantStaps1[i].matricule, " ").concat(idUe));
        tabledata4Input.setAttribute('id', "CC ".concat(myEtudiantStaps1[i].matricule).concat(idUe));
        tabledata4Input.setAttribute('required', ''); //tabledata4Input.setAttribute(`required`, "")

        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantStaps1[i].matricule, " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantStaps1[i].matricule, " ").concat(idUe));
        tabledata5Input.setAttribute('required', '');
        var tabledata5 = document.createElement('td');
        tabledata5.appendChild(tabledata5Input);
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata1);
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4);
        ligne.appendChild(tabledata5);
        /** TBODDY du modal afin d'ajouter les étudiants par filière */

        var listStudent = document.getElementById('listetudiant');
        listStudent.appendChild(ligne);
      }
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
      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */

      listeTitle = document.getElementById('listetudiant-title');
      listeTitle.innerText = "BORDOREAU DE NOTES UE --".concat(idUe, "-- ANNEE 202X-202X");
      tbodyMDS1 = document.getElementById('listetudiant');

      for (var i = 0; i < myEtudiantMDS1.length; i++) {
        var tabledata1 = document.createElement('td');
        tabledata1.setAttribute('scope', 'row');
        tabledata1.innerText = myEtudiantMDS1[i].id;
        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantMDS1[i].matricule;
        var nom = myEtudiantMDS1[i].nom + ' ' + myEtudiantMDS1[i].prenom;
        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('input');
        tabledata4Input.type = "text";
        tabledata4Input.setAttribute('placeholder', "Note CC ".concat(myEtudiantMDS1[i].matricule, "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "CC ".concat(myEtudiantMDS1[i].matricule, " ").concat(idUe));
        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantMDS1[i].matricule, " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantMDS1[i].matricule, " ").concat(idUe));
        var tabledata5 = document.createElement('td');
        tabledata5.appendChild(tabledata5Input);
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata1);
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4);
        ligne.appendChild(tabledata5);
        /** TBODDY du modal afin d'ajouter les étudiants par filière */

        var listStudent = document.getElementById('listetudiant');
        listStudent.appendChild(ligne);
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
      myEtudiantStaps1 = JSON.parse(this.responseText);
      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */

      listeTitle = document.getElementById('listetudiant-title'); //console.log(listeTitle);
      //listeTitle.innerHTML=""

      listeTitle.innerText = "BORDOREAU DE NOTES UE --".concat(idUe, "-- ANNEE 202X-202X");

      for (var i = 0; i < myEtudiantStaps1.length; i++) {
        var tabledata1 = document.createElement('td');
        tabledata1.setAttribute('scope', 'row');
        tabledata1.innerText = myEtudiantStaps1[i].id;
        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantStaps1[i].matricule;
        var nom = myEtudiantStaps1[i].nom + ' ' + myEtudiantStaps1[i].prenom;
        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('input');
        tabledata4Input.type = "text"; //console.log(element.parentElement.parentElement.parentElement.parentElement.children[0].innerText);

        tabledata4Input.setAttribute('placeholder', "Note CC ".concat(myEtudiantStaps1[i].matricule, "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "CC ".concat(myEtudiantStaps1[i].matricule, " ").concat(idUe));
        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantStaps1[i].matricule, " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantStaps1[i].matricule, " ").concat(idUe));
        var tabledata5 = document.createElement('td');
        tabledata5.appendChild(tabledata5Input);
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata1);
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4);
        ligne.appendChild(tabledata5);
        /** TBODDY du modal afin d'ajouter les étudiants par filière */

        var listStudent = document.getElementById('listetudiant');
        listStudent.appendChild(ligne);
      }
    }
  };

  xmlhttp.open("GET", url, true);
  xmlhttp.send();
}
/**REQUEST ETUDIANT NIVEAU 3 */


function getAllEtudiantNiveau3() {
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantNiveau3/";

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      myEtudiantNiveau3 = JSON.parse(this.responseText);
      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */

      listeTitle = document.getElementById('listetudiant-title');
      listeTitle.innerText = "BORDOREAU DE NOTES UE --".concat(idUe, "-- ANNEE 202X-202X");

      for (var i = 0; i < myEtudiantNiveau3.length; i++) {
        var tabledata1 = document.createElement('td');
        tabledata1.setAttribute('scope', 'row');
        tabledata1.innerText = myEtudiantNiveau3[i].id;
        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantNiveau3[i].matricule;
        var nom = myEtudiantNiveau3[i].nom + ' ' + myEtudiantNiveau3[i].prenom;
        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('input');
        tabledata4Input.type = "text"; //console.log(element.parentElement.parentElement.parentElement.parentElement.children[0].innerText);

        tabledata4Input.setAttribute('placeholder', "Note CC ".concat(myEtudiantNiveau3[i].matricule, "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "CC ".concat(myEtudiantNiveau3[i].matricule, " ").concat(idUe));
        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantNiveau3[i].matricule, " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantNiveau3[i].matricule, " ").concat(idUe));
        var tabledata5 = document.createElement('td');
        tabledata5.appendChild(tabledata5Input);
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata1);
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4);
        ligne.appendChild(tabledata5);
        /** TBODDY du modal afin d'ajouter les étudiants par filière */

        var listStudent = document.getElementById('listetudiant');
        listStudent.appendChild(ligne);
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
      listeTitle.innerText = "BORDOREAU DE NOTES UE --".concat(idUe, "-- ANNEE 202X-202X");

      for (var i = 0; i < myEtudiantNiveau3EVE.length; i++) {
        var tabledata1 = document.createElement('td');
        tabledata1.setAttribute('scope', 'row');
        tabledata1.innerText = myEtudiantNiveau3EVE[i].id;
        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantNiveau3EVE[i].matricule;
        var nom = myEtudiantNiveau3EVE[i].nom + ' ' + myEtudiantNiveau3EVE[i].prenom;
        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('input');
        tabledata4Input.type = "text"; //console.log(element.parentElement.parentElement.parentElement.parentElement.children[0].innerText);

        tabledata4Input.setAttribute('placeholder', "Note CC ".concat(myEtudiantNiveau3EVE[i].matricule, "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "CC ".concat(myEtudiantNiveau3EVE[i].matricule, " ").concat(idUe));
        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantNiveau3EVE[i].matricule, " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantNiveau3EVE[i].matricule, " ").concat(idUe));
        var tabledata5 = document.createElement('td');
        tabledata5.appendChild(tabledata5Input);
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata1);
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4);
        ligne.appendChild(tabledata5);
        /** TBODDY du modal afin d'ajouter les étudiants par filière */

        var listStudent = document.getElementById('listetudiant');
        listStudent.appendChild(ligne);
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
      listeTitle.innerText = "BORDOREAU DE NOTES UE --".concat(idUe, "-- ANNEE 202X-202X");

      for (var i = 0; i < myEtudiantNiveau3MSO.length; i++) {
        var tabledata1 = document.createElement('td');
        tabledata1.setAttribute('scope', 'row');
        tabledata1.innerText = myEtudiantNiveau3MSO[i].id;
        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantNiveau3MSO[i].matricule;
        var nom = myEtudiantNiveau3MSO[i].nom + ' ' + myEtudiantNiveau3MSO[i].prenom;
        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('input');
        tabledata4Input.type = "text"; //console.log(element.parentElement.parentElement.parentElement.parentElement.children[0].innerText);

        tabledata4Input.setAttribute('placeholder', "Note CC ".concat(myEtudiantNiveau3MSO[i].matricule, "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "CC ".concat(myEtudiantNiveau3MSO[i].matricule, " ").concat(idUe));
        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantNiveau3MSO[i].matricule, " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantNiveau3MSO[i].matricule, " ").concat(idUe));
        var tabledata5 = document.createElement('td');
        tabledata5.appendChild(tabledata5Input);
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata1);
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4);
        ligne.appendChild(tabledata5);
        /** TBODDY du modal afin d'ajouter les étudiants par filière */

        var listStudent = document.getElementById('listetudiant');
        listStudent.appendChild(ligne);
      }
    }
  };

  xmlhttp.open("GET", url, true);
  xmlhttp.send();
}
/** SEND DATA TO THE SERVER */


$(function () {
  $("form").validate({
    debug: true
  });
  $("form").on("submit", function (e) {
    e.preventDefault();
    var dataString = $(this).serialize();
    alert(dataString); //return false;

    $.ajax({
      type: "POST",
      url: "ajoutNoteEtudiant/",
      data: dataString,
      success: console.log('cool')
      /*() => {
      console.log("SUCCESS")
      submitForm = document.getElementById("submit")
      }*/

    }).done(function () {
      console.log(tbodylistStudent);
      tbodylistStudent.innerHTML = "";
      modal.style.display = "none";
    });
  });
});