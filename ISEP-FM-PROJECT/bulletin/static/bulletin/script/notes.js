title = document.getElementById('listetudiant-title')
console.log(title);

/** GET THE ID OF Buttons */
function getButtonId() {
    // Create event listener
    document.addEventListener('click', (e) => {
        // Retrieve id from clicked element
        if (e.target.id !== '' && e.target.tagName == 'BUTTON') {
            //console.log(e.target.parentElement.parentElement.parentElement.parentElement.children[0].innerText);
            idUe = e.target.parentElement.parentElement.parentElement.parentElement.children[0].innerText
                //
        } else { // If element has no id
            console.log(`object doesn't have ID`);
            console.log(idUe);

        }
    });
}
getButtonId()


/********************************** MODAL *************************************************/
function modal() {

    tbodylistStudent2 = document.getElementById('listetudiant2')

    tbodylistStudent = document.getElementById('listetudiant')

    // Get the modal For the add 
    modal = document.getElementById("myModal");

    main = document.getElementById('main')



    //modal2 = modal.cloneNode(true)
    //modal2.setAttribute('id', 'modal2')

    modal2 = document.getElementById('modal2')

    modal2.children[0].children[0].setAttribute('id', 'myform2')
    modal2.children[0].children[0].children[2].children[0].children[0].children[1].setAttribute('id', 'listetudiant2')
    main.appendChild(modal2)

    modalf = $('.modal-footer')[1]
    modalf.children[0].setAttribute('id', 'submit2')

    // Get the buttons that open the modal
    var btn = document.getElementsByClassName("myBtn");
    var btn1 = document.getElementsByClassName("myBtn-1");

    /**BOUTON DE FERMETURE NOTES */
    // GET the button that closes the modal
    spanClose = document.getElementsByClassName("close")[0];
    //When the user clicks on span (x), close the modal
    spanClose.onclick = function() {
        /**VIDAGE DU CONTENEUR DE LISTE DES ETUDIANTS */
        //console.log(tbodylistStudent);
        tbodylistStudent.innerHTML = ""
        modal.style.display = "none";
    }

    //MODAL 2
    spanClose1 = document.getElementsByClassName("close")[1];
    //When the user clicks on span (x), close the modal
    spanClose1.onclick = function() {
        /**VIDAGE DU CONTENEUR DE LISTE DES ETUDIANTS */
        //console.log(tbodylistStudent);
        modal2.children[0].children[0].children[2].children[0].children[0].children[1].innerHTML = ""
        modal2.style.display = "none";
    }

    /**ITERATION AFIN D'OBTENIR LES LISTES DES ETUDIANTS INSCRITS DANS LES MATIERES */
    for (let i = 0; i < btn.length; i++) {
        btn[i].onclick = function(e) {

            if (myArr[i].code_UE.startsWith("EPS1")) {
                getetudiantStapsNiveau1()
            } else if (myArr[i].code_UE.startsWith("MDS1") || myArr[i].code_UE /*.startsWith*/ == ("MDS111b")) {
                getetudiantMDSNiveau1()
            } else if (myArr[i].code_UE.startsWith("EPS2")) {
                getetudiantStapsNiveau2()
            } else if (myArr[i].code_UE.startsWith("MDS2")) {
                getetudiantMdsNiveau2()
            } else if (myArr[i].code_UE.startsWith("MAS")) {
                getAllEtudiantNiveau3()
            } else if (myArr[i].code_UE.startsWith("EVE")) {
                getetudiantEVENiveau3()
            } else if (myArr[i].code_UE.startsWith("MSO")) {
                getetudiantMSONiveau3()
            }
            modal.style.display = "block"
        };
    }
    /**Btn-1 */
    for (let i = 0; i < btn1.length; i++) {
        btn1[i].onclick = function(e) {

            if (myArr[i].code_UE.startsWith("EPS1")) {
                getetudiantStapsNiveau1R()
            } else if (myArr[i].code_UE.startsWith("MDS1") || myArr[i].code_UE /*.startsWith*/ == ("MDS111b")) {
                getetudiantMDSNiveau1R()
            } else if (myArr[i].code_UE.startsWith("EPS2")) {
                getetudiantStapsNiveau2R()
            } else if (myArr[i].code_UE.startsWith("MDS2")) {
                getetudiantMdsNiveau2R()
            } else if (myArr[i].code_UE.startsWith("MAS")) {
                getAllEtudiantNiveau3R()
            } else if (myArr[i].code_UE.startsWith("EVE")) {
                getetudiantEVENiveau3R()
            } else if (myArr[i].code_UE.startsWith("MSO")) {
                getetudiantMSONiveau3R()
            }
            modal2.style.display = "block"
        };
    }

}

/******************************** REQUEST *************************************************************/
function getUe() {
    var xmlhttp = new XMLHttpRequest();
    var url = "http://localhost:8000/UeAPI/";

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myArr = JSON.parse(this.responseText);

            const listUe = document.getElementById("list-ue")

            for (let i = 0; i < myArr.length; i++) {
                if (myArr[i].semestre_id == 1) {
                    imgSemestrePath = "/static/bulletin/icones/number_1.png"
                } else if (myArr[i].semestre_id == 2) {
                    imgSemestrePath = "/static/bulletin/icones/number_2.png"
                } else if (myArr[i].semestre_id == 3) {
                    imgSemestrePath = "/static/bulletin/icones/number_3.png"
                } else if (myArr[i].semestre_id == 4) {
                    imgSemestrePath = "/static/bulletin/icones/four_4.png"
                } else if (myArr[i].semestre_id == 5) {
                    imgSemestrePath = "/static/bulletin/icones/five_5.png"
                } else if (myArr[i].semestre_id == 6) {
                    imgSemestrePath = "/static/bulletin/icones/number_6.png"
                }
                var imgSemestre = document.createElement('img')
                imgSemestre.setAttribute('src', imgSemestrePath)
                imgSemestre.setAttribute('alt', 'One')

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
                intituleMatiere.setAttribute('id', 'intitule-matiere')
                var UeTitle = document.createTextNode(myArr[i].intitule_UE)
                intituleMatiere.appendChild(UeTitle)

                const myBtn = document.createElement('button')
                myBtn.setAttribute('id', `myBtn${i}`)
                myBtn.setAttribute('class', 'myBtn')

                const imgbtn1 = document.createElement('img')
                let addPathImg1 = "/static/bulletin/icones/edit.png"
                imgbtn1.setAttribute("src", addPathImg1)

                const myBtn1 = document.createElement('button')
                myBtn1.setAttribute('id', `myBtn-${i}`)
                myBtn1.setAttribute('class', 'myBtn-1')
                    //myBtn1.appendChild(imgbtn1)

                const add = document.createElement('div')
                const textMessage = document.createTextNode('SN')
                add.setAttribute("id", "add")
                myBtn.appendChild(textMessage)
                add.appendChild(myBtn)

                const modify = document.createElement('div')
                const textMessage1 = document.createTextNode('SR')
                modify.setAttribute("id", "modify")
                myBtn1.appendChild(textMessage1)
                modify.appendChild(myBtn1)

                const bigBoy = document.createElement('div')
                bigBoy.setAttribute('id', `big-boy`)
                bigBoy.appendChild(add)
                bigBoy.appendChild(modify)

                const addModifyMatiere = document.createElement('div')
                addModifyMatiere.setAttribute("id", "add-modify-matiere")
                addModifyMatiere.appendChild(bigBoy)

                const matiere = document.createElement("div")
                matiere.setAttribute("class", "matiere")

                if (myArr[i].code_UE.startsWith('MDS')) {
                    matiere.classList.add('MDS')
                } else if (myArr[i].code_UE.startsWith('EPS1')) {
                    matiere.classList.add('EPS1')
                } else if (myArr[i].code_UE.startsWith('EPS2')) {
                    matiere.classList.add('EPS2')
                } else {
                    matiere.classList.add('MASEVE')
                }

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

/** REQUEST ETUDIANTS STAPS NIVEAU 1 */
function getetudiantStapsNiveau1() {

    var xmlhttp = new XMLHttpRequest();
    var url = "http://localhost:8000/etudiantStaps1/";

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myEtudiantStaps1 = JSON.parse(this.responseText);

            console.log(myEtudiantStaps1);

            //SN & CC
            /** Ajout des lignes pour insertion des notes des étudiants */
            /**Changement du TITRE Du modal */
            listeTitle = document.getElementById('listetudiant-title')
            listeTitle.innerText = `BORDOREAU DE NOTES UE --${idUe}--  Année Académique ${myEtudiantStaps1['dateExamen'][0]['annee_academique']}`

            for (let i = 0; i < myEtudiantStaps1['etudiantStaps1'].length; i++) {
                const tabledata1 = document.createElement('td')
                tabledata1.setAttribute('scope', 'row')
                tabledata1.innerText = myEtudiantStaps1['etudiantStaps1'][i]['id']

                const tabledata2 = document.createElement('td')
                tabledata2.innerText = myEtudiantStaps1['etudiantStaps1'][i]['matricule']

                var nom = myEtudiantStaps1['etudiantStaps1'][i]['nom'] + ' ' + myEtudiantStaps1['etudiantStaps1'][i]['prenom']
                const tabledata3 = document.createElement('td')
                tabledata3.innerText = nom

                const tabledata4Input = document.createElement('input')
                tabledata4Input.type = "text"
                tabledata4Input.setAttribute('placeholder', `Note CC ${myEtudiantStaps1['etudiantStaps1'][i]['nom'] + ' ' + myEtudiantStaps1['etudiantStaps1'][i]['prenom']}  ${idUe}`)
                tabledata4Input.setAttribute('name', `CC ${myEtudiantStaps1['etudiantStaps1'][i]['matricule']} ${idUe}`)
                tabledata4Input.setAttribute('id', `CC ${myEtudiantStaps1['etudiantStaps1'][i]['matricule']}${idUe}`)
                    //tabledata4Input.setAttribute('required', '')

                    Object.keys(myEtudiantStaps1['S1']["ListeNoteUeS1EPS1"][idUe]).length > 0 ? tabledata4Input.value = myEtudiantStaps1['S1']["ListeNoteUeS1EPS1"][idUe][i]['note_cc']:console.log('LE coup fonctionne');


                tabledata4Input.setAttribute('class', 'noteField')
                    //tabledata4Input

                const tabledata4 = document.createElement('td')
                tabledata4.appendChild(tabledata4Input)

                const tabledata5Input = document.createElement('input')
                tabledata5Input.type = "text"
                tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantStaps1['etudiantStaps1'][i]['matricule']} ${idUe}`)
                tabledata5Input.setAttribute('name', `SN ${myEtudiantStaps1['etudiantStaps1'][i]['matricule']} ${idUe}`)
                    //tabledata5Input.setAttribute('required', '')


                     /**TEST du contenu des UE */
                     Object.keys(myEtudiantStaps1['S1']["ListeNoteUeS1EPS1"][idUe]).length > 0 ? tabledata5Input.value = myEtudiantStaps1['S1']["ListeNoteUeS1EPS1"][idUe][i]['note_sn']:console.log('LE coup fonctionne');


                tabledata5Input.setAttribute('class', 'noteField')
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
/** REQUEST ETUDIANTS STAPS NIVEAU 1 RATTRAPAGE */
function getetudiantStapsNiveau1R() {

    //Masquage de la div SN
    modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[3].innerHTML = "Rattrapage (Rt)"
    modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[4].style.display = "none"

    myform2 = document.getElementById('modal2').children[0].children[0]
    myform2.setAttribute('id', 'myform2')
        //console.log(myForm);

    var xmlhttp = new XMLHttpRequest();
    var url = "http://localhost:8000/etudiantStaps1/";

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myEtudiantStaps1 = JSON.parse(this.responseText);

            //SN & CC
            /** Ajout des lignes pour insertion des notes des étudiants */
            /**Changement du TITRE Du modal */
            //listeTitle = document.getElementById('listetudiant-title')
            listeTitle = modal2.children[0].children[0].children[1].children[1]
            listeTitle.innerText = `BORDOREAU DE NOTES UE --${idUe}-- Année Académique ${myEtudiantStaps1['dateExamen'][0]['annee_academique']}`

            for (let i = 0; i < myEtudiantStaps1['etudiantStaps1'].length; i++) {
                const tabledata1 = document.createElement('td')
                tabledata1.setAttribute('scope', 'row')
                tabledata1.innerText = myEtudiantStaps1['etudiantStaps1'][i]['id']

                const tabledata2 = document.createElement('td')
                tabledata2.innerText = myEtudiantStaps1['etudiantStaps1'][i]['matricule']

                var nom = myEtudiantStaps1['etudiantStaps1'][i]['nom'] + ' ' + myEtudiantStaps1['etudiantStaps1'][i]['prenom']
                const tabledata3 = document.createElement('td')
                tabledata3.innerText = nom

                const tabledata4Input = document.createElement('input')
                tabledata4Input.type = "text"
                tabledata4Input.setAttribute('placeholder', `Note Rattrapage ${myEtudiantStaps1['etudiantStaps1'][i]['matricule']}  ${idUe}`)
                tabledata4Input.setAttribute('name', `Rattrapage ${myEtudiantStaps1['etudiantStaps1'][i]['matricule']} ${idUe}`)
                tabledata4Input.setAttribute('id', `Rattrapage ${myEtudiantStaps1['etudiantStaps1'][i]['matricule']}${idUe}`)
                    //tabledata4Input.setAttribute('required', '')

                    Object.keys(myEtudiantStaps1['S1']["ListeNoteUeS1EPS1R"][idUe]).length > 0 ? tabledata4Input.value = myEtudiantStaps1['S1']["ListeNoteUeS1EPS1"][idUe][i]['note_rattrapage']:console.log('LE coup fonctionne');


                tabledata4Input.setAttribute('class', 'noteField')
                    //tabledata4Input

                const tabledata4 = document.createElement('td')
                tabledata4.appendChild(tabledata4Input)

                const tabledata5Input = document.createElement('input')
                tabledata5Input.type = "text"
                tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantStaps1['etudiantStaps1'][i]['matricule']} ${idUe}`)
                tabledata5Input.setAttribute('name', `SN ${myEtudiantStaps1['etudiantStaps1'][i]['matricule']} ${idUe}`)
                tabledata5Input.setAttribute('required', '')



                tabledata5Input.setAttribute('class', 'noteField')
                const tabledata5 = document.createElement('td')
                tabledata5.appendChild(tabledata5Input)

                const ligne = document.createElement('tr')
                ligne.appendChild(tabledata1);
                ligne.appendChild(tabledata2);
                ligne.appendChild(tabledata3);
                ligne.appendChild(tabledata4);
                //ligne.appendChild(tabledata5);

                /** TBODDY du modal afin d'ajouter les étudiants par filière */
                const listStudent12 = modal2.children[0].children[0].children[2].children[0].children[0].children[1]
                listStudent12.appendChild(ligne)
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

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myEtudiantMDS1 = JSON.parse(this.responseText);

            //console.log(myEtudiantMDS1);
            //console.log(myEtudiantMDS1["etudiantMDS1"]);
            //console.log(myEtudiantMDS1[1]);

            /** Ajout des lignes pour insertion des notes des étudiants */
            /**Changement du TITRE Du modal */
            listeTitle = document.getElementById('listetudiant-title')
            listeTitle.innerText = `BORDOREAU DE NOTES UE --${idUe}-- Année Académique ${myEtudiantMDS1['dateExamen'][0]['annee_academique']}`
            tbodyMDS1 = document.getElementById('listetudiant')

            //console.log(myEtudiantMDS1['matriceUENotesMDS1']);

                for (let i = 0; i < myEtudiantMDS1['etudiantMDS1'].length/*myEtudiantMDS1.length*/; i++) {
                    const tabledata1 = document.createElement('td')
                    tabledata1.setAttribute('scope', 'row')
                    tabledata1.innerText = myEtudiantMDS1['etudiantMDS1'][i]['id']//myEtudiantMDS1[0][i].id
    
                    const tabledata2 = document.createElement('td')
                    tabledata2.innerText = myEtudiantMDS1['etudiantMDS1'][i]['matricule']//myEtudiantMDS1[i].matricule
    
                    var nom = myEtudiantMDS1['etudiantMDS1'][i]['nom']/*myEtudiantMDS1[i].nom*/ + ' ' + myEtudiantMDS1['etudiantMDS1'][i]['prenom']/*myEtudiantMDS1[i].prenom*/
                    const tabledata3 = document.createElement('td')
                    tabledata3.innerText = nom
    
                    const tabledata4Input = document.createElement('input')
                    tabledata4Input.type = "text"
    
                    tabledata4Input.setAttribute('placeholder', `Note CC ${myEtudiantMDS1['etudiantMDS1'][i]['matricule'] /*myEtudiantMDS1[i].matricule*/}  ${idUe}`)
                    tabledata4Input.setAttribute('name', `CC ${myEtudiantMDS1['etudiantMDS1'][i]['matricule']/*myEtudiantMDS1[i].matricule*/} ${idUe}`)
                    //tabledata4Input.setAttribute('id', `CC ${myEtudiantMDS1['etudiantMDS1'][i]['matricule']/*myEtudiantMDS1[i].matricule*/} ${idUe}`)
                        //tabledata4Input.setAttribute('required', '');

                        Object.keys(myEtudiantMDS1['matriceUENotesMDS1'][idUe][0]).length > 0 ?tabledata4Input.value =  myEtudiantMDS1['matriceUENotesMDS1'][idUe][0][i]["note_cc"]:

                    //tabledata4Input.value = myEtudiantMDS1['matriceUENotesMDS1'][idUe][0][i]["note_cc"]//'alpha'


                    tabledata4Input.setAttribute('class', 'noteField')

                    const tabledata4 = document.createElement('td')
                    tabledata4.appendChild(tabledata4Input)
    
                    const tabledata5Input = document.createElement('input')
                    tabledata5Input.type = "text"
                    tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantMDS1['etudiantMDS1'][i]['matricule']/*myEtudiantMDS1[i].matricule*/} ${idUe}`)
                    tabledata5Input.setAttribute('name', `SN ${myEtudiantMDS1['etudiantMDS1'][i]['matricule']/*myEtudiantMDS1[i].matricule*/} ${idUe}`)
                        //tabledata5Input.setAttribute('required','');
                        Object.keys(myEtudiantMDS1['matriceUENotesMDS1'][idUe][0]).length > 0 ?tabledata5Input.value =  myEtudiantMDS1['matriceUENotesMDS1'][idUe][0][i]["note_sn"]:

                    tabledata5Input.setAttribute('class', 'noteField')
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
/** REQUEST ETUDIANTS MDS NIVEAU 1 RATTRAPAGE */
function getetudiantMDSNiveau1R() {

    //Masquage de la div SN
    modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[3].innerHTML = "Rattrapage (Rt)"
    modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[4].style.display = "none"

    myform2 = document.getElementById('modal2').children[0].children[0]


    var xmlhttp = new XMLHttpRequest();
    var url = "http://localhost:8000/etudiantMDS1/";

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myEtudiantMDS1 = JSON.parse(this.responseText);

            console.log(myEtudiantMDS1);

            /** Ajout des lignes pour insertion des notes des étudiants */
            /**Changement du TITRE Du modal */
            //listeTitle = document.getElementById('listetudiant-title')
            listeTitle = modal2.children[0].children[0].children[1].children[1]

            listeTitle.innerText = `BORDOREAU DE NOTES UE --${idUe}-- Année Académique ${myEtudiantMDS1['dateExamen'][0]['annee_academique']}`

            tbodyMDS1 = document.getElementById('listetudiant')

            //let test = ( Object.keys(myEtudiantMDS1['matriceUENotesMDS1']).length === 0 )

                for (let i = 0; i < myEtudiantMDS1['etudiantMDS1'].length/*myEtudiantMDS1.length*/; i++) {
                    console.log("OK OK");
                    const tabledata1 = document.createElement('td')
                    tabledata1.innerText = myEtudiantMDS1['etudiantMDS1'][i]['id']//myEtudiantMDS1[i].id

                    const tabledata2 = document.createElement('td')
                    tabledata2.innerText = myEtudiantMDS1['etudiantMDS1'][i]['matricule']//myEtudiantMDS1[i].matricule

                    var nom = myEtudiantMDS1['etudiantMDS1'][i]['nom']/*myEtudiantMDS1[i].nom*/ + ' ' + myEtudiantMDS1['etudiantMDS1'][i]['prenom']/*myEtudiantMDS1[i].prenom*/
                    const tabledata3 = document.createElement('td')
                    tabledata3.innerText = nom

                    const tabledata4Input = document.createElement('input')
                    tabledata4Input.type = "text"
                    tabledata4Input.setAttribute('placeholder', `Note Rattrapage ${myEtudiantMDS1['etudiantMDS1'][i]['matricule'] /*myEtudiantMDS1[i].matricule*/} ${idUe}`)
                    tabledata4Input.setAttribute('name', `Rattrapage ${myEtudiantMDS1['etudiantMDS1'][i]['matricule']} ${idUe}`)
                    tabledata4Input.setAttribute('id', `Rattrapage ${myEtudiantMDS1['etudiantMDS1'][i]['matricule']}${idUe}`)
                        //tabledata4Input.setAttribute('required', '')

                        /**TEST du contenu des UE */
                        Object.keys(myEtudiantMDS1['matriceUENotesMDS1R'][idUe][0]).length > 0 ? tabledata4Input.value = myEtudiantMDS1['matriceUENotesMDS1R'][idUe][0][i]['note_rattrapage']:console.log('LE coup fonctionne');

                    tabledata4Input.setAttribute('class', 'noteField')
                        //tabledata4Input

                    const tabledata4 = document.createElement('td')
                    tabledata4.appendChild(tabledata4Input)

                    const tabledata5Input = document.createElement('input')
                    tabledata5Input.type = "text"
                    tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantMDS1['etudiantMDS1'][i]['matricule']} ${idUe}`)
                    tabledata5Input.setAttribute('name', `SN ${myEtudiantMDS1['etudiantMDS1'][i]['matricule']} ${idUe}`)
                        //tabledata5Input.setAttribute('required','');

                        
                    tabledata5Input.setAttribute('class', 'noteField')
                    
                    

                    const tabledata5 = document.createElement('td')
                    tabledata5.appendChild(tabledata5Input)

                    

                    const ligne = document.createElement('tr')
                    ligne.appendChild(tabledata1);
                    ligne.appendChild(tabledata2);
                    ligne.appendChild(tabledata3);
                    ligne.appendChild(tabledata4);
                    //ligne.appendChild(tabledata5);

                    /** TBODDY du modal afin d'ajouter les étudiants par filière */
                    /*const listStudent = document.getElementById('listetudiant')
                    listStudent.appendChild(ligne)*/
                    const listStudent12 = modal2.children[0].children[0].children[2].children[0].children[0].children[1]
                    listStudent12.appendChild(ligne)
            }

        }
    }
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
    }




    /**  REQUEST ETUDIANT STAPS NIVEAU 2 */
    function getetudiantStapsNiveau2() {
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

            listeTitle.innerText = `BORDOREAU DE NOTES UE --${idUe}-- ANNEE 202X-202X`

            for (let i = 0; i < myEtudiantStaps2.length; i++) {
                const tabledata1 = document.createElement('td')
                tabledata1.setAttribute('scope', 'row')
                tabledata1.innerText = myEtudiantStaps2[i].id

                const tabledata2 = document.createElement('td')
                tabledata2.innerText = myEtudiantStaps2[i].matricule

                var nom = myEtudiantStaps2[i].nom + ' ' + myEtudiantStaps2[i].prenom
                const tabledata3 = document.createElement('td')
                tabledata3.innerText = nom

                const tabledata4Input = document.createElement('input')
                tabledata4Input.type = "text"
                tabledata4Input.setAttribute('placeholder', `Note CC ${myEtudiantStaps2[i].matricule}  ${idUe}`)
                tabledata4Input.setAttribute('name', `CC ${myEtudiantStaps2[i].matricule} ${idUe}`)
                tabledata4Input.setAttribute('id', `CC ${myEtudiantStaps2[i].matricule} ${idUe}`)
                    //tabledata4Input.setAttribute('required','')
                tabledata4Input.setAttribute('class', 'noteField')

                const tabledata4 = document.createElement('td')
                tabledata4.appendChild(tabledata4Input)

                const tabledata5Input = document.createElement('input')
                tabledata5Input.type = "text"
                tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantStaps2[i].matricule} ${idUe}`)
                tabledata5Input.setAttribute('name', `SN ${myEtudiantStaps2[i].matricule} ${idUe}`)
                    //tabledata5Input.setAttribute('required','');
                tabledata5Input.setAttribute('class', 'noteField')
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
    /**  REQUEST ETUDIANT STAPS NIVEAU 2 RATTRAPAGE */
    function getetudiantStapsNiveau2R() {

    //Masquage de la div SN
    modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[3].innerHTML = "Rattrapage (Rt)"
    modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[4].style.display = "none"

    myform2 = document.getElementById('modal2').children[0].children[0]


    var xmlhttp = new XMLHttpRequest();
    var url = "http://localhost:8000/etudiantStaps2/";

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myEtudiantStaps2 = JSON.parse(this.responseText);

            /** Ajout des lignes pour insertion des notes des étudiants */
            /**Changement du TITRE Du modal */
            //listeTitle = document.getElementById('listetudiant-title')
            //console.log(listeTitle);
            //listeTitle.innerHTML=""
            listeTitle = modal2.children[0].children[0].children[1].children[1]

            listeTitle.innerText = `BORDOREAU DE NOTES UE --${idUe}-- ANNEE 202X-202X`

            //tbodyMDS1 = document.getElementById('listetudiant')

            for (let i = 0; i < myEtudiantStaps2.length; i++) {
                const tabledata1 = document.createElement('td')
                tabledata1.setAttribute('scope', 'row')
                tabledata1.innerText = myEtudiantStaps2[i].id

                const tabledata2 = document.createElement('td')
                tabledata2.innerText = myEtudiantStaps2[i].matricule

                var nom = myEtudiantStaps2[i].nom + ' ' + myEtudiantStaps2[i].prenom
                const tabledata3 = document.createElement('td')
                tabledata3.innerText = nom

                const tabledata4Input = document.createElement('input')
                tabledata4Input.type = "text"
                tabledata4Input.setAttribute('placeholder', `Note Rattrapage ${myEtudiantStaps2[i].matricule}  ${idUe}`)
                tabledata4Input.setAttribute('name', `Rattrapage ${myEtudiantStaps2[i].matricule} ${idUe}`)
                tabledata4Input.setAttribute('id', `Rattrapage ${myEtudiantStaps2[i].matricule}${idUe}`)
                    //tabledata4Input.setAttribute('required', '')
                tabledata4Input.setAttribute('class', 'noteField')

                const tabledata4 = document.createElement('td')
                tabledata4.appendChild(tabledata4Input)

                const tabledata5Input = document.createElement('input')
                tabledata5Input.type = "text"
                tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantStaps2[i].matricule} ${idUe}`)
                tabledata5Input.setAttribute('name', `SN ${myEtudiantStaps2[i].matricule} ${idUe}`)
                    //tabledata5Input.setAttribute('required','');
                tabledata5Input.setAttribute('class', 'noteField')
                const tabledata5 = document.createElement('td')
                tabledata5.appendChild(tabledata5Input)

                const ligne = document.createElement('tr')
                ligne.appendChild(tabledata1);
                ligne.appendChild(tabledata2);
                ligne.appendChild(tabledata3);
                ligne.appendChild(tabledata4);
                //ligne.appendChild(tabledata5);


                /** TBODDY du modal afin d'ajouter les étudiants par filière */
                //const listStudent = document.getElementById('listetudiant')

                const listStudent12 = modal2.children[0].children[0].children[2].children[0].children[0].children[1]
                listStudent12.appendChild(ligne)
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

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myEtudiantMds2 = JSON.parse(this.responseText);

            /** Ajout des lignes pour insertion des notes des étudiants */
            /**Changement du TITRE Du modal */
            listeTitle = document.getElementById('listetudiant-title')
                //console.log(listeTitle);
                //listeTitle.innerHTML=""

            listeTitle.innerText = `BORDOREAU DE NOTES UE --${idUe}-- Année Académique ${myEtudiantMds2['dateExamen'][0]['annee_academique']}`

            for (let i = 0; i < myEtudiantMds2['etudiantMDS2'].length; i++) {
                const tabledata1 = document.createElement('td')
                tabledata1.setAttribute('scope', 'row')
                tabledata1.innerText = myEtudiantMds2['etudiantMDS2'][i]['id']//myEtudiantMds2[i].id

                const tabledata2 = document.createElement('td')
                tabledata2.innerText = myEtudiantMds2['etudiantMDS2'][i]['matricule']//myEtudiantMds2[i].matricule

                var nom = myEtudiantMds2['etudiantMDS2'][i]['nom']/*myEtudiantMDS1[i].nom*/ + ' ' + myEtudiantMds2['etudiantMDS2'][i]['prenom']/*myEtudiantMDS1[i].prenom*/
                const tabledata3 = document.createElement('td')
                tabledata3.innerText = nom

                const tabledata4Input = document.createElement('input')
                tabledata4Input.type = "text"
                tabledata4Input.setAttribute('placeholder', `Note CC ${myEtudiantMds2['etudiantMDS2'][i]['matricule']}  ${idUe}`)
                tabledata4Input.setAttribute('name', `CC ${myEtudiantMds2['etudiantMDS2'][i]['matricule']} ${idUe}`)
                tabledata4Input.setAttribute('id', `CC ${myEtudiantMds2['etudiantMDS2'][i]['matricule']} ${idUe}`)
                    //tabledata4Input.setAttribute('required','')

                    Object.keys(myEtudiantMds2['matriceUENotesMDS2'][idUe][0]).length > 0 ?tabledata4Input.value =  myEtudiantMds2['matriceUENotesMDS2'][idUe][0][i]["note_cc"]:

                tabledata4Input.setAttribute('class', 'noteField')

                const tabledata4 = document.createElement('td')
                tabledata4.appendChild(tabledata4Input)

                const tabledata5Input = document.createElement('input')
                tabledata5Input.type = "text"
                tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantMds2['etudiantMDS2'][i]['matricule']} ${idUe}`)
                tabledata5Input.setAttribute('name', `SN ${myEtudiantMds2['etudiantMDS2'][i]['matricule']} ${idUe}`)
                    //tabledata5Input.setAttribute('required','');

                    Object.keys(myEtudiantMds2['matriceUENotesMDS2'][idUe][0]).length > 0 ?tabledata5Input.value =  myEtudiantMds2['matriceUENotesMDS2'][idUe][0][i]["note_sn"]:

                tabledata5Input.setAttribute('class', 'noteField')
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
/**  REQUEST ETUDIANT MDS NIVEAU 2 RATTRAPAGE */
function getetudiantMdsNiveau2R() {

    //Masquage de la div SN
    modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[3].innerHTML = "Rattrapage (Rt)"
    modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[4].style.display = "none"

    myform2 = document.getElementById('modal2').children[0].children[0]


    var xmlhttp = new XMLHttpRequest();
    var url = "http://localhost:8000/etudiantMds2/";

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myEtudiantMds2 = JSON.parse(this.responseText);

            /** Ajout des lignes pour insertion des notes des étudiants */
            /**Changement du TITRE Du modal */
            //listeTitle = document.getElementById('listetudiant-title')
            //console.log(listeTitle);
            //listeTitle.innerHTML=""
            listeTitle = modal2.children[0].children[0].children[1].children[1]

            listeTitle.innerText = `BORDOREAU DE NOTES UE --${idUe}-- Année Académique ${myEtudiantMds2['dateExamen'][0]['annee_academique']}`

            //tbodyMDS1 = document.getElementById('listetudiant')

            for (let i = 0; i < myEtudiantMds2['etudiantMDS2'].length; i++) {
                const tabledata1 = document.createElement('td')
                tabledata1.setAttribute('scope', 'row')
                tabledata1.innerText = myEtudiantMds2['etudiantMDS2'][i]['id']//myEtudiantMds2[i].id

                const tabledata2 = document.createElement('td')
                tabledata2.innerText = myEtudiantMds2['etudiantMDS2'][i]['matricule']//myEtudiantMds2[i].matricule

                var nom = myEtudiantMds2['etudiantMDS2'][i]['nom']/*myEtudiantMDS1[i].nom*/ + ' ' + myEtudiantMds2['etudiantMDS2'][i]['prenom']/*myEtudiantMDS1[i].prenom*/
                const tabledata3 = document.createElement('td')
                tabledata3.innerText = nom

                const tabledata4Input = document.createElement('input')
                tabledata4Input.type = "text"
                tabledata4Input.setAttribute('placeholder', `Note Rattrapage ${myEtudiantMds2['etudiantMDS2'][i]['matricule']}  ${idUe}`)
                tabledata4Input.setAttribute('name', `Rattrapage ${myEtudiantMds2['etudiantMDS2'][i]['matricule']} ${idUe}`)
                tabledata4Input.setAttribute('id', `Rattrapage ${myEtudiantMds2['etudiantMDS2'][i]['matricule']}${idUe}`)
                    //tabledata4Input.setAttribute('required', '')

                    Object.keys(myEtudiantMds2['matriceUENotesMDS2R'][idUe][0]).length > 0 ? tabledata4Input.value = myEtudiantMds2['matriceUENotesMDS2R'][idUe][0][i]['note_rattrapage']:console.log('LE coup fonctionne');


                tabledata4Input.setAttribute('class', 'noteField')

                const tabledata4 = document.createElement('td')
                tabledata4.appendChild(tabledata4Input)

                const tabledata5Input = document.createElement('input')
                tabledata5Input.type = "text"
                tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantMds2['etudiantMDS2'][i]['matricule']} ${idUe}`)
                tabledata5Input.setAttribute('name', `SN ${myEtudiantMds2['etudiantMDS2'][i]['matricule']} ${idUe}`)
                    //tabledata5Input.setAttribute('required','');

                tabledata5Input.setAttribute('class', 'noteField')

                const tabledata5 = document.createElement('td')
                tabledata5.appendChild(tabledata5Input)

                const ligne = document.createElement('tr')
                ligne.appendChild(tabledata1);
                ligne.appendChild(tabledata2);
                ligne.appendChild(tabledata3);
                ligne.appendChild(tabledata4);
                //ligne.appendChild(tabledata5);


                /** TBODDY du modal afin d'ajouter les étudiants par filière */
                //const listStudent = document.getElementById('listetudiant')

                const listStudent12 = modal2.children[0].children[0].children[2].children[0].children[0].children[1]
                listStudent12.appendChild(ligne)
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

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myEtudiantNiveau3 = JSON.parse(this.responseText);

            /** Ajout des lignes pour insertion des notes des étudiants */
            /**Changement du TITRE Du modal */
            listeTitle = document.getElementById('listetudiant-title')
            listeTitle.innerText = `BORDOREAU DE NOTES UE --${idUe}-- ANNEE 202X-202X`

            for (let i = 0; i < myEtudiantNiveau3.length; i++) {
                const tabledata1 = document.createElement('td')
                tabledata1.setAttribute('scope', 'row')
                tabledata1.innerText = myEtudiantNiveau3[i].id

                const tabledata2 = document.createElement('td')
                tabledata2.innerText = myEtudiantNiveau3[i].matricule

                var nom = myEtudiantNiveau3[i].nom + ' ' + myEtudiantNiveau3[i].prenom
                const tabledata3 = document.createElement('td')
                tabledata3.innerText = nom

                const tabledata4Input = document.createElement('input')
                tabledata4Input.type = "text"
                    //console.log(element.parentElement.parentElement.parentElement.parentElement.children[0].innerText);
                tabledata4Input.setAttribute('placeholder', `Note CC ${myEtudiantNiveau3[i].matricule}  ${idUe}`)
                tabledata4Input.setAttribute('name', `CC ${myEtudiantNiveau3[i].matricule} ${idUe}`)
                tabledata4Input.setAttribute('id', `CC ${myEtudiantNiveau3[i].matricule} ${idUe}`)
                    //tabledata4Input.setAttribute('required','')
                tabledata4Input.setAttribute('class', 'noteField')

                const tabledata4 = document.createElement('td')
                tabledata4.appendChild(tabledata4Input)

                const tabledata5Input = document.createElement('input')
                tabledata5Input.type = "text"
                tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantNiveau3[i].matricule} ${idUe}`)
                tabledata5Input.setAttribute('name', `SN ${myEtudiantNiveau3[i].matricule} ${idUe}`)
                    //tabledata5Input.setAttribute('required', '');
                tabledata5Input.setAttribute('class', 'noteField')
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
/**REQUEST ETUDIANT NIVEAU 3 RATTRAPAGE */
function getAllEtudiantNiveau3R() {

    //Masquage de la div SN
    modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[3].innerHTML = "Rattrapage (Rt)"
    modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[4].style.display = "none"

    myform2 = document.getElementById('modal2').children[0].children[0]

    var xmlhttp = new XMLHttpRequest();
    var url = "http://localhost:8000/etudiantNiveau3/";

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myEtudiantNiveau3 = JSON.parse(this.responseText);

            /** Ajout des lignes pour insertion des notes des étudiants */
            /**Changement du TITRE Du modal */
            //listeTitle = document.getElementById('listetudiant-title')
            listeTitle = modal2.children[0].children[0].children[1].children[1]
            listeTitle.innerText = `BORDOREAU DE NOTES UE --${idUe}-- ANNEE 202X-202X`

            for (let i = 0; i < myEtudiantNiveau3.length; i++) {
                const tabledata1 = document.createElement('td')
                tabledata1.setAttribute('scope', 'row')
                tabledata1.innerText = myEtudiantNiveau3[i].id

                const tabledata2 = document.createElement('td')
                tabledata2.innerText = myEtudiantNiveau3[i].matricule

                var nom = myEtudiantNiveau3[i].nom + ' ' + myEtudiantNiveau3[i].prenom
                const tabledata3 = document.createElement('td')
                tabledata3.innerText = nom

                const tabledata4Input = document.createElement('input')
                tabledata4Input.type = "text"
                tabledata4Input.setAttribute('placeholder', `Note Rattrapage ${myEtudiantNiveau3[i].matricule}  ${idUe}`)
                tabledata4Input.setAttribute('name', `Rattrapage ${myEtudiantNiveau3[i].matricule} ${idUe}`)
                tabledata4Input.setAttribute('id', `Rattrapage ${myEtudiantNiveau3[i].matricule}${idUe}`)
                    //tabledata4Input.setAttribute('required', '')
                tabledata4Input.setAttribute('class', 'noteField')

                const tabledata4 = document.createElement('td')
                tabledata4.appendChild(tabledata4Input)

                const tabledata5Input = document.createElement('input')
                tabledata5Input.type = "text"
                tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantNiveau3[i].matricule} ${idUe}`)
                tabledata5Input.setAttribute('name', `SN ${myEtudiantNiveau3[i].matricule} ${idUe}`)
                    //tabledata5Input.setAttribute('required', '');
                tabledata5Input.setAttribute('class', 'noteField')
                const tabledata5 = document.createElement('td')
                tabledata5.appendChild(tabledata5Input)

                const ligne = document.createElement('tr')
                ligne.appendChild(tabledata1);
                ligne.appendChild(tabledata2);
                ligne.appendChild(tabledata3);
                ligne.appendChild(tabledata4);
                //ligne.appendChild(tabledata5);


                /** TBODDY du modal afin d'ajouter les étudiants par filière */
                //const listStudent = document.getElementById('listetudiant')
                //listStudent.appendChild(ligne)
                const listStudent12 = modal2.children[0].children[0].children[2].children[0].children[0].children[1]
                listStudent12.appendChild(ligne)
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

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myEtudiantNiveau3EVE = JSON.parse(this.responseText);

            /** Ajout des lignes pour insertion des notes des étudiants */
            /**Changement du TITRE Du modal */
            //listeTitle = document.getElementById('listetudiant-title')
            listeTitle = modal2.children[0].children[0].children[1].children[1]
            listeTitle.innerText = `BORDOREAU DE NOTES UE --${idUe}-- ANNEE 202X-202X`

            for (let i = 0; i < myEtudiantNiveau3EVE.length; i++) {
                const tabledata1 = document.createElement('td')
                tabledata1.setAttribute('scope', 'row')
                tabledata1.innerText = myEtudiantNiveau3EVE[i].id

                const tabledata2 = document.createElement('td')
                tabledata2.innerText = myEtudiantNiveau3EVE[i].matricule

                var nom = myEtudiantNiveau3EVE[i].nom + ' ' + myEtudiantNiveau3EVE[i].prenom
                const tabledata3 = document.createElement('td')
                tabledata3.innerText = nom

                const tabledata4Input = document.createElement('input')
                tabledata4Input.type = "text"
                tabledata4Input.setAttribute('placeholder', `Note CC ${myEtudiantNiveau3EVE[i].matricule}  ${idUe}`)
                tabledata4Input.setAttribute('name', `CC ${myEtudiantNiveau3EVE[i].matricule} ${idUe}`)
                tabledata4Input.setAttribute('id', `CC ${myEtudiantNiveau3EVE[i].matricule}${idUe}`)
                    //tabledata4Input.setAttribute('required', '')
                tabledata4Input.setAttribute('class', 'noteField')
                    //tabledata4Input

                const tabledata4 = document.createElement('td')
                tabledata4.appendChild(tabledata4Input)

                const tabledata5Input = document.createElement('input')
                tabledata5Input.type = "text"
                tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantNiveau3EVE[i].matricule} ${idUe}`)
                tabledata5Input.setAttribute('name', `SN ${myEtudiantNiveau3EVE[i].matricule} ${idUe}`)
                    //tabledata5Input.setAttribute('required','');
                tabledata5Input.setAttribute('class', 'noteField')
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
/** REQUEST ETUDIANTS EVE RATTRAPAGE */
function getetudiantEVENiveau3R() {

    //Masquage de la div SN
    modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[3].innerHTML = "Rattrapage (Rt)"
    modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[4].style.display = "none"

    myform2 = document.getElementById('modal2').children[0].children[0]

    var xmlhttp = new XMLHttpRequest();
    var url = "http://localhost:8000/etudiantNiveau3EVE/";

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myEtudiantNiveau3EVE = JSON.parse(this.responseText);

            /** Ajout des lignes pour insertion des notes des étudiants */
            /**Changement du TITRE Du modal */
            //listeTitle = document.getElementById('listetudiant-title')
            listeTitle = modal2.children[0].children[0].children[1].children[1]
            listeTitle.innerText = `BORDOREAU DE NOTES UE --${idUe}-- ANNEE 202X-202X`

            for (let i = 0; i < myEtudiantNiveau3EVE.length; i++) {
                const tabledata1 = document.createElement('td')
                tabledata1.setAttribute('scope', 'row')
                tabledata1.innerText = myEtudiantNiveau3EVE[i].id

                const tabledata2 = document.createElement('td')
                tabledata2.innerText = myEtudiantNiveau3EVE[i].matricule

                var nom = myEtudiantNiveau3EVE[i].nom + ' ' + myEtudiantNiveau3EVE[i].prenom
                const tabledata3 = document.createElement('td')
                tabledata3.innerText = nom

                const tabledata4Input = document.createElement('input')
                tabledata4Input.type = "text"
                tabledata4Input.setAttribute('placeholder', `Note Rattrapage ${myEtudiantNiveau3EVE[i].matricule}  ${idUe}`)
                tabledata4Input.setAttribute('name', `Rattrapage ${myEtudiantNiveau3EVE[i].matricule} ${idUe}`)
                tabledata4Input.setAttribute('id', `Rattrapage ${myEtudiantNiveau3EVE[i].matricule}${idUe}`)
                    //tabledata4Input.setAttribute('required', '')
                tabledata4Input.setAttribute('class', 'noteField')
                    //tabledata4Input

                const tabledata4 = document.createElement('td')
                tabledata4.appendChild(tabledata4Input)

                const tabledata5Input = document.createElement('input')
                tabledata5Input.type = "text"
                tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantNiveau3EVE[i].matricule} ${idUe}`)
                tabledata5Input.setAttribute('name', `SN ${myEtudiantNiveau3EVE[i].matricule} ${idUe}`)
                    //tabledata5Input.setAttribute('required','');
                tabledata5Input.setAttribute('class', 'noteField')
                const tabledata5 = document.createElement('td')
                tabledata5.appendChild(tabledata5Input)

                const ligne = document.createElement('tr')
                ligne.appendChild(tabledata1);
                ligne.appendChild(tabledata2);
                ligne.appendChild(tabledata3);
                ligne.appendChild(tabledata4);
                //ligne.appendChild(tabledata5);

                /** TBODDY du modal afin d'ajouter les étudiants par filière */
                //const listStudent = document.getElementById('listetudiant')
                //listStudent.appendChild(ligne)
                const listStudent12 = modal2.children[0].children[0].children[2].children[0].children[0].children[1]
                listStudent12.appendChild(ligne)
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

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myEtudiantNiveau3MSO = JSON.parse(this.responseText);

            /** Ajout des lignes pour insertion des notes des étudiants */
            /**Changement du TITRE Du modal */
            listeTitle = document.getElementById('listetudiant-title')
            listeTitle.innerText = `BORDOREAU DE NOTES UE --${idUe}-- ANNEE 202X-202X`

            for (let i = 0; i < myEtudiantNiveau3MSO.length; i++) {
                const tabledata1 = document.createElement('td')
                tabledata1.setAttribute('scope', 'row')
                tabledata1.innerText = myEtudiantNiveau3MSO[i].id

                const tabledata2 = document.createElement('td')
                tabledata2.innerText = myEtudiantNiveau3MSO[i].matricule

                var nom = myEtudiantNiveau3MSO[i].nom + ' ' + myEtudiantNiveau3MSO[i].prenom
                const tabledata3 = document.createElement('td')
                tabledata3.innerText = nom

                const tabledata4Input = document.createElement('input')
                tabledata4Input.type = "text"
                    //console.log(element.parentElement.parentElement.parentElement.parentElement.children[0].innerText);
                tabledata4Input.setAttribute('placeholder', `Note CC ${myEtudiantNiveau3MSO[i].matricule}  ${idUe}`)
                tabledata4Input.setAttribute('name', `CC ${myEtudiantNiveau3MSO[i].matricule} ${idUe}`)
                tabledata4Input.setAttribute('id', `CC ${myEtudiantNiveau3MSO[i].matricule} ${idUe}`)
                    //tabledata4Input.setAttribute('required', '')
                tabledata4Input.setAttribute('class', 'noteField')

                const tabledata4 = document.createElement('td')
                tabledata4.appendChild(tabledata4Input)

                const tabledata5Input = document.createElement('input')
                tabledata5Input.type = "text"
                tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantNiveau3MSO[i].matricule} ${idUe}`)
                tabledata5Input.setAttribute('name', `SN ${myEtudiantNiveau3MSO[i].matricule} ${idUe}`)
                    //tabledata5Input.setAttribute('required', '')
                tabledata5Input.setAttribute('class', 'noteField')
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
/** REQUEST ETUDIANTS MSO RATTRAPAGE */
function getetudiantMSONiveau3R() {

    //Masquage de la div SN
    modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[3].innerHTML = "Rattrapage (Rt)"
    modal2.children[0].children[0].children[2].children[0].children[0].children[0].children[0].children[4].style.display = "none"

    myform2 = document.getElementById('modal2').children[0].children[0]
    myform2.setAttribute('id', 'myform2')


    var xmlhttp = new XMLHttpRequest();
    var url = "http://localhost:8000/etudiantNiveau3MSO/";

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myEtudiantNiveau3MSO = JSON.parse(this.responseText);

            /** Ajout des lignes pour insertion des notes des étudiants */
            /**Changement du TITRE Du modal */
            listeTitle = document.getElementById('listetudiant-title')
            listeTitle.innerText = `BORDOREAU DE NOTES UE --${idUe}-- ANNEE 202X-202X`

            for (let i = 0; i < myEtudiantNiveau3MSO.length; i++) {
                const tabledata1 = document.createElement('td')
                tabledata1.setAttribute('scope', 'row')
                tabledata1.innerText = myEtudiantNiveau3MSO[i].id

                const tabledata2 = document.createElement('td')
                tabledata2.innerText = myEtudiantNiveau3MSO[i].matricule

                var nom = myEtudiantNiveau3MSO[i].nom + ' ' + myEtudiantNiveau3MSO[i].prenom
                const tabledata3 = document.createElement('td')
                tabledata3.innerText = nom

                const tabledata4Input = document.createElement('input')
                tabledata4Input.type = "text"
                tabledata4Input.setAttribute('placeholder', `Note Rattrapage ${myEtudiantNiveau3MSO[i].matricule}  ${idUe}`)
                tabledata4Input.setAttribute('name', `Rattrapage ${myEtudiantNiveau3MSO[i].matricule} ${idUe}`)
                tabledata4Input.setAttribute('id', `Rattrapage ${myEtudiantNiveau3MSO[i].matricule}${idUe}`)
                    //tabledata4Input.setAttribute('required', '')
                tabledata4Input.setAttribute('class', 'noteField')

                const tabledata4 = document.createElement('td')
                tabledata4.appendChild(tabledata4Input)

                const tabledata5Input = document.createElement('input')
                tabledata5Input.type = "text"
                tabledata5Input.setAttribute('placeholder', `Note SN ${myEtudiantNiveau3MSO[i].matricule} ${idUe}`)
                tabledata5Input.setAttribute('name', `SN ${myEtudiantNiveau3MSO[i].matricule} ${idUe}`)
                    //tabledata5Input.setAttribute('required', '')
                tabledata5Input.setAttribute('class', 'noteField')
                const tabledata5 = document.createElement('td')
                tabledata5.appendChild(tabledata5Input)

                const ligne = document.createElement('tr')
                ligne.appendChild(tabledata1);
                ligne.appendChild(tabledata2);
                ligne.appendChild(tabledata3);
                ligne.appendChild(tabledata4);
                //ligne.appendChild(tabledata5);

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
    dataString1 = $("#myForm").serializeArray()
    options1 = {
            //data : dataString,
            //target:"",
            url: 'ajoutNoteEtudiant/',
            type: "POST",
            success: "",
        }
        /**Validation par classe */
    jQuery.validator.addClassRules("noteField", {
        required: true,
    });

    $("#myForm").submit(function(e) {
        e.preventDefault();

        console.log('OK');

    }).validate({
        submitHandler: function(form) {

            $("#myForm").ajaxSubmit(options1)
            tbodylistStudent.innerHTML = ""

            modal.style.display = "none";
            alert(`LES NOTES ONT ETE ENREGISTREES AVEC SUCCESS`)
        }
    });
})

/** SEND DATA TO THE SERVER */ //RATTRAPAGE
$(function Rattrapage() {
    dataString = $("#myform2").serializeArray()
    options = {
            //data : dataString,
            //target:"",
            url: 'ajoutNoteEtudiantRattrapage/',
            type: "POST",
            success: "",
        }
        /**Validation par classe */
    jQuery.validator.addClassRules("noteField", {
        required: true,
    });

    $("#myform2").submit(function(e) {
        e.preventDefault();
    }).validate({
        submitHandler: function() {
            $("#myform2").ajaxSubmit(options)
            modal2.children[0].children[0].children[2].children[0].children[0].children[1].innerHTML = ""
                //tbodylistStudent2.innerHTML = ""

            modal2.style.display = "none";
            alert(`LES NOTES ONT ETE ENREGISTREES AVEC SUCCESS`)
        }
    });
})