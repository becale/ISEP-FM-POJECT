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
  tbodylistStudent2 = document.getElementById('listetudiant2');
  tbodylistStudent = document.getElementById('listetudiant'); // Get the modal For the add 

  modal = document.getElementById("myModal");
  main = document.getElementById('main'); //modal2 = modal.cloneNode(true)
  //modal2.setAttribute('id', 'modal2')

  modal2 = document.getElementById('modal2');
  modal2.children[0].children[0].setAttribute('id', 'myform2');
  modal2.children[0].children[0].children[2].children[0].children[0].children[1].setAttribute('id', 'listetudiant2');
  main.appendChild(modal2);
  modalf = $('.modal-footer')[1];
  modalf.children[0].setAttribute('id', 'submit2'); // Get the buttons that open the modal

  var btn = document.getElementsByClassName("myBtn");
  var btn1 = document.getElementsByClassName("myBtn-1");
  /**BOUTON DE FERMETURE NOTES */
  // GET the button that closes the modal

  spanClose = document.getElementsByClassName("close")[0]; //When the user clicks on span (x), close the modal

  spanClose.onclick = function () {
    /**VIDAGE DU CONTENEUR DE LISTE DES ETUDIANTS */
    //console.log(tbodylistStudent);
    tbodylistStudent.innerHTML = "";
    modal.style.display = "none";
  }; //MODAL 2


  spanClose1 = document.getElementsByClassName("close")[1]; //When the user clicks on span (x), close the modal

  spanClose1.onclick = function () {
    /**VIDAGE DU CONTENEUR DE LISTE DES ETUDIANTS */
    //console.log(tbodylistStudent);
    modal2.children[0].children[0].children[2].children[0].children[0].children[1].innerHTML = "";
    modal2.style.display = "none";
  };
  /**ITERATION AFIN D'OBTENIR LES LISTES DES ETUDIANTS INSCRITS DANS LES MATIERES */


  var _loop = function _loop(i) {
    btn[i].onclick = function (e) {
      if (myArr[i].code_UE.startsWith("EPS1")) {
        getetudiantStapsNiveau1();
      } else if (myArr[i].code_UE.startsWith("MDS1") || myArr[i].code_UE
      /*.startsWith*/
      == "MDS111b") {
        getetudiantMDSNiveau1();
      } else if (myArr[i].code_UE.startsWith("EPS2")) {
        getetudiantStapsNiveau2();
      } else if (myArr[i].code_UE.startsWith("MDS2")) {
        getetudiantMdsNiveau2();
      } else if (myArr[i].code_UE.startsWith("MAS")) {
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
  /**Btn-1 */


  var _loop2 = function _loop2(_i) {
    btn1[_i].onclick = function (e) {
      if (myArr[_i].code_UE.startsWith("EPS1")) {
        getetudiantStapsNiveau1R();
      } else if (myArr[_i].code_UE.startsWith("MDS1") || myArr[_i].code_UE
      /*.startsWith*/
      == "MDS111b") {
        getetudiantMDSNiveau1R();
      } else if (myArr[_i].code_UE.startsWith("EPS2")) {
        getetudiantStapsNiveau2R();
      } else if (myArr[_i].code_UE.startsWith("MDS2")) {
        getetudiantMdsNiveau2R();
      } else if (myArr[_i].code_UE.startsWith("MAS")) {
        getAllEtudiantNiveau3R();
      } else if (myArr[_i].code_UE.startsWith("EVE")) {
        getetudiantEVENiveau3R();
      } else if (myArr[_i].code_UE.startsWith("MSO")) {
        getetudiantMSONiveau3R();
      }

      modal2.style.display = "block";
    };
  };

  for (var _i = 0; _i < btn1.length; _i++) {
    _loop2(_i);
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
        } else if (myArr[i].semestre_id == 4) {
          imgSemestrePath = "/static/bulletin/icones/four_4.png";
        } else if (myArr[i].semestre_id == 5) {
          imgSemestrePath = "/static/bulletin/icones/five_5.png";
        } else if (myArr[i].semestre_id == 6) {
          imgSemestrePath = "/static/bulletin/icones/number_6.png";
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
        var myBtn = document.createElement('button');
        myBtn.setAttribute('id', "myBtn".concat(i));
        myBtn.setAttribute('class', 'myBtn');
        var imgbtn1 = document.createElement('img');
        var addPathImg1 = "/static/bulletin/icones/edit.png";
        imgbtn1.setAttribute("src", addPathImg1);
        var myBtn1 = document.createElement('button');
        myBtn1.setAttribute('id', "myBtn-".concat(i));
        myBtn1.setAttribute('class', 'myBtn-1'); //myBtn1.appendChild(imgbtn1)

        var add = document.createElement('div');
        var textMessage = document.createTextNode('SN');
        add.setAttribute("id", "add");
        myBtn.appendChild(textMessage);
        add.appendChild(myBtn);
        var modify = document.createElement('div');
        var textMessage1 = document.createTextNode('SR');
        modify.setAttribute("id", "modify");
        myBtn1.appendChild(textMessage1);
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

        if (myArr[i].code_UE.startsWith('MDS')) {
          matiere.classList.add('MDS');
        } else if (myArr[i].code_UE.startsWith('EPS1')) {
          matiere.classList.add('EPS1');
        } else if (myArr[i].code_UE.startsWith('EPS2')) {
          matiere.classList.add('EPS2');
        } else {
          matiere.classList.add('MASEVE');
        }

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
/** REQUEST ETUDIANTS STAPS NIVEAU 1 */

function getetudiantStapsNiveau1() {
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantStaps1/";

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      myEtudiantStaps1 = JSON.parse(this.responseText);
      console.log(myEtudiantStaps1); //SN & CC

      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */

      listeTitle = document.getElementById('listetudiant-title');
      listeTitle.innerText = "BORDOREAU DE NOTES UE --".concat(idUe, "--  Ann\xE9e Acad\xE9mique ").concat(myEtudiantStaps1['dateExamen'][0]['annee_academique']);

      for (var i = 0; i < myEtudiantStaps1['etudiantStaps1'].length; i++) {
        var tabledata1 = document.createElement('td');
        tabledata1.setAttribute('scope', 'row');
        tabledata1.innerText = myEtudiantStaps1['etudiantStaps1'][i]['id'];
        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantStaps1['etudiantStaps1'][i]['matricule'];
        var nom = myEtudiantStaps1['etudiantStaps1'][i]['nom'] + ' ' + myEtudiantStaps1['etudiantStaps1'][i]['prenom'];
        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('input');
        tabledata4Input.type = "text";
        tabledata4Input.setAttribute('placeholder', "Note CC ".concat(myEtudiantStaps1['etudiantStaps1'][i]['nom'] + ' ' + myEtudiantStaps1['etudiantStaps1'][i]['prenom'], "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "CC ".concat(myEtudiantStaps1['etudiantStaps1'][i]['matricule'], " ").concat(idUe));
        tabledata4Input.setAttribute('id', "CC ".concat(myEtudiantStaps1['etudiantStaps1'][i]['matricule']).concat(idUe)); //tabledata4Input.setAttribute('required', '')

        Object.keys(myEtudiantStaps1['S1']["ListeNoteUeS1EPS1"][idUe]).length > 0 ? tabledata4Input.value = myEtudiantStaps1['S1']["ListeNoteUeS1EPS1"][idUe][i]['note_cc'] : console.log('LE coup fonctionne');
        tabledata4Input.setAttribute('class', 'noteField'); //tabledata4Input

        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantStaps1['etudiantStaps1'][i]['matricule'], " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantStaps1['etudiantStaps1'][i]['matricule'], " ").concat(idUe)); //tabledata5Input.setAttribute('required', '')

        /**TEST du contenu des UE */

        Object.keys(myEtudiantStaps1['S1']["ListeNoteUeS1EPS1"][idUe]).length > 0 ? tabledata5Input.value = myEtudiantStaps1['S1']["ListeNoteUeS1EPS1"][idUe][i]['note_sn'] : console.log('LE coup fonctionne');
        tabledata5Input.setAttribute('class', 'noteField');
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
/** REQUEST ETUDIANTS STAPS NIVEAU 1 RATTRAPAGE */


function getetudiantStapsNiveau1R() {
  //Masquage de la div SN
  modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[3].innerHTML = "Rattrapage (Rt)";
  modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[4].style.display = "none";
  myform2 = document.getElementById('modal2').children[0].children[0];
  myform2.setAttribute('id', 'myform2'); //console.log(myForm);

  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantStaps1/";

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      myEtudiantStaps1 = JSON.parse(this.responseText); //SN & CC

      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */
      //listeTitle = document.getElementById('listetudiant-title')

      listeTitle = modal2.children[0].children[0].children[1].children[1];
      listeTitle.innerText = "BORDOREAU DE NOTES UE --".concat(idUe, "-- Ann\xE9e Acad\xE9mique ").concat(myEtudiantStaps1['dateExamen'][0]['annee_academique']);

      for (var i = 0; i < myEtudiantStaps1['etudiantStaps1'].length; i++) {
        var tabledata1 = document.createElement('td');
        tabledata1.setAttribute('scope', 'row');
        tabledata1.innerText = myEtudiantStaps1['etudiantStaps1'][i]['id'];
        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantStaps1['etudiantStaps1'][i]['matricule'];
        var nom = myEtudiantStaps1['etudiantStaps1'][i]['nom'] + ' ' + myEtudiantStaps1['etudiantStaps1'][i]['prenom'];
        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('input');
        tabledata4Input.type = "text";
        tabledata4Input.setAttribute('placeholder', "Note Rattrapage ".concat(myEtudiantStaps1['etudiantStaps1'][i]['matricule'], "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "Rattrapage ".concat(myEtudiantStaps1['etudiantStaps1'][i]['matricule'], " ").concat(idUe));
        tabledata4Input.setAttribute('id', "Rattrapage ".concat(myEtudiantStaps1['etudiantStaps1'][i]['matricule']).concat(idUe)); //tabledata4Input.setAttribute('required', '')

        Object.keys(myEtudiantStaps1['S1']["ListeNoteUeS1EPS1R"][idUe]).length > 0 ? tabledata4Input.value = myEtudiantStaps1['S1']["ListeNoteUeS1EPS1"][idUe][i]['note_rattrapage'] : console.log('LE coup fonctionne');
        tabledata4Input.setAttribute('class', 'noteField'); //tabledata4Input

        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantStaps1['etudiantStaps1'][i]['matricule'], " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantStaps1['etudiantStaps1'][i]['matricule'], " ").concat(idUe));
        tabledata5Input.setAttribute('required', '');
        tabledata5Input.setAttribute('class', 'noteField');
        var tabledata5 = document.createElement('td');
        tabledata5.appendChild(tabledata5Input);
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata1);
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4); //ligne.appendChild(tabledata5);

        /** TBODDY du modal afin d'ajouter les étudiants par filière */

        var listStudent12 = modal2.children[0].children[0].children[2].children[0].children[0].children[1];
        listStudent12.appendChild(ligne);
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
      myEtudiantMDS1 = JSON.parse(this.responseText); //console.log(myEtudiantMDS1);
      //console.log(myEtudiantMDS1["etudiantMDS1"]);
      //console.log(myEtudiantMDS1[1]);

      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */

      listeTitle = document.getElementById('listetudiant-title');
      listeTitle.innerText = "BORDOREAU DE NOTES UE --".concat(idUe, "-- Ann\xE9e Acad\xE9mique ").concat(myEtudiantMDS1['dateExamen'][0]['annee_academique']);
      tbodyMDS1 = document.getElementById('listetudiant'); //console.log(myEtudiantMDS1['matriceUENotesMDS1']);

      for (var i = 0; i < myEtudiantMDS1['etudiantMDS1'].length
      /*myEtudiantMDS1.length*/
      ; i++) {
        var tabledata1 = document.createElement('td');
        tabledata1.setAttribute('scope', 'row');
        tabledata1.innerText = myEtudiantMDS1['etudiantMDS1'][i]['id']; //myEtudiantMDS1[0][i].id

        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantMDS1['etudiantMDS1'][i]['matricule']; //myEtudiantMDS1[i].matricule

        var nom = myEtudiantMDS1['etudiantMDS1'][i]['nom']
        /*myEtudiantMDS1[i].nom*/
        + ' ' + myEtudiantMDS1['etudiantMDS1'][i]['prenom'];
        /*myEtudiantMDS1[i].prenom*/

        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('input');
        tabledata4Input.type = "text";
        tabledata4Input.setAttribute('placeholder', "Note CC ".concat(myEtudiantMDS1['etudiantMDS1'][i]['matricule']
        /*myEtudiantMDS1[i].matricule*/
        , "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "CC ".concat(myEtudiantMDS1['etudiantMDS1'][i]['matricule']
        /*myEtudiantMDS1[i].matricule*/
        , " ").concat(idUe)); //tabledata4Input.setAttribute('id', `CC ${myEtudiantMDS1['etudiantMDS1'][i]['matricule']/*myEtudiantMDS1[i].matricule*/} ${idUe}`)
        //tabledata4Input.setAttribute('required', '');

        Object.keys(myEtudiantMDS1['matriceUENotesMDS1'][idUe][0]).length > 0 ? tabledata4Input.value = myEtudiantMDS1['matriceUENotesMDS1'][idUe][0][i]["note_cc"] : //tabledata4Input.value = myEtudiantMDS1['matriceUENotesMDS1'][idUe][0][i]["note_cc"]//'alpha'
        tabledata4Input.setAttribute('class', 'noteField');
        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantMDS1['etudiantMDS1'][i]['matricule']
        /*myEtudiantMDS1[i].matricule*/
        , " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantMDS1['etudiantMDS1'][i]['matricule']
        /*myEtudiantMDS1[i].matricule*/
        , " ").concat(idUe)); //tabledata5Input.setAttribute('required','');

        Object.keys(myEtudiantMDS1['matriceUENotesMDS1'][idUe][0]).length > 0 ? tabledata5Input.value = myEtudiantMDS1['matriceUENotesMDS1'][idUe][0][i]["note_sn"] : tabledata5Input.setAttribute('class', 'noteField');
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
/** REQUEST ETUDIANTS MDS NIVEAU 1 RATTRAPAGE */


function getetudiantMDSNiveau1R() {
  //Masquage de la div SN
  modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[3].innerHTML = "Rattrapage (Rt)";
  modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[4].style.display = "none";
  myform2 = document.getElementById('modal2').children[0].children[0];
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantMDS1/";

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      myEtudiantMDS1 = JSON.parse(this.responseText);
      console.log(myEtudiantMDS1);
      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */
      //listeTitle = document.getElementById('listetudiant-title')

      listeTitle = modal2.children[0].children[0].children[1].children[1];
      listeTitle.innerText = "BORDOREAU DE NOTES UE --".concat(idUe, "-- Ann\xE9e Acad\xE9mique ").concat(myEtudiantMDS1['dateExamen'][0]['annee_academique']);
      tbodyMDS1 = document.getElementById('listetudiant'); //let test = ( Object.keys(myEtudiantMDS1['matriceUENotesMDS1']).length === 0 )

      for (var i = 0; i < myEtudiantMDS1['etudiantMDS1'].length
      /*myEtudiantMDS1.length*/
      ; i++) {
        console.log("OK OK");
        var tabledata1 = document.createElement('td');
        tabledata1.innerText = myEtudiantMDS1['etudiantMDS1'][i]['id']; //myEtudiantMDS1[i].id

        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantMDS1['etudiantMDS1'][i]['matricule']; //myEtudiantMDS1[i].matricule

        var nom = myEtudiantMDS1['etudiantMDS1'][i]['nom']
        /*myEtudiantMDS1[i].nom*/
        + ' ' + myEtudiantMDS1['etudiantMDS1'][i]['prenom'];
        /*myEtudiantMDS1[i].prenom*/

        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('input');
        tabledata4Input.type = "text";
        tabledata4Input.setAttribute('placeholder', "Note Rattrapage ".concat(myEtudiantMDS1['etudiantMDS1'][i]['matricule']
        /*myEtudiantMDS1[i].matricule*/
        , " ").concat(idUe));
        tabledata4Input.setAttribute('name', "Rattrapage ".concat(myEtudiantMDS1['etudiantMDS1'][i]['matricule'], " ").concat(idUe));
        tabledata4Input.setAttribute('id', "Rattrapage ".concat(myEtudiantMDS1['etudiantMDS1'][i]['matricule']).concat(idUe)); //tabledata4Input.setAttribute('required', '')

        /**TEST du contenu des UE */

        Object.keys(myEtudiantMDS1['matriceUENotesMDS1R'][idUe][0]).length > 0 ? tabledata4Input.value = myEtudiantMDS1['matriceUENotesMDS1R'][idUe][0][i]['note_rattrapage'] : console.log('LE coup fonctionne');
        tabledata4Input.setAttribute('class', 'noteField'); //tabledata4Input

        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantMDS1['etudiantMDS1'][i]['matricule'], " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantMDS1['etudiantMDS1'][i]['matricule'], " ").concat(idUe)); //tabledata5Input.setAttribute('required','');

        tabledata5Input.setAttribute('class', 'noteField');
        var tabledata5 = document.createElement('td');
        tabledata5.appendChild(tabledata5Input);
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata1);
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4); //ligne.appendChild(tabledata5);

        /** TBODDY du modal afin d'ajouter les étudiants par filière */

        /*const listStudent = document.getElementById('listetudiant')
        listStudent.appendChild(ligne)*/

        var listStudent12 = modal2.children[0].children[0].children[2].children[0].children[0].children[1];
        listStudent12.appendChild(ligne);
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
      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */

      listeTitle = document.getElementById('listetudiant-title'); //console.log(listeTitle);
      //listeTitle.innerHTML=""

      listeTitle.innerText = "BORDOREAU DE NOTES UE --".concat(idUe, "-- ANNEE 202X-202X");

      for (var i = 0; i < myEtudiantStaps2.length; i++) {
        var tabledata1 = document.createElement('td');
        tabledata1.setAttribute('scope', 'row');
        tabledata1.innerText = myEtudiantStaps2[i].id;
        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantStaps2[i].matricule;
        var nom = myEtudiantStaps2[i].nom + ' ' + myEtudiantStaps2[i].prenom;
        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('input');
        tabledata4Input.type = "text";
        tabledata4Input.setAttribute('placeholder', "Note CC ".concat(myEtudiantStaps2[i].matricule, "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "CC ".concat(myEtudiantStaps2[i].matricule, " ").concat(idUe));
        tabledata4Input.setAttribute('id', "CC ".concat(myEtudiantStaps2[i].matricule, " ").concat(idUe)); //tabledata4Input.setAttribute('required','')

        tabledata4Input.setAttribute('class', 'noteField');
        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantStaps2[i].matricule, " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantStaps2[i].matricule, " ").concat(idUe)); //tabledata5Input.setAttribute('required','');

        tabledata5Input.setAttribute('class', 'noteField');
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
/**  REQUEST ETUDIANT STAPS NIVEAU 2 RATTRAPAGE */


function getetudiantStapsNiveau2R() {
  //Masquage de la div SN
  modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[3].innerHTML = "Rattrapage (Rt)";
  modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[4].style.display = "none";
  myform2 = document.getElementById('modal2').children[0].children[0];
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantStaps2/";

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      myEtudiantStaps2 = JSON.parse(this.responseText);
      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */
      //listeTitle = document.getElementById('listetudiant-title')
      //console.log(listeTitle);
      //listeTitle.innerHTML=""

      listeTitle = modal2.children[0].children[0].children[1].children[1];
      listeTitle.innerText = "BORDOREAU DE NOTES UE --".concat(idUe, "-- ANNEE 202X-202X"); //tbodyMDS1 = document.getElementById('listetudiant')

      for (var i = 0; i < myEtudiantStaps2.length; i++) {
        var tabledata1 = document.createElement('td');
        tabledata1.setAttribute('scope', 'row');
        tabledata1.innerText = myEtudiantStaps2[i].id;
        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantStaps2[i].matricule;
        var nom = myEtudiantStaps2[i].nom + ' ' + myEtudiantStaps2[i].prenom;
        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('input');
        tabledata4Input.type = "text";
        tabledata4Input.setAttribute('placeholder', "Note Rattrapage ".concat(myEtudiantStaps2[i].matricule, "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "Rattrapage ".concat(myEtudiantStaps2[i].matricule, " ").concat(idUe));
        tabledata4Input.setAttribute('id', "Rattrapage ".concat(myEtudiantStaps2[i].matricule).concat(idUe)); //tabledata4Input.setAttribute('required', '')

        tabledata4Input.setAttribute('class', 'noteField');
        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantStaps2[i].matricule, " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantStaps2[i].matricule, " ").concat(idUe)); //tabledata5Input.setAttribute('required','');

        tabledata5Input.setAttribute('class', 'noteField');
        var tabledata5 = document.createElement('td');
        tabledata5.appendChild(tabledata5Input);
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata1);
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4); //ligne.appendChild(tabledata5);

        /** TBODDY du modal afin d'ajouter les étudiants par filière */
        //const listStudent = document.getElementById('listetudiant')

        var listStudent12 = modal2.children[0].children[0].children[2].children[0].children[0].children[1];
        listStudent12.appendChild(ligne);
      }
    }
  };

  xmlhttp.open("GET", url, true);
  xmlhttp.send();
}
/**  REQUEST ETUDIANT MDS NIVEAU 2 */


function getetudiantMdsNiveau2() {
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantMds2/";

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      myEtudiantMds2 = JSON.parse(this.responseText);
      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */

      listeTitle = document.getElementById('listetudiant-title'); //console.log(listeTitle);
      //listeTitle.innerHTML=""

      listeTitle.innerText = "BORDOREAU DE NOTES UE --".concat(idUe, "-- Ann\xE9e Acad\xE9mique ").concat(myEtudiantMds2['dateExamen'][0]['annee_academique']);

      for (var i = 0; i < myEtudiantMds2['etudiantMDS2'].length; i++) {
        var tabledata1 = document.createElement('td');
        tabledata1.setAttribute('scope', 'row');
        tabledata1.innerText = myEtudiantMds2['etudiantMDS2'][i]['id']; //myEtudiantMds2[i].id

        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantMds2['etudiantMDS2'][i]['matricule']; //myEtudiantMds2[i].matricule

        var nom = myEtudiantMds2['etudiantMDS2'][i]['nom']
        /*myEtudiantMDS1[i].nom*/
        + ' ' + myEtudiantMds2['etudiantMDS2'][i]['prenom'];
        /*myEtudiantMDS1[i].prenom*/

        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('input');
        tabledata4Input.type = "text";
        tabledata4Input.setAttribute('placeholder', "Note CC ".concat(myEtudiantMds2['etudiantMDS2'][i]['matricule'], "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "CC ".concat(myEtudiantMds2['etudiantMDS2'][i]['matricule'], " ").concat(idUe));
        tabledata4Input.setAttribute('id', "CC ".concat(myEtudiantMds2['etudiantMDS2'][i]['matricule'], " ").concat(idUe)); //tabledata4Input.setAttribute('required','')

        Object.keys(myEtudiantMds2['matriceUENotesMDS2'][idUe][0]).length > 0 ? tabledata4Input.value = myEtudiantMds2['matriceUENotesMDS2'][idUe][0][i]["note_cc"] : tabledata4Input.setAttribute('class', 'noteField');
        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantMds2['etudiantMDS2'][i]['matricule'], " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantMds2['etudiantMDS2'][i]['matricule'], " ").concat(idUe)); //tabledata5Input.setAttribute('required','');

        Object.keys(myEtudiantMds2['matriceUENotesMDS2'][idUe][0]).length > 0 ? tabledata5Input.value = myEtudiantMds2['matriceUENotesMDS2'][idUe][0][i]["note_sn"] : tabledata5Input.setAttribute('class', 'noteField');
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
/**  REQUEST ETUDIANT MDS NIVEAU 2 RATTRAPAGE */


function getetudiantMdsNiveau2R() {
  //Masquage de la div SN
  modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[3].innerHTML = "Rattrapage (Rt)";
  modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[4].style.display = "none";
  myform2 = document.getElementById('modal2').children[0].children[0];
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantMds2/";

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      myEtudiantMds2 = JSON.parse(this.responseText);
      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */
      //listeTitle = document.getElementById('listetudiant-title')
      //console.log(listeTitle);
      //listeTitle.innerHTML=""

      listeTitle = modal2.children[0].children[0].children[1].children[1];
      listeTitle.innerText = "BORDOREAU DE NOTES UE --".concat(idUe, "-- Ann\xE9e Acad\xE9mique ").concat(myEtudiantMds2['dateExamen'][0]['annee_academique']); //tbodyMDS1 = document.getElementById('listetudiant')

      for (var i = 0; i < myEtudiantMds2['etudiantMDS2'].length; i++) {
        var tabledata1 = document.createElement('td');
        tabledata1.setAttribute('scope', 'row');
        tabledata1.innerText = myEtudiantMds2['etudiantMDS2'][i]['id']; //myEtudiantMds2[i].id

        var tabledata2 = document.createElement('td');
        tabledata2.innerText = myEtudiantMds2['etudiantMDS2'][i]['matricule']; //myEtudiantMds2[i].matricule

        var nom = myEtudiantMds2['etudiantMDS2'][i]['nom']
        /*myEtudiantMDS1[i].nom*/
        + ' ' + myEtudiantMds2['etudiantMDS2'][i]['prenom'];
        /*myEtudiantMDS1[i].prenom*/

        var tabledata3 = document.createElement('td');
        tabledata3.innerText = nom;
        var tabledata4Input = document.createElement('input');
        tabledata4Input.type = "text";
        tabledata4Input.setAttribute('placeholder', "Note Rattrapage ".concat(myEtudiantMds2['etudiantMDS2'][i]['matricule'], "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "Rattrapage ".concat(myEtudiantMds2['etudiantMDS2'][i]['matricule'], " ").concat(idUe));
        tabledata4Input.setAttribute('id', "Rattrapage ".concat(myEtudiantMds2['etudiantMDS2'][i]['matricule']).concat(idUe)); //tabledata4Input.setAttribute('required', '')

        Object.keys(myEtudiantMds2['matriceUENotesMDS2R'][idUe][0]).length > 0 ? tabledata4Input.value = myEtudiantMds2['matriceUENotesMDS2R'][idUe][0][i]['note_rattrapage'] : console.log('LE coup fonctionne');
        tabledata4Input.setAttribute('class', 'noteField');
        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantMds2['etudiantMDS2'][i]['matricule'], " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantMds2['etudiantMDS2'][i]['matricule'], " ").concat(idUe)); //tabledata5Input.setAttribute('required','');

        tabledata5Input.setAttribute('class', 'noteField');
        var tabledata5 = document.createElement('td');
        tabledata5.appendChild(tabledata5Input);
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata1);
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4); //ligne.appendChild(tabledata5);

        /** TBODDY du modal afin d'ajouter les étudiants par filière */
        //const listStudent = document.getElementById('listetudiant')

        var listStudent12 = modal2.children[0].children[0].children[2].children[0].children[0].children[1];
        listStudent12.appendChild(ligne);
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
        tabledata4Input.setAttribute('id', "CC ".concat(myEtudiantNiveau3[i].matricule, " ").concat(idUe)); //tabledata4Input.setAttribute('required','')

        tabledata4Input.setAttribute('class', 'noteField');
        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantNiveau3[i].matricule, " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantNiveau3[i].matricule, " ").concat(idUe)); //tabledata5Input.setAttribute('required', '');

        tabledata5Input.setAttribute('class', 'noteField');
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
/**REQUEST ETUDIANT NIVEAU 3 RATTRAPAGE */


function getAllEtudiantNiveau3R() {
  //Masquage de la div SN
  modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[3].innerHTML = "Rattrapage (Rt)";
  modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[4].style.display = "none";
  myform2 = document.getElementById('modal2').children[0].children[0];
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantNiveau3/";

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      myEtudiantNiveau3 = JSON.parse(this.responseText);
      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */
      //listeTitle = document.getElementById('listetudiant-title')

      listeTitle = modal2.children[0].children[0].children[1].children[1];
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
        tabledata4Input.type = "text";
        tabledata4Input.setAttribute('placeholder', "Note Rattrapage ".concat(myEtudiantNiveau3[i].matricule, "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "Rattrapage ".concat(myEtudiantNiveau3[i].matricule, " ").concat(idUe));
        tabledata4Input.setAttribute('id', "Rattrapage ".concat(myEtudiantNiveau3[i].matricule).concat(idUe)); //tabledata4Input.setAttribute('required', '')

        tabledata4Input.setAttribute('class', 'noteField');
        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantNiveau3[i].matricule, " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantNiveau3[i].matricule, " ").concat(idUe)); //tabledata5Input.setAttribute('required', '');

        tabledata5Input.setAttribute('class', 'noteField');
        var tabledata5 = document.createElement('td');
        tabledata5.appendChild(tabledata5Input);
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata1);
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4); //ligne.appendChild(tabledata5);

        /** TBODDY du modal afin d'ajouter les étudiants par filière */
        //const listStudent = document.getElementById('listetudiant')
        //listStudent.appendChild(ligne)

        var listStudent12 = modal2.children[0].children[0].children[2].children[0].children[0].children[1];
        listStudent12.appendChild(ligne);
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
      //listeTitle = document.getElementById('listetudiant-title')

      listeTitle = modal2.children[0].children[0].children[1].children[1];
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
        tabledata4Input.type = "text";
        tabledata4Input.setAttribute('placeholder', "Note CC ".concat(myEtudiantNiveau3EVE[i].matricule, "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "CC ".concat(myEtudiantNiveau3EVE[i].matricule, " ").concat(idUe));
        tabledata4Input.setAttribute('id', "CC ".concat(myEtudiantNiveau3EVE[i].matricule).concat(idUe)); //tabledata4Input.setAttribute('required', '')

        tabledata4Input.setAttribute('class', 'noteField'); //tabledata4Input

        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantNiveau3EVE[i].matricule, " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantNiveau3EVE[i].matricule, " ").concat(idUe)); //tabledata5Input.setAttribute('required','');

        tabledata5Input.setAttribute('class', 'noteField');
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
/** REQUEST ETUDIANTS EVE RATTRAPAGE */


function getetudiantEVENiveau3R() {
  //Masquage de la div SN
  modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[3].innerHTML = "Rattrapage (Rt)";
  modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[4].style.display = "none";
  myform2 = document.getElementById('modal2').children[0].children[0];
  var xmlhttp = new XMLHttpRequest();
  var url = "http://localhost:8000/etudiantNiveau3EVE/";

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      myEtudiantNiveau3EVE = JSON.parse(this.responseText);
      /** Ajout des lignes pour insertion des notes des étudiants */

      /**Changement du TITRE Du modal */
      //listeTitle = document.getElementById('listetudiant-title')

      listeTitle = modal2.children[0].children[0].children[1].children[1];
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
        tabledata4Input.type = "text";
        tabledata4Input.setAttribute('placeholder', "Note Rattrapage ".concat(myEtudiantNiveau3EVE[i].matricule, "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "Rattrapage ".concat(myEtudiantNiveau3EVE[i].matricule, " ").concat(idUe));
        tabledata4Input.setAttribute('id', "Rattrapage ".concat(myEtudiantNiveau3EVE[i].matricule).concat(idUe)); //tabledata4Input.setAttribute('required', '')

        tabledata4Input.setAttribute('class', 'noteField'); //tabledata4Input

        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantNiveau3EVE[i].matricule, " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantNiveau3EVE[i].matricule, " ").concat(idUe)); //tabledata5Input.setAttribute('required','');

        tabledata5Input.setAttribute('class', 'noteField');
        var tabledata5 = document.createElement('td');
        tabledata5.appendChild(tabledata5Input);
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata1);
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4); //ligne.appendChild(tabledata5);

        /** TBODDY du modal afin d'ajouter les étudiants par filière */
        //const listStudent = document.getElementById('listetudiant')
        //listStudent.appendChild(ligne)

        var listStudent12 = modal2.children[0].children[0].children[2].children[0].children[0].children[1];
        listStudent12.appendChild(ligne);
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
        tabledata4Input.setAttribute('id', "CC ".concat(myEtudiantNiveau3MSO[i].matricule, " ").concat(idUe)); //tabledata4Input.setAttribute('required', '')

        tabledata4Input.setAttribute('class', 'noteField');
        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantNiveau3MSO[i].matricule, " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantNiveau3MSO[i].matricule, " ").concat(idUe)); //tabledata5Input.setAttribute('required', '')

        tabledata5Input.setAttribute('class', 'noteField');
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
/** REQUEST ETUDIANTS MSO RATTRAPAGE */


function getetudiantMSONiveau3R() {
  //Masquage de la div SN
  modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[3].innerHTML = "Rattrapage (Rt)";
  modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[4].style.display = "none";
  myform2 = document.getElementById('modal2').children[0].children[0];
  myform2.setAttribute('id', 'myform2');
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
        tabledata4Input.type = "text";
        tabledata4Input.setAttribute('placeholder', "Note Rattrapage ".concat(myEtudiantNiveau3MSO[i].matricule, "  ").concat(idUe));
        tabledata4Input.setAttribute('name', "Rattrapage ".concat(myEtudiantNiveau3MSO[i].matricule, " ").concat(idUe));
        tabledata4Input.setAttribute('id', "Rattrapage ".concat(myEtudiantNiveau3MSO[i].matricule).concat(idUe)); //tabledata4Input.setAttribute('required', '')

        tabledata4Input.setAttribute('class', 'noteField');
        var tabledata4 = document.createElement('td');
        tabledata4.appendChild(tabledata4Input);
        var tabledata5Input = document.createElement('input');
        tabledata5Input.type = "text";
        tabledata5Input.setAttribute('placeholder', "Note SN ".concat(myEtudiantNiveau3MSO[i].matricule, " ").concat(idUe));
        tabledata5Input.setAttribute('name', "SN ".concat(myEtudiantNiveau3MSO[i].matricule, " ").concat(idUe)); //tabledata5Input.setAttribute('required', '')

        tabledata5Input.setAttribute('class', 'noteField');
        var tabledata5 = document.createElement('td');
        tabledata5.appendChild(tabledata5Input);
        var ligne = document.createElement('tr');
        ligne.appendChild(tabledata1);
        ligne.appendChild(tabledata2);
        ligne.appendChild(tabledata3);
        ligne.appendChild(tabledata4); //ligne.appendChild(tabledata5);

        /** TBODDY du modal afin d'ajouter les étudiants par filière */

        /*const listStudent = document.getElementById('listetudiant')
        listStudent.appendChild(ligne)*/
      }
    }
  };

  xmlhttp.open("GET", url, true);
  xmlhttp.send();
}
/** SEND DATA TO THE SERVER */


$(function Examen() {
  dataString1 = $("#myForm").serializeArray();
  options1 = {
    //data : dataString,
    //target:"",
    url: 'ajoutNoteEtudiant/',
    type: "POST",
    success: ""
  };
  /**Validation par classe */

  jQuery.validator.addClassRules("noteField", {
    required: true
  });
  $("#myForm").submit(function (e) {
    e.preventDefault();
    console.log('OK');
  }).validate({
    submitHandler: function submitHandler(form) {
      $("#myForm").ajaxSubmit(options1);
      tbodylistStudent.innerHTML = "";
      modal.style.display = "none";
      alert("LES NOTES ONT ETE ENREGISTREES AVEC SUCCESS");
    }
  });
});
/** SEND DATA TO THE SERVER */
//RATTRAPAGE

$(function Rattrapage() {
  dataString = $("#myform2").serializeArray();
  options = {
    //data : dataString,
    //target:"",
    url: 'ajoutNoteEtudiantRattrapage/',
    type: "POST",
    success: ""
  };
  /**Validation par classe */

  jQuery.validator.addClassRules("noteField", {
    required: true
  });
  $("#myform2").submit(function (e) {
    e.preventDefault();
  }).validate({
    submitHandler: function submitHandler() {
      $("#myform2").ajaxSubmit(options);
      modal2.children[0].children[0].children[2].children[0].children[0].children[1].innerHTML = ""; //tbodylistStudent2.innerHTML = ""

      modal2.style.display = "none";
      alert("LES NOTES ONT ETE ENREGISTREES AVEC SUCCESS");
    }
  });
});