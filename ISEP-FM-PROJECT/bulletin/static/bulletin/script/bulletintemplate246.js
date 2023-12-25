//import  BullSTAPS1 from  './BulletinTemplate246Function/BullSTAPS1.js';
//import  BullSTAPS2 from  '../BulletinTemplate246Function/BullSTAPS2.js';

window.addEventListener('load', () => {
    

    //Recuperation de la variable des données
    var mydata = JSON.parse(document.getElementById('semestre1MDS').textContent);
    console.log(mydata)

    //Génération dynamique du tableau de bulletin
    //TEST GENERAL POUR TOUS LES BULLETINS SEMESTRE  1(EPS1 & MDS1) 3(EPS2) 5(EVE)S

    body = document.getElementById('body')

    if (mydata[0] == 'GESTION') {
        moY = []
        containerrr = GenerateBullMDS1Semestre1()
        listcontainer = document.createElement('div')
        for (i = 0; i < mydata[1].length; i++) {
            clone = containerrr.cloneNode(true);
            //Execution des traitements sur container
            clone = BullMDS1(clone, i, mydata)

            /**MOYENNE */
            moY[i] = globalThis.resultat.children[3].innerHTML
                //console.log(moY);

            //Puis ajout au containerList
            listcontainer.appendChild(clone)
        }
        //Fixation de ContainerList sur le body de la page
        body.appendChild(listcontainer)
            /*moY = stringToIntArray(moY)
            moy = triDecroissant(moY)
            console.log(moy);*/
    } else if (mydata[0] == 'STAPS1') {
        containeer = GenerateBullStaps1Semestre1()
        listcontainer = document.createElement('div')
        for (i = 0; i < mydata[1].length; i++) {
            clone = containeer.cloneNode(true);
            //Execution des traitements sur container
            clone = BullSTAPS1(clone, i, mydata)
                //Puis ajout au containerList
            listcontainer.appendChild(clone)
        }
        //Fixation de ContainerList sur le body de la page
        body.appendChild(listcontainer)
    } else if (mydata[0] == 'STAPS2') {
        body = document.getElementById('body')
        var containeer = GenerateBullStaps2Semestre3()
        var listcontainer = document.createElement('div')
        for (var i = 0; i < mydata[1].length; i++) {
            var clone = containeer.cloneNode(true);
            //Execution des traitements sur container
            clone = BullSTAPS2(clone, i, mydata)
                //Puis ajout au containerList
            listcontainer.appendChild(clone)
        }
        //Fixation de ContainerList sur le body de la page
        body.appendChild(listcontainer)
    } else if (mydata[0] == 'EVENEMENTIEL') {
        containeer = GenerateBullEVEsemestre5()
        listcontainer = document.createElement('div')
        for (i = 0; i < mydata[1].length; i++) {
            clone = containeer.cloneNode(true);
            //Execution des traitements sur container
            clone = BullEVE(clone, i)
                //Puis ajout au containerList
            listcontainer.appendChild(clone)
        }
        //Fixation de ContainerList sur le body de la page
        var body = document.getElementById('body')
        body.appendChild(listcontainer)
    } else if (mydata[0] == 'MSO') {
        containeer = GenerateBullMSOsemestre5()
        listcontainer = document.createElement('div')
            //for(i=0; i<mydata[1].length; i++){
        clone = containeer.cloneNode(true);
        //Execution des traitements sur container
        //clone = BullMDS1(clone)
        //Puis ajout au containerList
        listcontainer.appendChild(clone)
            //}
            //Fixation de ContainerList sur le body de la page
        body.appendChild(listcontainer)
    }
})








/**
 * DECLARATION DES FONCTIONS DE GENERATION DES BULLETTINS DES SEMESTRES 1, 3, 5
 */
/*DECLARATION S1 MDS*/
function GenerateBullMDS1Semestre1() {
    //title
    var br = document.createElement('br')
    var slogan = document.createElement('div')
    slogan.innerHTML = `Au-delà de la limite`
    slogan.setAttribute('class', 'slogan')

    var titleinfo = document.createElement('div')
    titleinfo.innerHTML = `BP : 7403 Yaoundé  Tél : (237) 695 548 821 / 653 764 050 <br> Site Web : www.institutfrançoisembango.com Email : isep_fm@yahoo.com`
    titleinfo.setAttribute('class', 'title-info')

    title = document.createElement('div')
    title.setAttribute("id", "title")
    title.appendChild(slogan)
    title.appendChild(titleinfo)

    //Logo
    var headleft = document.createElement('div')
    headleft.setAttribute('id', 'head-left')

    var image = document.createElement('img')
    image.setAttribute("src", `/static/bulletin/image/logo.jpeg`)
    image.setAttribute("alt", "logo")

    var logo = document.createElement('div')
    logo.setAttribute("id", "logo")
    logo.appendChild(image)

    var headright = document.createElement('div')
    headright.setAttribute('id', 'head-right')

    containertitle = document.createElement('div')
    containertitle.appendChild(headleft)
    containertitle.appendChild(logo)
    containertitle.appendChild(headright)

    logoTitle = document.createElement('div')
    logoTitle.setAttribute('id', 'logo-title')
    logoTitle.appendChild(containertitle)
    logoTitle.appendChild(title)

    header = document.createElement('div')
    header.appendChild(logoTitle)

    hr = document.createElement('hr')

    first = document.createElement('div')
    first.appendChild(header)
    first.appendChild(hr)

    //MAIN
    var bullcheck = document.createElement('div')
    bullcheck.setAttribute('id', 'bull-check')
    bullcheck.innerHTML = `PF/DE`

    var bulltitle = document.createElement('div')
    bulltitle.setAttribute('id', 'bull-title')
    bulltitle.innerHTML = `RELEVE DE NOTES`

    var bullchecktitle = document.createElement('div')
    bullchecktitle.setAttribute('id', 'bull-check-title')
    bullchecktitle.appendChild(bullcheck)
    bullchecktitle.appendChild(bulltitle)

    //info student
    var info1 = document.createElement('div')
    info1.setAttribute('class', 'info-student-style')
    info1.innerHTML = `Filière &nbsp;&nbsp; : GESTION`
    var info2 = document.createElement('div')
    info2.setAttribute('class', 'info-student-style')
    info2.innerHTML = `Spécialité &nbsp;:  MDS`
    var info3 = document.createElement('div')
    info3.setAttribute('class', 'info-student-style')
    info3.innerHTML = `Nom (s) &nbsp; &nbsp; : `
    var info4 = document.createElement('div')
    info4.setAttribute('class', 'info-student-style')
    info4.innerHTML = `Prénom (s) : `
    var info5 = document.createElement('div')
    info5.setAttribute('class', 'info-student-style')
    info5.innerHTML = `Nationalité : Camerounais(e)`

    var infostudent1 = document.createElement('div')
    infostudent1.setAttribute('id', 'info-student-1')
    infostudent1.appendChild(info1)
    infostudent1.appendChild(info2)
    infostudent1.appendChild(info3)
    infostudent1.appendChild(info4)
    infostudent1.appendChild(info5)

    var info11 = document.createElement('div')
    info11.setAttribute('class', 'info-student-style')
    info11.innerHTML = `Grade : BTS  `
    var info22 = document.createElement('div')
    info22.setAttribute('class', 'info-student-style')
    info22.innerHTML = `Matricule : `
    var info33 = document.createElement('div')
    info33.setAttribute('class', 'info-student-style')
    info33.innerHTML = `Date de Naissance : `
    var info44 = document.createElement('div')
    info44.setAttribute('class', 'info-student-style')
    info44.innerHTML = `Lieu de Naissance : `
    var info55 = document.createElement('div')
    info55.setAttribute('class', 'info-student-style')
    info55.innerHTML = `Année Académique : `

    var infostudent2 = document.createElement('div')
    infostudent2.setAttribute('id', 'info-student-2')
    infostudent2.appendChild(info11)
    infostudent2.appendChild(info22)
    infostudent2.appendChild(info33)
    infostudent2.appendChild(info44)
    infostudent2.appendChild(info55)

    var info111 = document.createElement('div')
    info111.innerHTML = `Niveau: I`

    var infostudent3 = document.createElement('div')
    infostudent3.setAttribute('id', 'info-student-3')
    infostudent3.appendChild(info111)

    var infostudent = document.createElement('div')
    infostudent.setAttribute('id', 'info-student')
    infostudent.appendChild(infostudent1)
    infostudent.appendChild(infostudent2)
    infostudent.appendChild(infostudent3)

    //table1
    //thead -Line 1
    var tr1 = document.createElement('tr')
    var thvalue = ["", "Groupe UE", "Code UE", "Matière", "Note", "Coef", "Total", "Moyenne Groupe", "Rang", "Mention", "Session", "Crédits Obtenus"]
    for (i = 0; i < thvalue.length; i++) {
        var th = document.createElement('th')
        th.setAttribute("scope", "col")
        th.innerHTML = thvalue[i]
        tr1.appendChild(th)
    }
    var thead1 = document.createElement('thead')
    thead1.appendChild(tr1)
        //tbody
        //Line 2
    var th1 = document.createElement('th')
    th1.setAttribute('id', 'semestre')
    th1.setAttribute('rowspan', '11')
    th1.innerHTML = `SEMESTRE 1`
    var th2 = document.createElement('th')
    th2.setAttribute('scope', 'row')
    th2.setAttribute('rowspan', '4')
    th2.innerHTML = `UE Fondamentales`
    var td1 = document.createElement('td')
    td1.setAttribute('id', 'MDS111-codeue')
    td1.innerHTML = `MDS111`
    var td2 = document.createElement('td')
    td2.setAttribute('id', 'MDS111-matiere')
    td2.innerHTML = `Mathématiques I`
    var td3 = document.createElement('td')
    td3.setAttribute('id', 'MDS111-note')

    var td4 = document.createElement('td')
    td4.setAttribute('id', 'MDS111-coef')

    var td5 = document.createElement('td')
    td5.setAttribute('id', 'MDS111-total')

    var td6 = document.createElement('td')
    td6.setAttribute('id', 'MDS111-moyenne')
    td6.setAttribute('rowspan', '4')

    var td7 = document.createElement('td')
    td7.setAttribute('id', 'MDS111-rang')

    var td8 = document.createElement('td')
    td8.setAttribute('id', 'MDS111-mention')

    var td9 = document.createElement('td')
    td9.setAttribute('id', 'MDS111-session')

    var td10 = document.createElement('td')
    td10.setAttribute('id', 'MDS111-credits')
    td10.setAttribute('rowspan', '2')

    var tr2 = document.createElement('tr')
    tr2.appendChild(th1)
    tr2.appendChild(th2)
    tr2.appendChild(td1)
    tr2.appendChild(td2)
    tr2.appendChild(td3)
    tr2.appendChild(td4)
    tr2.appendChild(td5)
    tr2.appendChild(td6)
    tr2.appendChild(td7)
    tr2.appendChild(td8)
    tr2.appendChild(td9)
    tr2.appendChild(td10)

    //Line 3
    var td1 = document.createElement('td')
    td1.setAttribute('id', 'MDS111-codeue')
    td1.innerHTML = `MDS111`
    var td2 = document.createElement('td')
    td2.setAttribute('id', 'MDS111-matiere')
    td2.innerHTML = `Informatique I`
    var td3 = document.createElement('td')
    td3.setAttribute('id', 'MDS111-note')

    var td4 = document.createElement('td')
    td4.setAttribute('id', 'MDS111-coef')

    var td5 = document.createElement('td')
    td5.setAttribute('id', 'MDS111-total')

    var td6 = document.createElement('td')
    td6.setAttribute('id', 'MDS111-rang')

    var td7 = document.createElement('td')
    td7.setAttribute('id', 'MDS111-mention')

    var td8 = document.createElement('td')
    td8.setAttribute('id', 'MDS111-session')

    /*var td9=document.createElement('td')
    td9.setAttribute('id','MDS111-credits')*/

    var tr3 = document.createElement('tr')
    tr3.appendChild(td1)
    tr3.appendChild(td2)
    tr3.appendChild(td3)
    tr3.appendChild(td4)
    tr3.appendChild(td5)
    tr3.appendChild(td6)
    tr3.appendChild(td7)
    tr3.appendChild(td8)
        /* tr3.appendChild(td9)*/

    //Line 33
    var td11 = document.createElement('td')
    td11.setAttribute('id', 'MDS112-codeue')
    td11.innerHTML = `MDS112`

    var td12 = document.createElement('td')
    td12.setAttribute('id', 'MDS112-matiere')
    td12.innerHTML = `Mathématiques financières I`

    var td13 = document.createElement('td')
    td13.setAttribute('id', 'MDS112-note')

    var td14 = document.createElement('td')
    td14.setAttribute('id', 'MDS112-coef')

    var td15 = document.createElement('td')
    td15.setAttribute('id', 'MDS112-total')

    /*var td166=document.createElement('td')
    td166.setAttribute('id','MDS112-moyenne')*/

    var td16 = document.createElement('td')
    td16.setAttribute('id', 'MDS112-rang')

    var td17 = document.createElement('td')
    td17.setAttribute('id', 'MDS112-mention')

    var td18 = document.createElement('td')
    td18.setAttribute('id', 'MDS112-session')

    var td19 = document.createElement('td')
    td19.setAttribute('id', 'MDS112-credits')
    td19.setAttribute('rowspan', '2')

    var tr33 = document.createElement('tr')
    tr33.setAttribute('id', 'tr33-border-top')
    tr33.appendChild(td11)
    tr33.appendChild(td12)
    tr33.appendChild(td13)
    tr33.appendChild(td14)
    tr33.appendChild(td15)
        //tr33.appendChild(td166)
    tr33.appendChild(td16)
    tr33.appendChild(td17)
    tr33.appendChild(td18)
    tr33.appendChild(td19)

    //Line 333
    var td111 = document.createElement('td')
    td111.setAttribute('id', 'MDS112-codeue')
    td111.innerHTML = `MDS112`

    var td122 = document.createElement('td')
    td122.setAttribute('id', 'MDS112-matiere')
    td122.innerHTML = `Statistiques descriptives I`

    var td133 = document.createElement('td')
    td133.setAttribute('id', 'MDS112-note')

    var td144 = document.createElement('td')
    td144.setAttribute('id', 'MDS112-coef')

    var td155 = document.createElement('td')
    td155.setAttribute('id', 'MDS112-total')

    /*var td166=document.createElement('td')
    td166.setAttribute('id','MDS112-moyenne')*/

    var td166 = document.createElement('td')
    td166.setAttribute('id', 'MDS112-rang')

    var td177 = document.createElement('td')
    td177.setAttribute('id', 'MDS112-mention')

    var td188 = document.createElement('td')
    td188.setAttribute('id', 'MDS112-session')

    /*var td199=document.createElement('td')
    td199.setAttribute('id','MDS112-credits')*/

    var tr333 = document.createElement('tr')
    tr333.setAttribute('id', 'tr333-border-top')
    tr333.appendChild(td111)
    tr333.appendChild(td122)
    tr333.appendChild(td133)
    tr333.appendChild(td144)
    tr333.appendChild(td155)
        //tr33.appendChild(td166)
    tr333.appendChild(td166)
    tr333.appendChild(td177)
    tr333.appendChild(td188)
        //tr333.appendChild(td199)

    //Line 4 //REGROUPER L4 et L5 dans une boucle
    var th2 = document.createElement('th')
    th2.setAttribute('scope', 'row')
    th2.setAttribute('rowspan', '4')
    th2.innerHTML = `UE Professionnelles`

    var td20 = document.createElement('td')
    td20.setAttribute("id", "MDS113-codeue")
    td20.innerHTML = `MDS113`

    var td21 = document.createElement('td')
    td21.setAttribute("id", "MDS113-matiere")
    td21.innerHTML = `Environnement juridique et comptable I`

    var td22 = document.createElement('td')
    td22.setAttribute("id", "MDS113-note")

    var td222 = document.createElement('td')
    td222.setAttribute("id", "MDS113-coef")

    var td23 = document.createElement('td')
    td23.setAttribute("id", "MDS113-total")

    var td24 = document.createElement('td')
    td24.setAttribute("rowspan", "4")
    td24.setAttribute("id", "MDS113-moyenne")

    var td25 = document.createElement('td')
    td25.setAttribute("id", "MDS113-rang")

    var td26 = document.createElement('td')
    td26.setAttribute("id", "MDS113-mention")

    var td27 = document.createElement('td')
    td27.setAttribute("id", "MDS113-session")

    var td28 = document.createElement('td')
    td28.setAttribute("id", "MDS113-credits")

    var tr4 = document.createElement('tr')
    tr4.appendChild(th2)
    tr4.appendChild(td20)
    tr4.appendChild(td21)
    tr4.appendChild(td22)
    tr4.appendChild(td222)
    tr4.appendChild(td23)
    tr4.appendChild(td24)
    tr4.appendChild(td25)
    tr4.appendChild(td26)
    tr4.appendChild(td27)
    tr4.appendChild(td28)

    //Line 5
    var td28 = document.createElement('td')
    td28.setAttribute("id", "MDS114-codeue")
    td28.innerHTML = `MDS114`

    var td29 = document.createElement('td')
    td29.setAttribute("id", "MDS114-matiere")
    td29.innerHTML = `Marketing`

    var td30 = document.createElement('td')
    td30.setAttribute("id", "MDS114-note")

    var td31 = document.createElement('td')
    td31.setAttribute("id", "MDS114-coef")

    var td32 = document.createElement('td')
    td32.setAttribute("id", "MDS114-total")

    var td33 = document.createElement('td')
    td33.setAttribute("id", "MDS114-rang")

    var td34 = document.createElement('td')
    td34.setAttribute("id", "MDS114-mention")

    var td35 = document.createElement('td')
    td35.setAttribute("id", "MDS114-session")

    var td36 = document.createElement('td')
    td36.setAttribute("id", "MDS114-credits")

    var tr5 = document.createElement('tr')
    tr5.appendChild(td28)
    tr5.appendChild(td29)
    tr5.appendChild(td30)
    tr5.appendChild(td31)
    tr5.appendChild(td32)
    tr5.appendChild(td33)
    tr5.appendChild(td34)
    tr5.appendChild(td35)
    tr5.appendChild(td36)

    //Line 6
    var td377 = document.createElement('td')
    td377.setAttribute("id", "MDS115-codeue")
    td377.innerHTML = `MDS115`

    var td37 = document.createElement('td')
    td37.setAttribute("id", "MDS115-matiere")
    td37.innerHTML = `Outils de gestion de sport I`

    var td38 = document.createElement('td')
    td38.setAttribute("id", "MDS115-note")

    var td39 = document.createElement('td')
    td39.setAttribute("id", "MDS115-coef")

    var td40 = document.createElement('td')
    td40.setAttribute("id", "MDS115-total")

    var td41 = document.createElement('td')
    td41.setAttribute("id", "MDS115-rang")

    var td42 = document.createElement('td')
    td42.setAttribute("id", "MDS115-mention")

    var td43 = document.createElement('td')
    td43.setAttribute("id", "MDS115-session")

    var td44 = document.createElement('td')
    td44.setAttribute("id", "MDS115-credits")

    var tr6 = document.createElement('tr')
    tr6.appendChild(td377)
    tr6.appendChild(td37)
    tr6.appendChild(td38)
    tr6.appendChild(td39)
    tr6.appendChild(td40)
    tr6.appendChild(td41)
    tr6.appendChild(td42)
    tr6.appendChild(td43)
    tr6.appendChild(td44)

    //Line 7
    var td45 = document.createElement('td')
    td45.setAttribute("id", "MDS116-codeue")
    td45.innerHTML = `MDS116`

    var td46 = document.createElement('td')
    td46.setAttribute("id", "MDS116-matiere")
    td46.innerHTML = `Gestion des structures et organisations sportives I`

    var td47 = document.createElement('td')
    td47.setAttribute("id", "MDS116-note")

    var td48 = document.createElement('td')
    td48.setAttribute("id", "MDS116-coef")

    var td49 = document.createElement('td')
    td49.setAttribute("id", "MDS116-total")

    var td50 = document.createElement('td')
    td50.setAttribute("id", "MDS116-rang")

    var td51 = document.createElement('td')
    td51.setAttribute("id", "MDS116-mention")

    var td52 = document.createElement('td')
    td52.setAttribute("id", "MDS116-session")

    var td53 = document.createElement('td')
    td53.setAttribute("id", "MDS116-credits")

    var tr7 = document.createElement('tr')
    tr7.appendChild(td45)
    tr7.appendChild(td46)
    tr7.appendChild(td47)
    tr7.appendChild(td48)
    tr7.appendChild(td49)
    tr7.appendChild(td50)
    tr7.appendChild(td51)
    tr7.appendChild(td52)
    tr7.appendChild(td53)

    //Line 8
    var th3 = document.createElement('th')
    th3.setAttribute('scope', 'row')
    th3.setAttribute('rowspan', '2')
    th3.innerHTML = `UE Transversales`

    var td54 = document.createElement('td')
    td54.setAttribute("id", "MDS117-codeue")
    td54.innerHTML = `MDS117`

    var td56 = document.createElement('td')
    td56.setAttribute("id", "MDS117-matiere")
    td56.innerHTML = `Technique d'expression anglaise`

    var td57 = document.createElement('td')
    td57.setAttribute("id", "MDS117-note")

    var td58 = document.createElement('td')
    td58.setAttribute("id", "MDS117-coef")

    var td59 = document.createElement('td')
    td59.setAttribute("id", "MDS117-total")

    var td60 = document.createElement('td')
        //td60.setAttribute("rowspan","3")
    td60.setAttribute("id", "MDS117-moyenne")
    td60.setAttribute('rowspan', '2')

    var td61 = document.createElement('td')
    td61.setAttribute("id", "MDS117-rang")

    var td62 = document.createElement('td')
    td62.setAttribute("id", "MDS117-mention")

    var td63 = document.createElement('td')
    td63.setAttribute("id", "MDS117-session")

    var td64 = document.createElement('td')
    td64.setAttribute("id", "MDS117-credits")
    td64.setAttribute("rowspan", "")

    var tr8 = document.createElement('tr')
    tr8.setAttribute('id', "ligne-MDS117")
    tr8.appendChild(th3)
    tr8.appendChild(td54)
    tr8.appendChild(td56)
    tr8.appendChild(td57)
    tr8.appendChild(td58)
    tr8.appendChild(td59)
    tr8.appendChild(td60)
    tr8.appendChild(td61)
    tr8.appendChild(td62)
    tr8.appendChild(td63)
    tr8.appendChild(td64)

    //Line 88
    /*var th3=document.createElement('th')
    th3.setAttribute('scope','row')
    //th3.setAttribute('rowspan','3')
    th3.innerHTML=`UE Transversales`*/

    var td544 = document.createElement('td')
    td544.setAttribute("id", "MDS117-codeue")
    td544.innerHTML = `MDS117`

    var td566 = document.createElement('td')
    td566.setAttribute("id", "MDS117-matiere")
    td566.innerHTML = `Technique d'expression française`

    var td577 = document.createElement('td')
    td577.setAttribute("id", "MDS117-note")

    var td588 = document.createElement('td')
    td588.setAttribute("id", "MDS117-coef")

    var td599 = document.createElement('td')
    td599.setAttribute("id", "MDS117-total")

    //var td600=document.createElement('td')
    //td60.setAttribute("rowspan","3")
    //td600.setAttribute("id","MDS117-moyenne")

    var td611 = document.createElement('td')
    td611.setAttribute("id", "MDS117-rang")

    var td622 = document.createElement('td')
    td622.setAttribute("id", "MDS117-mention")

    var td633 = document.createElement('td')
    td633.setAttribute("id", "MDS117-session")

    var td644 = document.createElement('td')
    td644.setAttribute("id", "MDS117-credits")

    var tr88 = document.createElement('tr')
        //tr88.appendChild(th3)
    tr88.appendChild(td544)
    tr88.appendChild(td566)
    tr88.appendChild(td577)
    tr88.appendChild(td588)
    tr88.appendChild(td599)
        //tr88.appendChild(td600)
    tr88.appendChild(td611)
    tr88.appendChild(td622)
    tr88.appendChild(td633)
    tr88.appendChild(td644)
        //style
    tr88.setAttribute('class', 'line10')


    //Line 9
    var tr9 = document.createElement('tr')
        //tr9.setAttribute('id','resultat-eps2')
    for (i = 0; i <= 6; i++) {
        var td = document.createElement('td')
        if (i == 0) {
            td.innerHTML = `RESULTATS SEMESTRE 1`;
            td.setAttribute('colspan', '4')
        }
        if (i == 1) { td.setAttribute('id', 'resultat-coef') }
        if (i == 2) { td.setAttribute('id', 'resultat-total') }
        if (i == 3) { td.setAttribute('id', 'resultat-moyenne') }
        if (i == 4) { td.setAttribute('id', 'resultat-rang') }
        if (i == 5) {
            td.setAttribute('id', 'resultat');
            td.setAttribute('colspan', '2');
            td.innerHTML = `Total Crédits Semestre 1`
        }
        if (i == 6) { td.setAttribute('id', 'resultat-crédits') }

        tr9.appendChild(td)
    }

    //tbody
    var tbody = document.createElement('tbody')
    tbody.setAttribute('id', 'tbody00')
    tbody.appendChild(tr2)
    tbody.appendChild(tr3)
    tbody.appendChild(tr33)
    tbody.appendChild(tr333)
    tbody.appendChild(tr4)
    tbody.appendChild(tr5)
    tbody.appendChild(tr6)
    tbody.appendChild(tr7)
    tbody.appendChild(tr8)
    tbody.appendChild(tr88)
    tbody.appendChild(tr9)

    var table1 = document.createElement('table')
    table1.setAttribute('class', 'table-1')
    table1.appendChild(thead1)
    table1.appendChild(tbody)

    //table3
    //thead2
    var tr12 = document.createElement('tr')
    for (i = 0; i <= 11; i++) {
        var th = document.createElement('th')
        th.setAttribute('scope', 'col')
        if (i == 0) { th.innerHTML = `&nbsp;&nbsp;` }
        tr12.appendChild(th)
    }
    var thead2 = document.createElement('thead')
    thead2.appendChild(tr12)

    //tbody
    //Line 1
    var tr13 = document.createElement('tr')
    for (i = 0; i <= 8; i++) {
        var td = document.createElement('td')
        if (i == 1) {
            td.setAttribute('colspan', '3');
            td.innerHTML = `Moyenne de Classe de l'étudiant :`
        }
        if (i == 2) { td.innerHTML = `/ 20` }
        if (i == 3) {
            td.setAttribute('colspan', '2');
            td.innerHTML = `Maximum :`
        }
        if (i == 7) { td.innerHTML = `Retard :` }

        tr13.appendChild(td)
    }
    //Line 2
    var tr14 = document.createElement('tr')
    for (i = 0; i <= 8; i++) {
        var td = document.createElement('td')
        if (i == 1) {
            td.setAttribute('colspan', '3');
            td.innerHTML = `Moyenne Générale de la classe :`
        }
        if (i == 2) { td.innerHTML = `/ 20` }
        if (i == 3) {
            td.setAttribute('colspan', '2');
            td.innerHTML = `Minimum :`
        }
        if (i == 7) { td.innerHTML = `Absences:` }

        tr14.appendChild(td)
    }
    //Line 3
    var tr15 = document.createElement('tr')
    for (i = 0; i <= 8; i++) {
        var td = document.createElement('td')
        if (i == 1) { td.setAttribute('colspan', '3'); /*td.innerHTML=`Moyenne Générale de la classe :`*/ }
        //if(i==3){/*td.innerHTML=`/ 20`*/}
        if (i == 4) {
            td.setAttribute('colspan', '2');
            td.innerHTML = `Rang :`
        }
        //if(i==8){td.innerHTML=`Absences:`}
        if (i == 5) { td.innerHTML = ` sur ` }

        tr15.appendChild(td)
    }
    //Line 4

    //TABLEAU 3
    var tbody3 = document.createElement('tbody')
    tbody3.setAttribute('id', 'tbody-3')
    tbody3.appendChild(tr13)
    tbody3.appendChild(tr14)
    tbody3.appendChild(tr15)

    var table3 = document.createElement('table')
    table3.setAttribute('id', 'table-3')
    table3.appendChild(thead2)
    table3.appendChild(tbody3)

    //semester Result
    var semestreResult = document.createElement('div')
    semestreResult.setAttribute('id', 'semester-result')
    semestreResult.appendChild(table1)
    semestreResult.appendChild(table3)
        //Style du tab3
    semestreResult.children[1].style.display = 'none'
        /**SEMESTRE RESULT 2 */
    semestreResultmds2 = semestreResult.cloneNode(true)
    semestreResultmds2.setAttribute('id', 'semester-result-2')
        //
    bx = document.getElementById('recpas1s2')
    s1s2mds = bx.cloneNode(true)

    by = document.getElementById('visa1')
    s1s2mdsvisa = by.cloneNode(true)

    //Main
    var main = document.createElement('main')
    main.appendChild(bullchecktitle)
    main.appendChild(infostudent)
    main.appendChild(semestreResult)
        /**SEMESTRE RESULT 2 */
    main.appendChild(semestreResultmds2)

    main.appendChild(s1s2mds)
    main.appendChild(s1s2mdsvisa)


    //Footer
    var visa = document.createElement('div')
    visa.setAttribute('class', 'visa')
    visa.innerHTML = "VISA CHEF ETABLISSEMENT"

    var footer = document.createElement('footer')
    footer.appendChild(visa)

    //TEST
    containerbull = document.createElement('div')
    containerbull.setAttribute('class', 'container-bull')
    containerbull.appendChild(header)
    containerbull.appendChild(hr)
    containerbull.appendChild(main)
    containerbull.appendChild(footer)

    /*** BULLETINS SEMESTRE 2 MDS1  */









    //Retour de composant Bulletin
    return (containerbull)
}

/*DECLARATION S1 STAPS*/
function GenerateBullStaps1Semestre1() {
    var br = document.createElement('br')
    var slogan = document.createElement('div')
    slogan.innerHTML = `ARRETE N022-0003/L/MINESUP/DDES/ESUP/SDA/ABC`
    slogan.setAttribute('class', 'slogan')

    var titleinfo = document.createElement('div')
    titleinfo.innerHTML = `BP : 7403 Yaoundé  Tél : (237) 695 548 821 / 653 764 050 <br> Site Web : www.institutfrançoisembango.com Email : isep_fm@yahoo.com`
    titleinfo.setAttribute('class', 'title-info')

    var title = document.createElement('div')
    title.setAttribute("id", "title")
    title.appendChild(slogan)
    title.appendChild(titleinfo)

    //Logo
    var headleft = document.createElement('div')
    headleft.setAttribute('id', 'head-left')

    var image = document.createElement('img')
    image.setAttribute("src", `/static/bulletin/image/logo.jpeg`)
    image.setAttribute("alt", "logo")

    var logo = document.createElement('div')
    logo.setAttribute("id", "logo")
    logo.appendChild(image)

    var headright = document.createElement('div')
    headright.setAttribute('id', 'head-right')

    var containertitle = document.createElement('div')
    containertitle.appendChild(headleft)
    containertitle.appendChild(logo)
    containertitle.appendChild(headright)

    var logoTitle = document.createElement('div')
    logoTitle.setAttribute('id', 'logo-title')
    logoTitle.appendChild(containertitle)
    logoTitle.appendChild(title)

    var header = document.createElement('header')
    header.appendChild(logoTitle)

    var body = document.getElementsByTagName('body')
    body[0].appendChild(header)

    var hr = document.createElement('hr')

    //MAIN
    var bullcheck = document.createElement('div')
    bullcheck.setAttribute('id', 'bull-check')
    bullcheck.innerHTML = `PF/DE`

    var bulltitle = document.createElement('div')
    bulltitle.setAttribute('id', 'bull-title')
    bulltitle.innerHTML = `RELEVE DE NOTES`

    var bullchecktitle = document.createElement('div')
    bullchecktitle.setAttribute('id', 'bull-check-title')
    bullchecktitle.appendChild(bullcheck)
    bullchecktitle.appendChild(bulltitle)

    //info student
    var info1 = document.createElement('div')
    info1.setAttribute('class', 'info-student-style')
    info1.innerHTML = `Filière &nbsp;&nbsp; : STAPS`
    var info2 = document.createElement('div')
    info2.setAttribute('class', 'info-student-style')
    info2.innerHTML = `Spécialité &nbsp;:  EPS`
    var info3 = document.createElement('div')
    info3.setAttribute('class', 'info-student-style')
    info3.innerHTML = `Nom (s) &nbsp; &nbsp; : `
    var info4 = document.createElement('div')
    info4.setAttribute('class', 'info-student-style')
    info4.innerHTML = `Prénom (s) : `
    var info5 = document.createElement('div')
    info5.setAttribute('class', 'info-student-style')
    info5.innerHTML = `Nationalité : Camerounais(e)`

    var infostudent1 = document.createElement('div')
    infostudent1.setAttribute('id', 'info-student-1')
    infostudent1.appendChild(info1)
    infostudent1.appendChild(info2)
    infostudent1.appendChild(info3)
    infostudent1.appendChild(info4)
    infostudent1.appendChild(info5)

    var info11 = document.createElement('div')
    info11.setAttribute('class', 'info-student-style')
    info11.innerHTML = `Grade : BTS  `
    var info22 = document.createElement('div')
    info22.setAttribute('class', 'info-student-style')
    info22.innerHTML = `Matricule : `
    var info33 = document.createElement('div')
    info33.setAttribute('class', 'info-student-style')
    info33.innerHTML = `Date de Naissance : `
    var info44 = document.createElement('div')
    info44.setAttribute('class', 'info-student-style')
    info44.innerHTML = `Lieu de Naissance : `
    var info55 = document.createElement('div')
    info55.setAttribute('class', 'info-student-style')
    info55.innerHTML = `Année Académique : `

    var infostudent2 = document.createElement('div')
    infostudent2.setAttribute('id', 'info-student-2')
    infostudent2.appendChild(info11)
    infostudent2.appendChild(info22)
    infostudent2.appendChild(info33)
    infostudent2.appendChild(info44)
    infostudent2.appendChild(info55)

    var info111 = document.createElement('div')
    info111.innerHTML = `Niveau: I`

    var infostudent3 = document.createElement('div')
    infostudent3.setAttribute('id', 'info-student-3')
    infostudent3.appendChild(info111)

    var infostudent = document.createElement('div')
    infostudent.setAttribute('id', 'info-student')
    infostudent.appendChild(infostudent1)
    infostudent.appendChild(infostudent2)
    infostudent.appendChild(infostudent3)


    //table1
    //thead -Line 1
    var tr1 = document.createElement('tr')
    var thvalue = ["", "Groupe UE", "Code UE", "Matière", "Note", "Coef", "Total", "Moyenne Groupe", "Rang", "Mention", "Session", "Crédits Obtenus"]
    for (i = 0; i < thvalue.length; i++) {
        var th = document.createElement('th')
        th.setAttribute("scope", "col")
        th.innerHTML = thvalue[i]
        tr1.appendChild(th)
    }
    var thead1 = document.createElement('thead')
    thead1.appendChild(tr1)
        //tbody
        //Line 2
    var th1 = document.createElement('th')
    th1.setAttribute('id', 'semestre')
    th1.setAttribute('rowspan', '13')
    th1.innerHTML = `SEMESTRE 1`
    var th2 = document.createElement('th')
    th2.setAttribute('scope', 'row')
    th2.setAttribute('rowspan', '2')
    th2.innerHTML = `UE Fondamentales`
    var td1 = document.createElement('td')
    td1.setAttribute('id', 'EPS111-codeue')
    td1.innerHTML = `EPS111`
    var td2 = document.createElement('td')
    td2.setAttribute('id', 'EPS111-matiere')
    td2.innerHTML = `Histoire et principes de base de l'éducation Physique`
    var td3 = document.createElement('td')
    td3.setAttribute('id', 'EPS111-note')

    var td4 = document.createElement('td')
    td4.setAttribute('id', 'EPS111-coef')

    var td5 = document.createElement('td')
    td5.setAttribute('id', 'EPS111-total')

    var td6 = document.createElement('td')
    td6.setAttribute('id', 'EPS111-moyenne')
    td6.setAttribute('rowspan', '2')

    var td7 = document.createElement('td')
    td7.setAttribute('id', 'EPS111-rang')

    var td8 = document.createElement('td')
    td8.setAttribute('id', 'EPS111-mention')

    var td9 = document.createElement('td')
    td9.setAttribute('id', 'EPS111-session')

    var td10 = document.createElement('td')
    td10.setAttribute('id', 'EPS111-credits')

    var tr2 = document.createElement('tr')
    tr2.appendChild(th1)
    tr2.appendChild(th2)
    tr2.appendChild(td1)
    tr2.appendChild(td2)
    tr2.appendChild(td3)
    tr2.appendChild(td4)
    tr2.appendChild(td5)
    tr2.appendChild(td6)
    tr2.appendChild(td7)
    tr2.appendChild(td8)
    tr2.appendChild(td9)
    tr2.appendChild(td10)

    //Line 3
    var td11 = document.createElement('td')
    td11.setAttribute('id', 'EPS112-codeue')
    td11.innerHTML = `EPS112`

    var td12 = document.createElement('td')
    td12.setAttribute('id', 'EPS112-matiere')
    td12.innerHTML = `Psychologie du Sport-Sociologie du Sport`

    var td13 = document.createElement('td')
    td13.setAttribute('id', 'EPS112-note')

    var td14 = document.createElement('td')
    td14.setAttribute('id', 'EPS112-coef')

    var td15 = document.createElement('td')
    td15.setAttribute('id', 'EPS112-total')

    var td16 = document.createElement('td')
    td16.setAttribute('id', 'EPS112-rang')

    var td17 = document.createElement('td')
    td17.setAttribute('id', 'EPS112-mention')

    var td18 = document.createElement('td')
    td18.setAttribute('id', 'EPS112-session')

    var td19 = document.createElement('td')
    td19.setAttribute('id', 'EPS112-credits')

    var tr3 = document.createElement('tr')
    tr3.appendChild(td11)
    tr3.appendChild(td12)
    tr3.appendChild(td13)
    tr3.appendChild(td14)
    tr3.appendChild(td15)
    tr3.appendChild(td16)
    tr3.appendChild(td17)
    tr3.appendChild(td18)
    tr3.appendChild(td19)

    //Line 4 //REGROUPER L4 et L5 dans une boucle
    var th2 = document.createElement('th')
    th2.setAttribute('scope', 'row')
    th2.setAttribute('rowspan', '7')
    th2.innerHTML = `UE Professionnelles`

    var td20 = document.createElement('td')
    td20.setAttribute("id", "EPS113-codeue")
    td20.innerHTML = `EPS113`

    var td21 = document.createElement('td')
    td21.setAttribute("id", "EPS113-matiere")
    td21.innerHTML = `Didactique de l'EPS I`

    var td22 = document.createElement('td')
    td22.setAttribute("id", "EPS113-note")

    var td222 = document.createElement('td')
    td222.setAttribute("id", "EPS113-coef")

    var td23 = document.createElement('td')
    td23.setAttribute("id", "EPS113-total")

    var td24 = document.createElement('td')
    td24.setAttribute("rowspan", "7")
    td24.setAttribute("id", "EPS113-moyenne")

    var td25 = document.createElement('td')
    td25.setAttribute("id", "EPS113-rang")

    var td26 = document.createElement('td')
    td26.setAttribute("id", "EPS113-mention")

    var td27 = document.createElement('td')
    td27.setAttribute("id", "EPS113-session")

    var td28 = document.createElement('td')
    td28.setAttribute("id", "EPS113-credits")

    var tr4 = document.createElement('tr')
    tr4.appendChild(th2)
    tr4.appendChild(td20)
    tr4.appendChild(td21)
    tr4.appendChild(td22)
    tr4.appendChild(td222)
    tr4.appendChild(td23)
    tr4.appendChild(td24)
    tr4.appendChild(td25)
    tr4.appendChild(td26)
    tr4.appendChild(td27)
    tr4.appendChild(td28)

    //Line 5
    var td28 = document.createElement('td')
    td28.setAttribute("id", "EPS114-codeue")
    td28.innerHTML = `EPS114`

    var td29 = document.createElement('td')
    td29.setAttribute("id", "EPS114-matiere")
    td29.innerHTML = `Anatomie I`

    var td30 = document.createElement('td')
    td30.setAttribute("id", "EPS114-note")

    var td31 = document.createElement('td')
    td31.setAttribute("id", "EPS114-coef")

    var td32 = document.createElement('td')
    td32.setAttribute("id", "EPS114-total")

    var td33 = document.createElement('td')
    td33.setAttribute("id", "EPS114-rang")

    var td34 = document.createElement('td')
    td34.setAttribute("id", "EPS114-mention")

    var td35 = document.createElement('td')
    td35.setAttribute("id", "EPS114-session")

    var td36 = document.createElement('td')
    td36.setAttribute("id", "EPS114-credits")

    var tr5 = document.createElement('tr')
    tr5.appendChild(td28)
    tr5.appendChild(td29)
    tr5.appendChild(td30)
    tr5.appendChild(td31)
    tr5.appendChild(td32)
    tr5.appendChild(td33)
    tr5.appendChild(td34)
    tr5.appendChild(td35)
    tr5.appendChild(td36)

    //Line 6
    var td377 = document.createElement('td')
    td377.setAttribute("id", "EPS115a-codeue")
    td377.innerHTML = `EPS115`

    var td37 = document.createElement('td')
    td37.setAttribute("id", "EPS115a-matiere")
    td37.innerHTML = `Didactique des APS: Athlétisme`

    var td38 = document.createElement('td')
    td38.setAttribute("id", "EPS115a-note")

    var td39 = document.createElement('td')
    td39.setAttribute("id", "EPS115a-coef")

    var td40 = document.createElement('td')
    td40.setAttribute("id", "EPS115a-total")

    var td41 = document.createElement('td')
    td41.setAttribute("id", "EPS115a-rang")

    var td42 = document.createElement('td')
    td42.setAttribute("id", "EPS115a-mention")

    var td43 = document.createElement('td')
    td43.setAttribute("id", "EPS115a-session")

    var td44 = document.createElement('td')
    td44.setAttribute('rowspan', "4")
    td44.setAttribute("id", "EPS115a-credits")

    var tr6 = document.createElement('tr')
    tr6.appendChild(td377)
    tr6.appendChild(td37)
    tr6.appendChild(td38)
    tr6.appendChild(td39)
    tr6.appendChild(td40)
    tr6.appendChild(td41)
    tr6.appendChild(td42)
    tr6.appendChild(td43)
    tr6.appendChild(td44)

    //Line 6a
    var td377a = document.createElement('td')
    td377a.setAttribute("id", "EPS115-codeue")
    td377a.innerHTML = `EPS115`

    var td37a = document.createElement('td')
    td37a.setAttribute("id", "EPS115b-matiere")
    td37a.innerHTML = `Didactique des APS: Basket Ball`

    var td38a = document.createElement('td')
    td38a.setAttribute("id", "EPS115b-note")

    var td39a = document.createElement('td')
    td39a.setAttribute("id", "EPS115b-coef")

    var td40a = document.createElement('td')
    td40a.setAttribute("id", "EPS115b-total")

    var td41a = document.createElement('td')
    td41a.setAttribute("id", "EPS115b-rang")

    var td42a = document.createElement('td')
    td42a.setAttribute("id", "EPS115b-mention")

    var td43a = document.createElement('td')
    td43a.setAttribute("id", "EPS115b-session")

    //var td44a=document.createElement('td')
    //td44a.setAttribute("id","EPS115b-credits")

    var tr6a = document.createElement('tr')
    tr6a.setAttribute('id', 'ligne-EPS115b')
    tr6a.appendChild(td377a)
    tr6a.appendChild(td37a)
    tr6a.appendChild(td38a)
    tr6a.appendChild(td39a)
    tr6a.appendChild(td40a)
    tr6a.appendChild(td41a)
    tr6a.appendChild(td42a)
    tr6a.appendChild(td43a)
        //tr6a.appendChild(td44a)

    //Line 6b
    var td377b = document.createElement('td')
    td377b.setAttribute("id", "EPS115b-codeue")
    td377b.innerHTML = `EPS115`

    var td37b = document.createElement('td')
    td37b.setAttribute("id", "EPS115b-matiere")
    td37b.innerHTML = `Didactique des APS: Judo`

    var td38b = document.createElement('td')
    td38b.setAttribute("id", "EPS115b-note")

    var td39b = document.createElement('td')
    td39b.setAttribute("id", "EPS115b-coef")

    var td40b = document.createElement('td')
    td40b.setAttribute("id", "EPS115b-total")

    var td41b = document.createElement('td')
    td41b.setAttribute("id", "EPS115b-rang")

    var td42b = document.createElement('td')
    td42b.setAttribute("id", "EPS115b-mention")

    var td43b = document.createElement('td')
    td43b.setAttribute("id", "EPS115b-session")

    var td44b = document.createElement('td')
        //td44b.setAttribute("id","EPS115b-credits")

    var tr6b = document.createElement('tr')
    tr6b.appendChild(td377b)
    tr6b.appendChild(td37b)
    tr6b.appendChild(td38b)
    tr6b.appendChild(td39b)
    tr6b.appendChild(td40b)
    tr6b.appendChild(td41b)
    tr6b.appendChild(td42b)
    tr6b.appendChild(td43b)
        //tr6b.appendChild(td44b)

    //Line 6j
    var td377j = document.createElement('td')
    td377j.setAttribute("id", "EPS115j-codeue")
    td377j.innerHTML = `EPS115`

    var td37j = document.createElement('td')
    td37j.setAttribute("id", "EPS115j-matiere")
    td37j.innerHTML = `Didactique dees APS: Lutte`

    var td38j = document.createElement('td')
    td38j.setAttribute("id", "EPS115j-note")

    var td39j = document.createElement('td')
    td39j.setAttribute("id", "EPS115j-coef")

    var td40j = document.createElement('td')
    td40j.setAttribute("id", "EPS115j-total")

    var td41j = document.createElement('td')
    td41j.setAttribute("id", "EPS115j-rang")

    var td42j = document.createElement('td')
    td42j.setAttribute("id", "EPS115j-mention")

    var td43j = document.createElement('td')
    td43j.setAttribute("id", "EPS115j-session")

    //var td44j=document.createElement('td')
    //td44j.setAttribute("id","EPS115j-credits")

    var tr6j = document.createElement('tr')
    tr6j.appendChild(td377j)
    tr6j.appendChild(td37j)
    tr6j.appendChild(td38j)
    tr6j.appendChild(td39j)
    tr6j.appendChild(td40j)
    tr6j.appendChild(td41j)
    tr6j.appendChild(td42j)
    tr6j.appendChild(td43j)
        //tr6j.appendChild(td44j)

    //Line 7
    var td45 = document.createElement('td')
    td45.setAttribute("id", "EPS116-codeue")
    td45.innerHTML = `EPS116`

    var td46 = document.createElement('td')
    td46.setAttribute("id", "EPS116-matiere")
    td46.innerHTML = `La Physiologie de l’Execice I`

    var td47 = document.createElement('td')
    td47.setAttribute("id", "EPS116-note")

    var td48 = document.createElement('td')
    td48.setAttribute("id", "EPS116-coef")

    var td49 = document.createElement('td')
    td49.setAttribute("id", "EPS116-total")

    var td50 = document.createElement('td')
    td50.setAttribute("id", "EPS116-rang")

    var td51 = document.createElement('td')
    td51.setAttribute("id", "EPS116-mention")

    var td52 = document.createElement('td')
    td52.setAttribute("id", "EPS116-session")

    var td53 = document.createElement('td')
    td53.setAttribute("id", "EPS116-credits")

    var tr7 = document.createElement('tr')
    tr7.appendChild(td45)
    tr7.appendChild(td46)
    tr7.appendChild(td47)
    tr7.appendChild(td48)
    tr7.appendChild(td49)
    tr7.appendChild(td50)
    tr7.appendChild(td51)
    tr7.appendChild(td52)
    tr7.appendChild(td53)

    //Line 8
    var th3 = document.createElement('th')
    th3.setAttribute('scope', 'row')
    th3.setAttribute('rowspan', '3')
    th3.innerHTML = `UE Transversales`

    var td54 = document.createElement('td')
    td54.setAttribute("id", "EPS117-codeue")
    td54.innerHTML = `EPS117`

    var td56 = document.createElement('td')
    td56.setAttribute("id", "EPS117-matiere")
    td56.innerHTML = `Informatique`

    var td57 = document.createElement('td')
    td57.setAttribute("id", "EPS117-note")

    var td58 = document.createElement('td')
    td58.setAttribute("id", "EPS117-coef")

    var td59 = document.createElement('td')
    td59.setAttribute("id", "EPS117-total")

    var td60 = document.createElement('td')
    td60.setAttribute("rowspan", "3")
    td60.setAttribute("id", "EPS117-moyenne")

    var td61 = document.createElement('td')
    td61.setAttribute("id", "EPS117-rang")

    var td62 = document.createElement('td')
    td62.setAttribute("id", "EPS117-mention")

    var td63 = document.createElement('td')
    td63.setAttribute("id", "EPS117-session")

    var td64 = document.createElement('td')
        //td64.setAttribute('rowspan','2')
    td64.setAttribute("id", "EPS117-credits")

    var tr8 = document.createElement('tr')
    tr8.appendChild(th3)
    tr8.appendChild(td54)
    tr8.appendChild(td56)
    tr8.appendChild(td57)
    tr8.appendChild(td58)
    tr8.appendChild(td59)
    tr8.appendChild(td60)
    tr8.appendChild(td61)
    tr8.appendChild(td62)
    tr8.appendChild(td63)
    tr8.appendChild(td64)

    //Line 9
    var td45 = document.createElement('td')
    td45.setAttribute("id", "EPS118-codeue")
    td45.innerHTML = `EPS118`

    var td46 = document.createElement('td')
    td46.setAttribute("id", "EPS118-matiere")
    td46.innerHTML = `Technique d'expression française`

    var td47 = document.createElement('td')
    td47.setAttribute("id", "EPS118-note")

    var td48 = document.createElement('td')
    td48.setAttribute("id", "EPS118-coef")

    var td49 = document.createElement('td')
    td49.setAttribute("id", "EPS118-total")

    var td50 = document.createElement('td')
    td50.setAttribute("id", "EPS118-rang")

    var td51 = document.createElement('td')
    td51.setAttribute("id", "EPS118-mention")

    var td52 = document.createElement('td')
    td52.setAttribute("id", "EPS118-session")

    var td53 = document.createElement('td')
    td53.setAttribute("id", "EPS118-credits")

    var tr9 = document.createElement('tr')
    tr9.setAttribute('id', 'ligne-EPS118')
    tr9.appendChild(td45)
    tr9.appendChild(td46)
    tr9.appendChild(td47)
    tr9.appendChild(td48)
    tr9.appendChild(td49)
    tr9.appendChild(td50)
    tr9.appendChild(td51)
    tr9.appendChild(td52)
    tr9.appendChild(td53)

    //Line 10
    var td45 = document.createElement('td')
    td45.setAttribute("id", "EPS119-codeue")
    td45.innerHTML = `EPS119`

    var td46 = document.createElement('td')
    td46.setAttribute("id", "EPS119-matiere")
    td46.innerHTML = `Technique d'expression anglaise. Anglaise- Forbi`

    var td47 = document.createElement('td')
    td47.setAttribute("id", "EPS119-note")

    var td48 = document.createElement('td')
    td48.setAttribute("id", "EPS119-coef")

    var td49 = document.createElement('td')
    td49.setAttribute("id", "EPS119-total")

    var td50 = document.createElement('td')
    td50.setAttribute("id", "EPS119-rang")

    var td51 = document.createElement('td')
    td51.setAttribute("id", "EPS119-mention")

    var td52 = document.createElement('td')
    td52.setAttribute("id", "EPS119-session")

    var td53 = document.createElement('td')
    td53.setAttribute("id", "EPS119-credits")

    var tr10 = document.createElement('tr')
    tr10.setAttribute('id', 'ligne-EPS119')
    tr10.appendChild(td45)
    tr10.appendChild(td46)
    tr10.appendChild(td47)
    tr10.appendChild(td48)
    tr10.appendChild(td49)
    tr10.appendChild(td50)
    tr10.appendChild(td51)
    tr10.appendChild(td52)
    tr10.appendChild(td53)

    //Line 11
    var td100 = document.createElement('td')
    td100.setAttribute('colspan', '4')
    td100.innerHTML = `RESULTATS SEMESTRE 1`

    var td101 = document.createElement('td')
    td101.setAttribute("id", "resultat-coef")

    var td102 = document.createElement('td')
    td102.setAttribute("id", "resultat-total")

    var td103 = document.createElement('td')
    td103.setAttribute("id", "resultat-moyenne")

    var td104 = document.createElement('td')
    td104.setAttribute("id", "resultat-rang")

    var td105 = document.createElement('td')
    td105.setAttribute("colspan", "2")
    td105.setAttribute("id", "resultat")
    td105.innerHTML = `Total Crédits Semestre 1`

    var td106 = document.createElement('td')
    td106.setAttribute("id", "resultat-crédits")

    var tr11 = document.createElement('tr')
    tr11.setAttribute('id', 'ligne-13')
    tr11.appendChild(td100)
    tr11.appendChild(td101)
    tr11.appendChild(td102)
    tr11.appendChild(td103)
    tr11.appendChild(td104)
    tr11.appendChild(td105)
    tr11.appendChild(td106)

    //tbody
    var tbody = document.createElement('tbody')
    tbody.appendChild(tr2)
    tbody.appendChild(tr3)
    tbody.appendChild(tr4)
    tbody.appendChild(tr5)
    tbody.appendChild(tr6)
    tbody.appendChild(tr6a)
    tbody.appendChild(tr6b)
    tbody.appendChild(tr6j)
    tbody.appendChild(tr7)
    tbody.appendChild(tr8)
    tbody.appendChild(tr9)
    tbody.appendChild(tr10)
    tbody.appendChild(tr11)

    var table1 = document.createElement('table')
    table1.setAttribute('class', 'table-1')
    table1.appendChild(thead1)
    table1.appendChild(tbody)

    //table3
    //thead2
    var tr12 = document.createElement('tr')
    for (i = 0; i <= 11; i++) {
        var th = document.createElement('th')
        th.setAttribute('scope', 'col')
        if (i == 0) { th.innerHTML = `&nbsp;&nbsp;` }
        tr12.appendChild(th)
    }
    var thead2 = document.createElement('thead')
    thead2.appendChild(tr12)

    //tbody
    //Line 1
    var tr13 = document.createElement('tr')
    for (i = 0; i <= 8; i++) {
        var td = document.createElement('td')
        if (i == 1) {
            td.setAttribute('colspan', '3');
            td.innerHTML = `Moyenne de Classe de l'étudiant :`
        }
        if (i == 2) { td.innerHTML = `/ 20` }
        if (i == 3) {
            td.setAttribute('colspan', '2');
            td.innerHTML = `Maximum :`
        }
        if (i == 7) { td.innerHTML = `Retard :` }

        tr13.appendChild(td)
    }
    //Line 2
    var tr14 = document.createElement('tr')
    for (i = 0; i <= 8; i++) {
        var td = document.createElement('td')
        if (i == 1) {
            td.setAttribute('colspan', '3');
            td.innerHTML = `Moyenne Générale de la classe :`
        }
        if (i == 2) { td.innerHTML = `/ 20` }
        if (i == 3) {
            td.setAttribute('colspan', '2');
            td.innerHTML = `Minimum :`
        }
        if (i == 7) { td.innerHTML = `Absences:` }

        tr14.appendChild(td)
    }
    //Line 3
    var tr15 = document.createElement('tr')
    for (i = 0; i <= 8; i++) {
        var td = document.createElement('td')
        if (i == 1) { td.setAttribute('colspan', '3'); }
        if (i == 4) {
            td.setAttribute('colspan', '2');
            td.innerHTML = `Rang :`
        }
        if (i == 5) { td.innerHTML = ` sur ` }

        tr15.appendChild(td)
    }
    //Line 4
    var tbody3 = document.createElement('tbody')
    tbody3.setAttribute('id', 'tbody-3')
    tbody3.appendChild(tr13)
    tbody3.appendChild(tr14)
    tbody3.appendChild(tr15)

    var table3 = document.createElement('table')
    table3.setAttribute('id', 'table-3')
    table3.appendChild(thead2)
    table3.appendChild(tbody3)

    //semester Result
    var semestreResult = document.createElement('div')
    semestreResult.setAttribute('id', 'semester-result')
    semestreResult.appendChild(table1)
    semestreResult.appendChild(table3)
        /**SEMESTRE RESULT 2 */
    semestreResulteps2 = semestreResult.cloneNode(true)
    semestreResulteps2.setAttribute('id', 'semester-result-2')
        //
    bx1 = document.getElementById('recpas1s2')
    s1s2eps = bx1.cloneNode(true)

    by1 = document.getElementById('visa1')
    s1s2epsvisa = by1.cloneNode(true)

    //Main
    var main = document.createElement('main')
    main.appendChild(bullchecktitle)
    main.appendChild(infostudent)
    main.appendChild(semestreResult)
        /**SEMESTRE RESULT 2 */
    main.appendChild(semestreResulteps2)

    main.appendChild(s1s2eps)
    main.appendChild(s1s2epsvisa)

    //Footer
    var visa = document.createElement('div')
    visa.setAttribute('class', 'visa')
    visa.innerHTML = "VISA CHEF ETABLISSEMENT"

    var footer = document.createElement('footer')
    footer.appendChild(visa)

    //TEST
    containerbull = document.createElement('div')
    containerbull.setAttribute('class', 'container-bull')
    containerbull.appendChild(header)
    containerbull.appendChild(hr)
    containerbull.appendChild(main)
    containerbull.appendChild(footer)

    //TEST
    return (containerbull)
}
/*DECLARATION S3 STAPS*/
function GenerateBullStaps2Semestre3() {
    //title
    var br = document.createElement('br')
    var slogan = document.createElement('div')
    slogan.innerHTML = `ARRETE N022-0003/L/MINESUP/DDES/ESUP/SDA/ABC`
    slogan.setAttribute('class', 'slogan')

    var titleinfo = document.createElement('div')
    titleinfo.innerHTML = `BP : 7403 Yaoundé  Tél : (237) 695 548 821 / 653 764 050 <br> Site Web : www.institutfrançoisembango.com Email : isep_fm@yahoo.com`
    titleinfo.setAttribute('class', 'title-info')

    var title = document.createElement('div')
    title.setAttribute("id", "title")
    title.appendChild(slogan)
    title.appendChild(titleinfo)

    //Logo
    var headleft = document.createElement('div')
    headleft.setAttribute('id', 'head-left')

    var image = document.createElement('img')
    image.setAttribute("src", `/static/bulletin/image/logo.jpeg`)
    image.setAttribute("alt", "logo")

    var logo = document.createElement('div')
    logo.setAttribute("id", "logo")
    logo.appendChild(image)

    var headright = document.createElement('div')
    headright.setAttribute('id', 'head-right')

    var containertitle = document.createElement('div')
    containertitle.appendChild(headleft)
    containertitle.appendChild(logo)
    containertitle.appendChild(headright)

    var logoTitle = document.createElement('div')
    logoTitle.setAttribute('id', 'logo-title')
    logoTitle.appendChild(containertitle)
    logoTitle.appendChild(title)

    var header = document.createElement('header')
    header.appendChild(logoTitle)

    var body = document.getElementsByTagName('body')
    body[0].appendChild(header)

    var hr = document.createElement('hr')

    var bullcheck = document.createElement('div')
    bullcheck.setAttribute('id', 'bull-check')
    bullcheck.innerHTML = `PF/DE`

    var bulltitle = document.createElement('div')
    bulltitle.setAttribute('id', 'bull-title')
    bulltitle.innerHTML = `RELEVE DE NOTES`

    var bullchecktitle = document.createElement('div')
    bullchecktitle.setAttribute('id', 'bull-check-title')
    bullchecktitle.appendChild(bullcheck)
    bullchecktitle.appendChild(bulltitle)

    //info student
    var info1 = document.createElement('div')
    info1.setAttribute('class', 'info-student-style')
    info1.innerHTML = `Filière &nbsp;&nbsp; : STAPS`
    var info2 = document.createElement('div')
    info2.setAttribute('class', 'info-student-style')
    info2.innerHTML = `Spécialité &nbsp;:  EPS`
    var info3 = document.createElement('div')
    info3.setAttribute('class', 'info-student-style')
    info3.innerHTML = `Nom (s) &nbsp; &nbsp; : `
    var info4 = document.createElement('div')
    info4.setAttribute('class', 'info-student-style')
    info4.innerHTML = `Prénom (s) : `
    var info5 = document.createElement('div')
    info5.setAttribute('class', 'info-student-style')
    info5.innerHTML = `Nationalité : Camerounais(e)`

    var infostudent1 = document.createElement('div')
    infostudent1.setAttribute('id', 'info-student-1')
    infostudent1.appendChild(info1)
    infostudent1.appendChild(info2)
    infostudent1.appendChild(info3)
    infostudent1.appendChild(info4)
    infostudent1.appendChild(info5)

    var info11 = document.createElement('div')
    info11.setAttribute('class', 'info-student-style')
    info11.innerHTML = `Grade : BTS  `
    var info22 = document.createElement('div')
    info22.setAttribute('class', 'info-student-style')
    info22.innerHTML = `Matricule : `
    var info33 = document.createElement('div')
    info33.setAttribute('class', 'info-student-style')
    info33.innerHTML = `Date de Naissance : `
    var info44 = document.createElement('div')
    info44.setAttribute('class', 'info-student-style')
    info44.innerHTML = `Lieu de Naissance : `
    var info55 = document.createElement('div')
    info55.setAttribute('class', 'info-student-style')
    info55.innerHTML = `Année Académique : `

    var infostudent2 = document.createElement('div')
    infostudent2.setAttribute('id', 'info-student-2')
    infostudent2.appendChild(info11)
    infostudent2.appendChild(info22)
    infostudent2.appendChild(info33)
    infostudent2.appendChild(info44)
    infostudent2.appendChild(info55)

    var info111 = document.createElement('div')
    info111.innerHTML = `Niveau: II`

    var infostudent3 = document.createElement('div')
    infostudent3.setAttribute('id', 'info-student-3')
    infostudent3.appendChild(info111)

    var infostudent = document.createElement('div')
    infostudent.setAttribute('id', 'info-student')
    infostudent.appendChild(infostudent1)
    infostudent.appendChild(infostudent2)
    infostudent.appendChild(infostudent3)

    //table1
    //thead -Line 1
    var tr1 = document.createElement('tr')
    var thvalue = ["", "Groupe UE", "Code UE", "Matière", "Note", "Coef", "Total", "Moyenne Groupe", "Rang", "Mention", "Session", "Crédits Obtenus"]
    for (let i = 0; i < thvalue.length; i++) {
        var th = document.createElement('th')
        th.setAttribute("scope", "col")
        th.innerHTML = thvalue[i]
        tr1.appendChild(th)
    }
    var thead1 = document.createElement('thead')
    thead1.appendChild(tr1)
        //tbody
        //Line 2
    var th1 = document.createElement('th')
    th1.setAttribute('id', 'semestre')
    th1.setAttribute('rowspan', '15')
    th1.innerHTML = `SEMESTRE 3`
    var th2 = document.createElement('th')
    th2.setAttribute('scope', 'row')
    th2.setAttribute('rowspan', '2')
    th2.innerHTML = `UE Fondamentales`
    var td1 = document.createElement('td')
    td1.setAttribute('id', 'EPS231-codeue')
    td1.innerHTML = `EPS231`
    var td2 = document.createElement('td')
    td2.setAttribute('id', 'EPS231-matiere')
    td2.innerHTML = `Education Physique : Loisirs`
    var td3 = document.createElement('td')
    td3.setAttribute('id', 'EPS231-note')

    var td4 = document.createElement('td')
    td4.setAttribute('id', 'EPS231-coef')

    var td5 = document.createElement('td')
    td5.setAttribute('id', 'EPS231-total')

    var td6 = document.createElement('td')
    td6.setAttribute('id', 'EPS231-moyenne')
    td6.setAttribute('rowspan', '2')

    var td7 = document.createElement('td')
    td7.setAttribute('id', 'EPS231-rang')

    var td8 = document.createElement('td')
    td8.setAttribute('id', 'EPS231-mention')

    var td9 = document.createElement('td')
    td9.setAttribute('id', 'EPS231-session')

    var td10 = document.createElement('td')
    td10.setAttribute('id', 'EPS231-credits')

    var tr2 = document.createElement('tr')
    tr2.appendChild(th1)
    tr2.appendChild(th2)
    tr2.appendChild(td1)
    tr2.appendChild(td2)
    tr2.appendChild(td3)
    tr2.appendChild(td4)
    tr2.appendChild(td5)
    tr2.appendChild(td6)
    tr2.appendChild(td7)
    tr2.appendChild(td8)
    tr2.appendChild(td9)
    tr2.appendChild(td10)

    //Line 3
    var td11 = document.createElement('td')
    td11.setAttribute('id', 'EPS232-codeue')
    td11.innerHTML = `EPS232`

    var td12 = document.createElement('td')
    td12.setAttribute('id', 'EPS232-matiere')
    td12.innerHTML = `Eléments de Psychopédagogie`

    var td13 = document.createElement('td')
    td13.setAttribute('id', 'EPS232-note')

    var td14 = document.createElement('td')
    td14.setAttribute('id', 'EPS232-coef')

    var td15 = document.createElement('td')
    td15.setAttribute('id', 'EPS232-total')

    var td16 = document.createElement('td')
    td16.setAttribute('id', 'EPS232-rang')

    var td17 = document.createElement('td')
    td17.setAttribute('id', 'EPS232-mention')

    var td18 = document.createElement('td')
    td18.setAttribute('id', 'EPS232-session')

    var td19 = document.createElement('td')
    td19.setAttribute('id', 'EPS232-credits')

    var tr3 = document.createElement('tr')
    tr3.appendChild(td11)
    tr3.appendChild(td12)
    tr3.appendChild(td13)
    tr3.appendChild(td14)
    tr3.appendChild(td15)
    tr3.appendChild(td16)
    tr3.appendChild(td17)
    tr3.appendChild(td18)
    tr3.appendChild(td19)

    //Line 4 //REGROUPER L4 et L5 dans une boucle
    var th2 = document.createElement('th')
    th2.setAttribute('scope', 'row')
    th2.setAttribute('rowspan', '9')
    th2.innerHTML = `UE Professionnelles`

    var td20 = document.createElement('td')
    td20.setAttribute("id", "EPS233-codeue")
    td20.innerHTML = `EPS233`

    var td21 = document.createElement('td')
    td21.setAttribute("id", "EPS233-matiere")
    td21.innerHTML = `Didactique de l'EPS III`

    var td22 = document.createElement('td')
    td22.setAttribute("id", "EPS233-note")

    var td222 = document.createElement('td')
    td222.setAttribute("id", "EPS233-coef")

    var td23 = document.createElement('td')
    td23.setAttribute("id", "EPS233-total")

    var td24 = document.createElement('td')
    td24.setAttribute("rowspan", "9")
    td24.setAttribute("id", "EPS233-moyenne")

    var td25 = document.createElement('td')
    td25.setAttribute("id", "EPS233-rang")

    var td26 = document.createElement('td')
    td26.setAttribute("id", "EPS233-mention")

    var td27 = document.createElement('td')
    td27.setAttribute("id", "EPS233-session")

    var td28 = document.createElement('td')
    td28.setAttribute("id", "EPS233-credits")

    var tr4 = document.createElement('tr')
    tr4.appendChild(th2)
    tr4.appendChild(td20)
    tr4.appendChild(td21)
    tr4.appendChild(td22)
    tr4.appendChild(td222)
    tr4.appendChild(td23)
    tr4.appendChild(td24)
    tr4.appendChild(td25)
    tr4.appendChild(td26)
    tr4.appendChild(td27)
    tr4.appendChild(td28)

    //Line 5
    var td28 = document.createElement('td')
    td28.setAttribute("id", "EPS234-codeue")
    td28.innerHTML = `EPS234`

    var td29 = document.createElement('td')
    td29.setAttribute("id", "EPS234-matiere")
    td29.innerHTML = `La Physiologie de L'Exercice II`

    var td30 = document.createElement('td')
    td30.setAttribute("id", "EPS234-note")

    var td31 = document.createElement('td')
    td31.setAttribute("id", "EPS234-coef")

    var td32 = document.createElement('td')
    td32.setAttribute("id", "EPS234-total")

    var td33 = document.createElement('td')
    td33.setAttribute("id", "EPS234-rang")

    var td34 = document.createElement('td')
    td34.setAttribute("id", "EPS234-mention")

    var td35 = document.createElement('td')
    td35.setAttribute("id", "EPS234-session")

    var td36 = document.createElement('td')
    td36.setAttribute("id", "EPS234-credits")

    var tr5 = document.createElement('tr')
    tr5.appendChild(td28)
    tr5.appendChild(td29)
    tr5.appendChild(td30)
    tr5.appendChild(td31)
    tr5.appendChild(td32)
    tr5.appendChild(td33)
    tr5.appendChild(td34)
    tr5.appendChild(td35)
    tr5.appendChild(td36)

    //Line 6a
    var td377a = document.createElement('td')
    td377a.setAttribute("id", "EPS235a-codeue")
    td377a.innerHTML = `EPS235`

    var td37a = document.createElement('td')
    td37a.setAttribute("id", "EPS235a-matiere")
    td37a.innerHTML = `Didactique des APS: Athlétisme`

    var td38a = document.createElement('td')
    td38a.setAttribute("id", "EPS235a-note")

    var td39a = document.createElement('td')
    td39a.setAttribute("id", "EPS235a-coef")

    var td40a = document.createElement('td')
    td40a.setAttribute("id", "EPS235a-total")

    var td41a = document.createElement('td')
    td41a.setAttribute("id", "EPS235a-rang")

    var td42a = document.createElement('td')
    td42a.setAttribute("id", "EPS235a-mention")

    var td43a = document.createElement('td')
    td43a.setAttribute("id", "EPS235a-session")

    var td44a = document.createElement('td')
    td44a.setAttribute('rowspan', '6')
    td44a.setAttribute("id", "EPS235a-credits")

    var tr6a = document.createElement('tr')
    tr6a.appendChild(td377a)
    tr6a.appendChild(td37a)
    tr6a.appendChild(td38a)
    tr6a.appendChild(td39a)
    tr6a.appendChild(td40a)
    tr6a.appendChild(td41a)
    tr6a.appendChild(td42a)
    tr6a.appendChild(td43a)
    tr6a.appendChild(td44a)

    //Line 6b
    var td377b = document.createElement('td')
    td377b.setAttribute("id", "EPS235b-codeue")
    td377b.innerHTML = `EPS235`

    var td37b = document.createElement('td')
    td37b.setAttribute("id", "EPS235b-matiere")
    td37b.innerHTML = `Didactique des APS: Basket Ball`

    var td38b = document.createElement('td')
    td38b.setAttribute("id", "EPS235b-note")

    var td39b = document.createElement('td')
    td39b.setAttribute("id", "EPS235b-coef")

    var td40b = document.createElement('td')
    td40b.setAttribute("id", "EPS235b-total")

    var td41b = document.createElement('td')
    td41b.setAttribute("id", "EPS235b-rang")

    var td42b = document.createElement('td')
    td42b.setAttribute("id", "EPS235b-mention")

    var td43b = document.createElement('td')
    td43b.setAttribute("id", "EPS235b-session")

    /*var td44b=document.createElement('td')
    td44b.setAttribute("id","EPS235b-credits")*/

    var tr6b = document.createElement('tr')
    tr6b.setAttribute('id', 'ligne-eps235b')
    tr6b.appendChild(td377b)
    tr6b.appendChild(td37b)
    tr6b.appendChild(td38b)
    tr6b.appendChild(td39b)
    tr6b.appendChild(td40b)
    tr6b.appendChild(td41b)
    tr6b.appendChild(td42b)
    tr6b.appendChild(td43b)
        //tr6b.appendChild(td44b)

    //Line 6f
    var td377f = document.createElement('td')
    td377f.setAttribute("id", "EPS235f-codeue")
    td377f.innerHTML = `EPS235`

    var td37f = document.createElement('td')
    td37f.setAttribute("id", "EPS235f-matiere")
    td37f.innerHTML = `Didactique des APS: Football`

    var td38f = document.createElement('td')
    td38f.setAttribute("id", "EPS235f-note")

    var td39f = document.createElement('td')
    td39f.setAttribute("id", "EPS235f-coef")

    var td40f = document.createElement('td')
    td40f.setAttribute("id", "EPS235f-total")

    var td41f = document.createElement('td')
    td41f.setAttribute("id", "EPS235f-rang")

    var td42f = document.createElement('td')
    td42f.setAttribute("id", "EPS235f-mention")

    var td43f = document.createElement('td')
    td43f.setAttribute("id", "EPS235f-session")

    /*var td44f=document.createElement('td')
    td44f.setAttribute("id","EPS235f-credits")*/

    var tr6f = document.createElement('tr')
    tr6f.appendChild(td377f)
    tr6f.appendChild(td37f)
    tr6f.appendChild(td38f)
    tr6f.appendChild(td39f)
    tr6f.appendChild(td40f)
    tr6f.appendChild(td41f)
    tr6f.appendChild(td42f)
    tr6f.appendChild(td43f)
        //tr6f.appendChild(td44f)

    //Line 6g
    var td377g = document.createElement('td')
    td377g.setAttribute("id", "EPS235g-codeue")
    td377g.innerHTML = `EPS235`

    var td37g = document.createElement('td')
    td37g.setAttribute("id", "EPS235g-matiere")
    td37g.innerHTML = `Didactique des APS: Gymnastique`

    var td38g = document.createElement('td')
    td38g.setAttribute("id", "EPS235g-note")

    var td39g = document.createElement('td')
    td39g.setAttribute("id", "EPS235g-coef")

    var td40g = document.createElement('td')
    td40g.setAttribute("id", "EPS235g-total")

    var td41g = document.createElement('td')
    td41g.setAttribute("id", "EPS235g-rang")

    var td42g = document.createElement('td')
    td42g.setAttribute("id", "EPS235g-mention")

    var td43g = document.createElement('td')
    td43g.setAttribute("id", "EPS235g-session")

    /*var td44g=document.createElement('td')
    td44g.setAttribute("id","EPS235g-credits")*/

    var tr6g = document.createElement('tr')
    tr6g.appendChild(td377g)
    tr6g.appendChild(td37g)
    tr6g.appendChild(td38g)
    tr6g.appendChild(td39g)
    tr6g.appendChild(td40g)
    tr6g.appendChild(td41g)
    tr6g.appendChild(td42g)
    tr6g.appendChild(td43g)
        //tr6g.appendChild(td44g)

    //Line 6j
    var td377j = document.createElement('td')
    td377j.setAttribute("id", "EPS235j-codeue")
    td377j.innerHTML = `EPS235`

    var td37j = document.createElement('td')
    td37j.setAttribute("id", "EPS235j-matiere")
    td37j.innerHTML = `Didactique des APS: Judo`

    var td38j = document.createElement('td')
    td38j.setAttribute("id", "EPS235j-note")

    var td39j = document.createElement('td')
    td39j.setAttribute("id", "EPS235j-coef")

    var td40j = document.createElement('td')
    td40j.setAttribute("id", "EPS235j-total")

    var td41j = document.createElement('td')
    td41j.setAttribute("id", "EPS235j-rang")

    var td42j = document.createElement('td')
    td42j.setAttribute("id", "EPS235j-mention")

    var td43j = document.createElement('td')
    td43j.setAttribute("id", "EPS235j-session")

    /*var td44j=document.createElement('td')
    td44j.setAttribute("id","EPS235j-credits")*/

    var tr6j = document.createElement('tr')
    tr6j.setAttribute('id', 'ligne-eps235j')
    tr6j.appendChild(td377j)
    tr6j.appendChild(td37j)
    tr6j.appendChild(td38j)
    tr6j.appendChild(td39j)
    tr6j.appendChild(td40j)
    tr6j.appendChild(td41j)
    tr6j.appendChild(td42j)
    tr6j.appendChild(td43j)
        //tr6j.appendChild(td44j)

    //Line 6j
    var td377l = document.createElement('td')
    td377l.setAttribute("id", "EPS235l-codeue")
    td377l.innerHTML = `EPS235`

    var td37l = document.createElement('td')
    td37l.setAttribute("id", "EPS235l-matiere")
    td37l.innerHTML = `Didactique des APS: Lutte`

    var td38l = document.createElement('td')
    td38l.setAttribute("id", "EPS235l-note")

    var td39l = document.createElement('td')
    td39l.setAttribute("id", "EPS235l-coef")

    var td40l = document.createElement('td')
    td40l.setAttribute("id", "EPS235l-total")

    var td41l = document.createElement('td')
    td41l.setAttribute("id", "EPS235l-rang")

    var td42l = document.createElement('td')
    td42l.setAttribute("id", "EPS235l-mention")

    var td43l = document.createElement('td')
    td43l.setAttribute("id", "EPS235l-session")

    /*var td44l=document.createElement('td')
    td44l.setAttribute("id","EPS235l-credits")*/

    var tr6l = document.createElement('tr')
    tr6l.setAttribute('id', 'ligne-eps235l')
    tr6l.appendChild(td377l)
    tr6l.appendChild(td37l)
    tr6l.appendChild(td38l)
    tr6l.appendChild(td39l)
    tr6l.appendChild(td40l)
    tr6l.appendChild(td41l)
    tr6l.appendChild(td42l)
    tr6l.appendChild(td43l)
        //tr6l.appendChild(td44l)

    //Line 7
    var td45 = document.createElement('td')
    td45.setAttribute("id", "EPS236-codeue")
    td45.innerHTML = `EPS236`

    var td46 = document.createElement('td')
    td46.setAttribute("id", "EPS236-matiere")
    td46.innerHTML = `Pédagogie Pratique II`

    var td47 = document.createElement('td')
    td47.setAttribute("id", "EPS236-note")

    var td48 = document.createElement('td')
    td48.setAttribute("id", "EPS236-coef")

    var td49 = document.createElement('td')
    td49.setAttribute("id", "EPS236-total")

    var td50 = document.createElement('td')
    td50.setAttribute("id", "EPS236-rang")

    var td51 = document.createElement('td')
    td51.setAttribute("id", "EPS236-mention")

    var td52 = document.createElement('td')
    td52.setAttribute("id", "EPS236-session")

    var td53 = document.createElement('td')
    td53.setAttribute("id", "EPS236-credits")

    var tr7 = document.createElement('tr')
    tr7.setAttribute('id', 'ligne-eps236')
    tr7.appendChild(td45)
    tr7.appendChild(td46)
    tr7.appendChild(td47)
    tr7.appendChild(td48)
    tr7.appendChild(td49)
    tr7.appendChild(td50)
    tr7.appendChild(td51)
    tr7.appendChild(td52)
    tr7.appendChild(td53)

    //
    //Line 7
    /*var td455=document.createElement('td')
    td455.setAttribute("id","EPS236-codeue")
    td455.innerHTML=`EPS236`

    var td466=document.createElement('td')
    td466.setAttribute("id","EPS236-matiere")
    td466.innerHTML=`Pédagogie Pratique II`

    var td477=document.createElement('td')
    td477.setAttribute("id","EPS236-note")

    var td488=document.createElement('td')
    td488.setAttribute("id","EPS236-coef")

    var td499=document.createElement('td')
    td499.setAttribute("id","EPS236-total")

    var td500=document.createElement('td')
    td500.setAttribute("id","EPS236-rang")

    var td511=document.createElement('td')
    td511.setAttribute("id","EPS236-mention")

    var td522=document.createElement('td')
    td522.setAttribute("id","EPS236-session")

    var td533=document.createElement('td')
    td533.setAttribute("id","EPS236-credits")

    var tr77=document.createElement('tr')
    tr77.setAttribute('id','ligne-eps236')
    tr77.appendChild(td455)
    tr77.appendChild(td466)
    tr77.appendChild(td477)
    tr77.appendChild(td488)
    tr77.appendChild(td499)
    tr77.appendChild(td500)
    tr77.appendChild(td511)
    tr77.appendChild(td522)
    tr77.appendChild(td533)*/

    //Line 8
    var th3 = document.createElement('th')
    th3.setAttribute('scope', 'row')
    th3.setAttribute('rowspan', '3')
    th3.innerHTML = `UE Transversales`

    var td54 = document.createElement('td')
    td54.setAttribute("id", "EPS237-codeue")
    td54.innerHTML = `EPS237`

    var td56 = document.createElement('td')
    td56.setAttribute("id", "EPS237-matiere")
    td56.innerHTML = `Formation Bilingue -Anglais appliqué au APS`

    var td57 = document.createElement('td')
    td57.setAttribute("id", "EPS237-note")

    var td58 = document.createElement('td')
    td58.setAttribute("id", "EPS237-coef")

    var td59 = document.createElement('td')
    td59.setAttribute("id", "EPS237-total")

    var td60 = document.createElement('td')
    td60.setAttribute("rowspan", "3")
    td60.setAttribute("id", "EPS237-moyenne")

    var td61 = document.createElement('td')
    td61.setAttribute("id", "EPS237-rang")

    var td62 = document.createElement('td')
    td62.setAttribute("id", "EPS237-mention")

    var td63 = document.createElement('td')
    td63.setAttribute("id", "EPS237-session")

    var td64 = document.createElement('td')
        //td64.setAttribute('rowspan','3')
    td64.setAttribute("id", "EPS237-credits")

    var tr8 = document.createElement('tr')
    tr8.appendChild(th3)
    tr8.appendChild(td54)
    tr8.appendChild(td56)
    tr8.appendChild(td57)
    tr8.appendChild(td58)
    tr8.appendChild(td59)
    tr8.appendChild(td60)
    tr8.appendChild(td61)
    tr8.appendChild(td62)
    tr8.appendChild(td63)
    tr8.appendChild(td64)

    //Line 9
    var td45 = document.createElement('td')
    td45.setAttribute("id", "EPS238-codeue")
    td45.innerHTML = `EPS238`

    var td46 = document.createElement('td')
    td46.setAttribute("id", "EPS238-matiere")
    td46.innerHTML = `Technique d'expression française`

    var td47 = document.createElement('td')
    td47.setAttribute("id", "EPS238-note")

    var td48 = document.createElement('td')
    td48.setAttribute("id", "EPS238-coef")

    var td49 = document.createElement('td')
    td49.setAttribute("id", "EPS238-total")

    var td50 = document.createElement('td')
    td50.setAttribute("id", "EPS238-rang")

    var td51 = document.createElement('td')
    td51.setAttribute("id", "EPS238-mention")

    var td52 = document.createElement('td')
    td52.setAttribute("id", "EPS238-session")

    var td53 = document.createElement('td')
        //td53.setAttribute('rowspan','2')
    td53.setAttribute("id", "EPS238-credits")

    var tr9 = document.createElement('tr')
    tr9.appendChild(td45)
    tr9.appendChild(td46)
    tr9.appendChild(td47)
    tr9.appendChild(td48)
    tr9.appendChild(td49)
    tr9.appendChild(td50)
    tr9.appendChild(td51)
    tr9.appendChild(td52)
    tr9.appendChild(td53)

    //Line 10
    var td45 = document.createElement('td')
    td45.setAttribute("id", "EPS239-codeue")
    td45.innerHTML = `EPS239`

    var td46 = document.createElement('td')
    td46.setAttribute("id", "EPS239-matiere")
    td46.innerHTML = `Informatique`

    var td47 = document.createElement('td')
    td47.setAttribute("id", "EPS239-note")

    var td48 = document.createElement('td')
    td48.setAttribute("id", "EPS239-coef")

    var td49 = document.createElement('td')
    td49.setAttribute("id", "EPS239-total")

    var td50 = document.createElement('td')
    td50.setAttribute("id", "EPS239-rang")

    var td51 = document.createElement('td')
    td51.setAttribute("id", "EPS239-mention")

    var td52 = document.createElement('td')
    td52.setAttribute("id", "EPS239-session")

    var td53 = document.createElement('td')
    td53.setAttribute("id", "EPS239-credits")

    var tr10 = document.createElement('tr')
    tr10.appendChild(td45)
    tr10.appendChild(td46)
    tr10.appendChild(td47)
    tr10.appendChild(td48)
    tr10.appendChild(td49)
    tr10.appendChild(td50)
    tr10.appendChild(td51)
    tr10.appendChild(td52)
    tr10.appendChild(td53)

    //Line 11
    var td100 = document.createElement('td')
    td100.setAttribute('colspan', '4')
    td100.innerHTML = `RESULTATS SEMESTRE 3`

    var td101 = document.createElement('td')
    td101.setAttribute("id", "resultat-coef")

    var td102 = document.createElement('td')
    td102.setAttribute("id", "resultat-total")

    var td103 = document.createElement('td')
    td103.setAttribute("id", "resultat-moyenne")

    var td104 = document.createElement('td')
    td104.setAttribute("id", "resultat-rang")

    var td105 = document.createElement('td')
    td105.setAttribute("colspan", "2")
    td105.setAttribute("id", "resultat")
    td105.innerHTML = `Total Crédits Semestre 3`

    var td106 = document.createElement('td')
    td106.setAttribute("id", "resultat-crédits")

    var tr11 = document.createElement('tr')
    tr11.setAttribute('id', 'resultat-eps2')
    tr11.appendChild(td100)
    tr11.appendChild(td101)
    tr11.appendChild(td102)
    tr11.appendChild(td103)
    tr11.appendChild(td104)
    tr11.appendChild(td105)
    tr11.appendChild(td106)

    //tbody
    var tbody = document.createElement('tbody')
    tbody.appendChild(tr2)
    tbody.appendChild(tr3)
    tbody.appendChild(tr4)
    tbody.appendChild(tr5)
    tbody.appendChild(tr6a)
    tbody.appendChild(tr6b)
    tbody.appendChild(tr6f)
    tbody.appendChild(tr6g)
    tbody.appendChild(tr6j)
    tbody.appendChild(tr6l)
    tbody.appendChild(tr7)
    tbody.appendChild(tr8)
    tbody.appendChild(tr9)
    tbody.appendChild(tr10)
    tbody.appendChild(tr11)

    var table1 = document.createElement('table')
    table1.setAttribute('class', 'table-1')
    table1.appendChild(thead1)
    table1.appendChild(tbody)

    //table3
    //thead2
    var tr12 = document.createElement('tr')
    for (var i = 0; i <= 11; i++) {
        var th = document.createElement('th')
        th.setAttribute('scope', 'col')
        if (i == 0) { th.innerHTML = `&nbsp;&nbsp;` }
        tr12.appendChild(th)
    }
    var thead2 = document.createElement('thead')
    thead2.appendChild(tr12)

    //tbody
    //Line 1
    var tr13 = document.createElement('tr')
    for (i = 0; i <= 8; i++) {
        var td = document.createElement('td')
        if (i == 1) {
            td.setAttribute('colspan', '3');
            td.innerHTML = `Moyenne de Classe de l'étudiant :`
        }
        if (i == 2) { td.innerHTML = `/ 20` }
        if (i == 3) {
            td.setAttribute('colspan', '2');
            td.innerHTML = `Maximum :`
        }
        if (i == 7) { td.innerHTML = `Retard :` }

        tr13.appendChild(td)
    }
    //Line 2
    var tr14 = document.createElement('tr')
    for (i = 0; i <= 8; i++) {
        var td = document.createElement('td')
        if (i == 1) {
            td.setAttribute('colspan', '3');
            td.innerHTML = `Moyenne Générale de la classe :`
        }
        if (i == 2) { td.innerHTML = `/ 20` }
        if (i == 3) {
            td.setAttribute('colspan', '2');
            td.innerHTML = `Minimum :`
        }
        if (i == 7) { td.innerHTML = `Absences:` }

        tr14.appendChild(td)
    }
    //Line 3
    var tr15 = document.createElement('tr')
    for (i = 0; i <= 8; i++) {
        var td = document.createElement('td')
        if (i == 1) { td.setAttribute('colspan', '3'); }

        if (i == 4) {
            td.setAttribute('colspan', '2');
            td.innerHTML = `Rang :`
        }
        //if(i==8){td.innerHTML=`Absences:`}
        if (i == 5) { td.innerHTML = ` sur ` }

        tr15.appendChild(td)
    }
    //Line 4


    var tbody3 = document.createElement('tbody')
    tbody3.setAttribute('id', 'tbody-3')
    tbody3.appendChild(tr13)
    tbody3.appendChild(tr14)
    tbody3.appendChild(tr15)

    var table3 = document.createElement('table')
    table3.setAttribute('id', 'table-3')
    table3.appendChild(thead2)
    table3.appendChild(tbody3)

    //semester Result
    var semestreResult = document.createElement('div')
    semestreResult.setAttribute('id', 'semester-result')
    semestreResult.appendChild(table1)
    semestreResult.appendChild(table3)


    //Main
    var main = document.createElement('main')
    main.appendChild(bullchecktitle)
    main.appendChild(infostudent)

    /************************************************************************  SEMESTRE 4  *****************************************************************************/
    /*s4 = document.getElementById('semester-result0')
    s44 = s4.cloneNode(true)*/

    var semestreResult2 = semestreResult.cloneNode(true)
    semestreResult2.setAttribute('id', 'semestreResult2')

    /**MODIFICATION SEMESTRE 4 */
    //Ligne 1 & 2

    semestreResult2.children[0].children[1].children[0].children[0].innerHTML = "SEMESTRE 4"

    for (var j = 2; j <= 11; j++) {
        semestreResult2.children[0].children[1].children[0].children[j].innerHTML = "--"
    }
    for (j = 0; j <= 8; j++) {
        semestreResult2.children[0].children[1].children[1].children[j].innerHTML = "--"
    }

    semestreResult2.children[0].children[1].children[2].children[1].innerHTML = "EPS244"
    semestreResult2.children[0].children[1].children[2].children[2].innerHTML = "Stage-Professionnel"
        //Ligne 4
    semestreResult2.children[0].children[1].children[3].children[0].innerHTML = "EPS245"
    semestreResult2.children[0].children[1].children[3].children[1].innerHTML = "Didactique des APS : Athlétisme II"
        //Ligne 5
    semestreResult2.children[0].children[1].children[4].children[0].innerHTML = "EPS245"
    semestreResult2.children[0].children[1].children[4].children[1].innerHTML = "Didactique des APS : Football II"
        //Ligne 6
    semestreResult2.children[0].children[1].children[5].children[0].innerHTML = "EPS245"
    semestreResult2.children[0].children[1].children[5].children[1].innerHTML = "Didactique des APS : Judo II"
        //Ligne 7
    semestreResult2.children[0].children[1].children[6].children[0].innerHTML = "EPS245"
    semestreResult2.children[0].children[1].children[6].children[1].innerHTML = "Didactique des APS : Gymnastqiue"
        //Ligne 8
    semestreResult2.children[0].children[1].children[7].children[0].innerHTML = "EPS246"
    semestreResult2.children[0].children[1].children[7].children[1].innerHTML = "Anatomie"
        //Ligne 9
    semestreResult2.children[0].children[1].children[8].children[0].innerHTML = "EPS247"
    semestreResult2.children[0].children[1].children[8].children[1].innerHTML = "Physiologie"
        //Ligne 10
    semestreResult2.children[0].children[1].children[9].children[0].innerHTML = "EPS248"
    semestreResult2.children[0].children[1].children[9].children[1].innerHTML = "Education Physique : Loisirs II"
        //Ligne 11
    semestreResult2.children[0].children[1].children[10].children[0].innerHTML = "EPS249"
    semestreResult2.children[0].children[1].children[10].children[1].innerHTML = "Traumatologie - Premiers Secours"
        //Ligne 13
    semestreResult2.children[0].children[1].children[11].children[1].innerHTML = "EPS251"
    semestreResult2.children[0].children[1].children[11].children[2].innerHTML = "Economie du sport"
        //Ligne 14
    semestreResult2.children[0].children[1].children[12].children[0].innerHTML = "EPS252"
    semestreResult2.children[0].children[1].children[12].children[1].innerHTML = "Technique d'expression française II"


    //INSERTION DU NOEUD
    var nodeToCopy = semestreResult2.children[0].children[1].children[10]

    var newNode = nodeToCopy.cloneNode(true)
    newNode.setAttribute('id', 'ligne-eps250')
        //newNode.children[1].innerHTML = "PEDAGOGIE PRATIQUE III"

    var parentNode = semestreResult2.children[0].children[1]
    parentNode.insertBefore(newNode, nodeToCopy)
        //Ligne 12
    semestreResult2.children[0].children[1].children[11].children[0].innerHTML = "EPS250"
    semestreResult2.children[0].children[1].children[11].children[1].innerHTML = "Pédagogie Pratique III"
        //line
    semestreResult2.children[0].children[1].children[15].children[0].innerHTML = "RESULTATS SEMESTRE 4"
    semestreResult2.children[0].children[1].children[15].children[5].innerHTML = "Total Crédits Semestre 4"


    //node 248
    var node248 = semestreResult2.children[0].children[1].children[9]
    var tdvar = semestreResult2.children[0].children[1].children[10].children[8]
    var tdcredit = tdvar.cloneNode(true)
    tdcredit.setAttribute('id', 'eps248-credit')
    node248.insertBefore(tdcredit, node248.lastChild)

    //node 247
    var tdcredit1 = tdvar.cloneNode(true)
    tdcredit1.setAttribute('id', 'eps247-credit')
    var node247 = semestreResult2.children[0].children[1].children[8]
    node247.insertBefore(tdcredit1, node247.lastChild)

    //node 246
    var tdcredit12 = tdvar.cloneNode(true)
    tdcredit12.setAttribute('id', 'eps246-credit')
    var node246 = semestreResult2.children[0].children[1].children[7]
    node246.insertBefore(tdcredit12, node246.lastChild)


    /**MODIFICATIONS STYLE */
    parentNode.children[2].children[0].setAttribute('rowspan', "10")

    parentNode.children[2].children[6].setAttribute('rowspan', "10")

    parentNode.children[0].children[0].setAttribute('rowspan', "15") //16 à 15

    parentNode.children[3].children[8].setAttribute('rowspan', "4")
    parentNode.children[4].children[8].style.display = "none";

    parentNode.children[14].style.display = "none"

    parentNode.children[12].children[0].setAttribute('rowspan', "2")
    parentNode.children[12].children[6].setAttribute('rowspan', "2")


    /** RESULTAT FINAL */
    //var temp = document.getElementById('semester-result0')

    var s4result = semestreResult2.cloneNode(true)

    var s4s3 = document.getElementById('recpas3s4')
    var s4s3recap = s4s3.cloneNode(true)

    var v = document.getElementById('visa')
    visa = v.cloneNode(true)


    //#####################################  CREATION DU TABLEAU SEMESTRE 4  ########################################################


    //**********************Fixation sur le MAIN
    main.appendChild(semestreResult)
    main.appendChild(semestreResult2)
    main.appendChild(s4s3recap)
    main.appendChild(visa)
        //main.appendChild(s44)

    //Footer
    var visa = document.createElement('div')
    visa.setAttribute('class', 'visa')
    visa.innerHTML = "VISA CHEF ETABLISSEMENT"

    var footer = document.createElement('footer')
    footer.appendChild(visa)

    //TEST
    var containerbull = document.createElement('div')
    containerbull.setAttribute('class', 'container-bull')
    containerbull.appendChild(header)
    containerbull.appendChild(hr)
    containerbull.appendChild(main)
    containerbull.appendChild(footer)

    containerbull.style.display = 'block'

    //TEST
    /*body=document.getElementsByTagName('body')
    body[0].appendChild(containerbull)*/
    return (containerbull)
}






/*DECLARATION SEMESTRE 5 EVE */
function GenerateBullEVEsemestre5() {
    var br = document.createElement('br')
    var slogan = document.createElement('div')
    slogan.innerHTML = `Au-delà de la limite`
    slogan.setAttribute('class', 'slogan')

    var titleinfo = document.createElement('div')
    titleinfo.innerHTML = `BP : 7403 Yaoundé  Tél : (237) 695 548 821 / 653 764 050 <br> Site Web : www.institutfrançoisembango.com Email : isep_fm@yahoo.com`
    titleinfo.setAttribute('class', 'title-info')

    var title = document.createElement('div')
    title.setAttribute("id", "title")
    title.appendChild(slogan)
    title.appendChild(titleinfo)

    //Logo
    var headleft = document.createElement('div')
    headleft.setAttribute('id', 'head-left')

    var image = document.createElement('img')
    image.setAttribute("src", `/static/bulletin/image/logo.jpeg`)
    image.setAttribute("alt", "logo")

    var logo = document.createElement('div')
    logo.setAttribute("id", "logo")
    logo.appendChild(image)

    var headright = document.createElement('div')
    headright.setAttribute('id', 'head-right')

    var containertitle = document.createElement('div')
    containertitle.appendChild(headleft)
    containertitle.appendChild(logo)
    containertitle.appendChild(headright)

    var logoTitle = document.createElement('div')
    logoTitle.setAttribute('id', 'logo-title')
    logoTitle.appendChild(containertitle)
    logoTitle.appendChild(title)

    var header = document.createElement('header')
    header.appendChild(logoTitle)

    body = document.getElementsByTagName('body')
    body[0].appendChild(header)

    var hr = document.createElement('hr')

    var bullcheck = document.createElement('div')
    bullcheck.setAttribute('id', 'bull-check')
    bullcheck.innerHTML = `PF/DE`

    var bulltitle = document.createElement('div')
    bulltitle.setAttribute('id', 'bull-title')
    bulltitle.innerHTML = `RELEVE DE NOTES`

    var bullchecktitle = document.createElement('div')
    bullchecktitle.setAttribute('id', 'bull-check-title')
    bullchecktitle.appendChild(bullcheck)
    bullchecktitle.appendChild(bulltitle)

    //info student
    var info1 = document.createElement('div')
    info1.setAttribute('class', 'info-student-style')
    info1.innerHTML = `Filière &nbsp;&nbsp; : MAS`
    var info2 = document.createElement('div')
    info2.setAttribute('class', 'info-student-style')
    info2.innerHTML = `Spécialité &nbsp;:  EVE`
    var info3 = document.createElement('div')
    info3.setAttribute('class', 'info-student-style')
    info3.innerHTML = `Nom (s) &nbsp; &nbsp; : `
    var info4 = document.createElement('div')
    info4.setAttribute('class', 'info-student-style')
    info4.innerHTML = `Prénom (s) : `
    var info5 = document.createElement('div')
    info5.setAttribute('class', 'info-student-style')
    info5.innerHTML = `Nationalité : Camerounais(e)`

    var infostudent1 = document.createElement('div')
    infostudent1.setAttribute('id', 'info-student-1')
    infostudent1.appendChild(info1)
    infostudent1.appendChild(info2)
    infostudent1.appendChild(info3)
    infostudent1.appendChild(info4)
    infostudent1.appendChild(info5)

    var info11 = document.createElement('div')
    info11.setAttribute('class', 'info-student-style')
    info11.innerHTML = `Grade : LICENCE `
    var info22 = document.createElement('div')
    info22.setAttribute('class', 'info-student-style')
    info22.innerHTML = `Matricule : `
    var info33 = document.createElement('div')
    info33.setAttribute('class', 'info-student-style')
    info33.innerHTML = `Date de Naissance : `
    var info44 = document.createElement('div')
    info44.setAttribute('class', 'info-student-style')
    info44.innerHTML = `Lieu de Naissance : `
    var info55 = document.createElement('div')
    info55.setAttribute('class', 'info-student-style')
    info55.innerHTML = `Année Académique : `

    var infostudent2 = document.createElement('div')
    infostudent2.setAttribute('id', 'info-student-2')
    infostudent2.appendChild(info11)
    infostudent2.appendChild(info22)
    infostudent2.appendChild(info33)
    infostudent2.appendChild(info44)
    infostudent2.appendChild(info55)

    var info111 = document.createElement('div')
    info111.innerHTML = `Niveau: III`

    var infostudent3 = document.createElement('div')
    infostudent3.setAttribute('id', 'info-student-3')
    infostudent3.appendChild(info111)

    var infostudent = document.createElement('div')
    infostudent.setAttribute('id', 'info-student')
    infostudent.appendChild(infostudent1)
    infostudent.appendChild(infostudent2)
    infostudent.appendChild(infostudent3)

    //table1
    //thead -Line 1
    var tr1 = document.createElement('tr')
    var thvalue = ["", "Groupe UE", "Code UE", "Matière", "Note", "Coef", "Total", "Moyenne Groupe", "Rang", "Mention", "Session", "Crédits Obtenus"]
    for (i = 0; i < thvalue.length; i++) {
        var th = document.createElement('th')
        th.setAttribute("scope", "col")
        th.innerHTML = thvalue[i]
        tr1.appendChild(th)
    }
    var thead1 = document.createElement('thead')
    thead1.appendChild(tr1)
        //tbody
        //Line 2
    var th1 = document.createElement('th')
    th1.setAttribute('id', 'semestre')
    th1.setAttribute('rowspan', '7')
    th1.innerHTML = `SEMESTRE 5`
    var th2 = document.createElement('th')
    th2.setAttribute('scope', 'row')
    th2.setAttribute('rowspan', '4')
    th2.innerHTML = `UE Fondamentales`
    var td1 = document.createElement('td')
    td1.setAttribute('id', 'MAS315-codeue')
    td1.innerHTML = `MAS315`
    var td2 = document.createElement('td')
    td2.setAttribute('id', 'MAS315-matiere')
    td2.innerHTML = `Environnement Institutionnel de la pratique du Sport`
    var td3 = document.createElement('td')
    td3.setAttribute('id', 'MAS315-note')

    var td4 = document.createElement('td')
    td4.setAttribute('id', 'MAS315-coef')

    var td5 = document.createElement('td')
    td5.setAttribute('id', 'MAS315-total')

    var td6 = document.createElement('td')
    td6.setAttribute('id', 'MAS315-moyenne')
    td6.setAttribute('rowspan', '4')

    var td7 = document.createElement('td')
    td7.setAttribute('id', 'MAS315-rang')

    var td8 = document.createElement('td')
    td8.setAttribute('id', 'MAS315-mention')

    var td9 = document.createElement('td')
    td9.setAttribute('id', 'MAS315-session')

    var td10 = document.createElement('td')
    td10.setAttribute('id', 'MAS315-credits')

    var tr2 = document.createElement('tr')
    tr2.appendChild(th1)
    tr2.appendChild(th2)
    tr2.appendChild(td1)
    tr2.appendChild(td2)
    tr2.appendChild(td3)
    tr2.appendChild(td4)
    tr2.appendChild(td5)
    tr2.appendChild(td6)
    tr2.appendChild(td7)
    tr2.appendChild(td8)
    tr2.appendChild(td9)
    tr2.appendChild(td10)

    //Line 3
    var td11 = document.createElement('td')
    td11.setAttribute('id', 'MAS325-codeue')
    td11.innerHTML = `MAS325`

    var td12 = document.createElement('td')
    td12.setAttribute('id', 'MAS325-matiere')
    td12.innerHTML = `Montage Des Projets Et Entrepreneuriat Sportif`

    var td13 = document.createElement('td')
    td13.setAttribute('id', 'MAS325-note')

    var td14 = document.createElement('td')
    td14.setAttribute('id', 'MAS325-coef')

    var td15 = document.createElement('td')
    td15.setAttribute('id', 'MAS325-total')

    var td16 = document.createElement('td')
    td16.setAttribute('id', 'MAS325-rang')

    var td17 = document.createElement('td')
    td17.setAttribute('id', 'MAS325-mention')

    var td18 = document.createElement('td')
    td18.setAttribute('id', 'MAS325-session')

    var td19 = document.createElement('td')
    td19.setAttribute('id', 'EPS325-credits')

    var tr3 = document.createElement('tr')
    tr3.appendChild(td11)
    tr3.appendChild(td12)
    tr3.appendChild(td13)
    tr3.appendChild(td14)
    tr3.appendChild(td15)
    tr3.appendChild(td16)
    tr3.appendChild(td17)
    tr3.appendChild(td18)
    tr3.appendChild(td19)

    var td20 = document.createElement('td')
    td20.setAttribute("id", "MAS335-codeue")
    td20.innerHTML = `MAS335`

    var td21 = document.createElement('td')
    td21.setAttribute("id", "MAS335-matiere")
    td21.innerHTML = `Information Et Communication Stratégiques dans le Sport et les Loisirs`

    var td22 = document.createElement('td')
    td22.setAttribute("id", "MAS335-note")

    var td222 = document.createElement('td')
    td222.setAttribute("id", "MAS335-coef")

    var td23 = document.createElement('td')
    td23.setAttribute("id", "MAS335-total")

    var td25 = document.createElement('td')
    td25.setAttribute("id", "MAS335-rang")

    var td26 = document.createElement('td')
    td26.setAttribute("id", "MAS335-mention")

    var td27 = document.createElement('td')
    td27.setAttribute("id", "MAS335-session")

    var td28 = document.createElement('td')
    td28.setAttribute("id", "MAS335-credits")

    var tr4 = document.createElement('tr')
    tr4.appendChild(td20)
    tr4.appendChild(td21)
    tr4.appendChild(td22)
    tr4.appendChild(td222)
    tr4.appendChild(td23)
    tr4.appendChild(td25)
    tr4.appendChild(td26)
    tr4.appendChild(td27)
    tr4.appendChild(td28)

    //Line 5
    var td28 = document.createElement('td')
    td28.setAttribute("id", "MAS345-codeue")
    td28.innerHTML = `MAS345`

    var td29 = document.createElement('td')
    td29.setAttribute("id", "MAS345-matiere")
    td29.innerHTML = `E-sport`

    var td30 = document.createElement('td')
    td30.setAttribute("id", "MAS345-note")

    var td31 = document.createElement('td')
    td31.setAttribute("id", "MAS345-coef")

    var td32 = document.createElement('td')
    td32.setAttribute("id", "MAS345-total")

    var td33 = document.createElement('td')
    td33.setAttribute("id", "MAS345-rang")

    var td34 = document.createElement('td')
    td34.setAttribute("id", "MAS345-mention")

    var td35 = document.createElement('td')
    td35.setAttribute("id", "MAS345-session")

    var td36 = document.createElement('td')
    td36.setAttribute("id", "MAS345-credits")

    var tr5 = document.createElement('tr')
    tr5.appendChild(td28)
    tr5.appendChild(td29)
    tr5.appendChild(td30)
    tr5.appendChild(td31)
    tr5.appendChild(td32)
    tr5.appendChild(td33)
    tr5.appendChild(td34)
    tr5.appendChild(td35)
    tr5.appendChild(td36)

    //Line 8
    var th3 = document.createElement('th')
    th3.setAttribute('scope', 'row')
    th3.setAttribute('rowspan', '2')
    th3.innerHTML = `UE Spécialité`

    var td54 = document.createElement('td')
    td54.setAttribute("id", "EVE355-codeue")
    td54.innerHTML = `EVE355`

    var td56 = document.createElement('td')
    td56.setAttribute("id", "EVE355-matiere")
    td56.innerHTML = `Multimédias dans le Développement de Sport et Des Loisirs`

    var td57 = document.createElement('td')
    td57.setAttribute("id", "EVE355-note")

    var td58 = document.createElement('td')
    td58.setAttribute("id", "EVE355-coef")

    var td59 = document.createElement('td')
    td59.setAttribute("id", "EVE355-total")

    var td60 = document.createElement('td')
    td60.setAttribute("rowspan", "2")
    td60.setAttribute("id", "EVE355-moyenne")

    var td61 = document.createElement('td')
    td61.setAttribute("id", "EVE355-rang")

    var td62 = document.createElement('td')
    td62.setAttribute("id", "EVE355-mention")

    var td63 = document.createElement('td')
    td63.setAttribute("id", "EVE355-session")

    var td64 = document.createElement('td')
    td64.setAttribute("id", "EVE355-credits")

    var tr8 = document.createElement('tr')
    tr8.appendChild(th3)
    tr8.appendChild(td54)
    tr8.appendChild(td56)
    tr8.appendChild(td57)
    tr8.appendChild(td58)
    tr8.appendChild(td59)
    tr8.appendChild(td60)
    tr8.appendChild(td61)
    tr8.appendChild(td62)
    tr8.appendChild(td63)
    tr8.appendChild(td64)

    //Line 9
    var td45 = document.createElement('td')
    td45.setAttribute("id", "EVE365-codeue")
    td45.innerHTML = `EVE365`

    var td46 = document.createElement('td')
    td46.setAttribute("id", "EVE365-matiere")
    td46.innerHTML = `Ingénierie de L'Animation Sportive Et Culturelle`

    var td47 = document.createElement('td')
    td47.setAttribute("id", "EVE365-note")

    var td48 = document.createElement('td')
    td48.setAttribute("id", "EVE365-coef")

    var td49 = document.createElement('td')
    td49.setAttribute("id", "EVE365-total")

    var td50 = document.createElement('td')
    td50.setAttribute("id", "EVE365-rang")

    var td51 = document.createElement('td')
    td51.setAttribute("id", "EVE365-mention")

    var td52 = document.createElement('td')
    td52.setAttribute("id", "EVE365-session")

    var td53 = document.createElement('td')
    td53.setAttribute("id", "EVE365-credits")

    var tr9 = document.createElement('tr')
    tr9.appendChild(td45)
    tr9.appendChild(td46)
    tr9.appendChild(td47)
    tr9.appendChild(td48)
    tr9.appendChild(td49)
    tr9.appendChild(td50)
    tr9.appendChild(td51)
    tr9.appendChild(td52)
    tr9.appendChild(td53)

    //Line 11
    var td100 = document.createElement('td')
    td100.setAttribute('colspan', '4')
    td100.innerHTML = `RESULTATS SEMESTRE 5`

    var td101 = document.createElement('td')
    td101.setAttribute("id", "resultat-coef")

    var td102 = document.createElement('td')
    td102.setAttribute("id", "resultat-total")

    var td103 = document.createElement('td')
    td103.setAttribute("id", "resultat-moyenne")

    var td104 = document.createElement('td')
    td104.setAttribute("id", "resultat-rang")

    var td105 = document.createElement('td')
    td105.setAttribute("colspan", "2")
    td105.setAttribute("id", "resultat")
    td105.innerHTML = `Total Crédits Semestre 5`

    var td106 = document.createElement('td')
    td106.setAttribute("id", "resultat-crédits")

    var tr11 = document.createElement('tr')
    tr11.appendChild(td100)
    tr11.appendChild(td101)
    tr11.appendChild(td102)
    tr11.appendChild(td103)
    tr11.appendChild(td104)
    tr11.appendChild(td105)
    tr11.appendChild(td106)

    //tbody
    var tbody = document.createElement('tbody')
    tbody.setAttribute('id', 'tbody01')
    tbody.appendChild(tr2)
    tbody.appendChild(tr3)
    tbody.appendChild(tr4)
    tbody.appendChild(tr5)
    tbody.appendChild(tr8)
    tbody.appendChild(tr9)
    tbody.appendChild(tr11)

    var table1 = document.createElement('table')
    table1.setAttribute('class', 'table-1')
    table1.appendChild(thead1)
    table1.appendChild(tbody)

    //table3
    //thead2
    var tr12 = document.createElement('tr')
    for (i = 0; i <= 11; i++) {
        var th = document.createElement('th')
        th.setAttribute('scope', 'col')
        if (i == 0) { th.innerHTML = `&nbsp;&nbsp;` }
        tr12.appendChild(th)
    }
    var thead2 = document.createElement('thead')
    thead2.appendChild(tr12)

    //tbody
    //Line 1
    var tr13 = document.createElement('tr')
    for (i = 0; i <= 8; i++) {
        var td = document.createElement('td')
        if (i == 1) {
            td.setAttribute('colspan', '3');
            td.innerHTML = `Moyenne de Classe de l'étudiant :`
        }
        if (i == 2) { td.innerHTML = `/ 20` }
        if (i == 3) {
            td.setAttribute('colspan', '2');
            td.innerHTML = `Maximum :`
        }
        if (i == 7) { td.innerHTML = `Retard :` }

        tr13.appendChild(td)
    }
    //Line 2
    var tr14 = document.createElement('tr')
    for (i = 0; i <= 8; i++) {
        var td = document.createElement('td')
        if (i == 1) {
            td.setAttribute('colspan', '3');
            td.innerHTML = `Moyenne Générale de la classe :`
        }
        if (i == 2) { td.innerHTML = `/ 20` }
        if (i == 3) {
            td.setAttribute('colspan', '2');
            td.innerHTML = `Minimum :`
        }
        if (i == 7) { td.innerHTML = `Absences:` }

        tr14.appendChild(td)
    }
    //Line 3
    var tr15 = document.createElement('tr')
    for (i = 0; i <= 8; i++) {
        var td = document.createElement('td')
        if (i == 1) { td.setAttribute('colspan', '3'); }
        if (i == 4) {
            td.setAttribute('colspan', '2');
            td.innerHTML = `Rang :`
        }
        if (i == 5) { td.innerHTML = ` sur ` }

        tr15.appendChild(td)
    }
    //Line 4
    var tbody3 = document.createElement('tbody')
    tbody3.setAttribute('id', 'tbody-3')
    tbody3.appendChild(tr13)
    tbody3.appendChild(tr14)
    tbody3.appendChild(tr15)

    var table3 = document.createElement('table')
    table3.setAttribute('id', 'table-3')
    table3.appendChild(thead2)
    table3.appendChild(tbody3)

    var semestreResult = document.createElement('div')
    semestreResult.setAttribute('id', 'semester-result')
    semestreResult.appendChild(table1)
    semestreResult.appendChild(table3)

    /**SEMESTRE 6 RESULT */
    semestreResulteve6 = semestreResult.cloneNode(true)
    semestreResulteve6.setAttribute('id', 'semester-result-2')

    var s5s6 = document.getElementById('recpas3s4')
    s5s6recap = s5s6.cloneNode(true)

    var v = document.getElementById('visa')
    visa = v.cloneNode(true)

    //FOOTER
    /*var visa = document.createElement('div')
    visa.setAttribute('class', 'visa')
    visa.innerHTML = "VISA CHEF ETABLISSEMENT"

    var footer = document.createElement('footer')
    footer.appendChild(visa)*/


    //Main
    var main = document.createElement('main')
    main.appendChild(bullchecktitle)
    main.appendChild(infostudent)
    main.appendChild(semestreResult)
        /**SEMESTRE 6 RESULT */
    main.appendChild(semestreResulteve6)
    main.appendChild(s5s6recap)
    main.appendChild(visa)




    containerbull = document.createElement('div')
    containerbull.setAttribute('class', 'container-bull')
    containerbull.appendChild(header)
    containerbull.appendChild(hr)
    containerbull.appendChild(main)
        //containerbull.appendChild(footer)

    /*body=document.getElementsByTagName('body')
    body[0].appendChild(containerbull)*/
    return (containerbull)
}
/*DECLARATION GENERATION SEEMESTRE 5 MSO */
function GenerateBullMSOsemestre5() {
    var br = document.createElement('br')
    var slogan = document.createElement('div')
    slogan.innerHTML = `ARRETE N022-0003/L/MINESUP/DDES/ESUP/SDA/ABC`
    slogan.setAttribute('class', 'slogan')

    var titleinfo = document.createElement('div')
    titleinfo.innerHTML = `BP : 7403 Yaoundé  Tél : (237) 695 548 821 / 653 764 050 <br> Site Web : www.institutfrançoisembango.com Email : isep_fm@yahoo.com`
    titleinfo.setAttribute('class', 'title-info')

    var title = document.createElement('div')
    title.setAttribute("id", "title")
    title.appendChild(slogan)
    title.appendChild(titleinfo)

    //Logo
    var headleft = document.createElement('div')
    headleft.setAttribute('id', 'head-left')

    var image = document.createElement('img')
    image.setAttribute("src", `/static/bulletin/image/logo.jpeg`)
    image.setAttribute("alt", "logo")

    var logo = document.createElement('div')
    logo.setAttribute("id", "logo")
    logo.appendChild(image)




    var headright = document.createElement('div')
    headright.setAttribute('id', 'head-right')

    var containertitle = document.createElement('div')
    containertitle.appendChild(headleft)
    containertitle.appendChild(logo)
    containertitle.appendChild(headright)

    var logoTitle = document.createElement('div')
    logoTitle.setAttribute('id', 'logo-title')
    logoTitle.appendChild(containertitle)
    logoTitle.appendChild(title)

    var header = document.createElement('header')
    header.appendChild(logoTitle)

    body = document.getElementsByTagName('body')
    body[0].appendChild(header)

    var hr = document.createElement('hr')

    var bullcheck = document.createElement('div')
    bullcheck.setAttribute('id', 'bull-check')
    bullcheck.innerHTML = `PF/DE`

    var bulltitle = document.createElement('div')
    bulltitle.setAttribute('id', 'bull-title')
    bulltitle.innerHTML = `RELEVE DE NOTES`

    var bullchecktitle = document.createElement('div')
    bullchecktitle.setAttribute('id', 'bull-check-title')
    bullchecktitle.appendChild(bullcheck)
    bullchecktitle.appendChild(bulltitle)

    //info student
    var info1 = document.createElement('div')
    info1.setAttribute('class', 'info-student-style')
    info1.innerHTML = `Filière &nbsp;&nbsp; : MAS`
    var info2 = document.createElement('div')
    info2.setAttribute('class', 'info-student-style')
    info2.innerHTML = `Spécialité &nbsp;:  MSO`
    var info3 = document.createElement('div')
    info3.setAttribute('class', 'info-student-style')
    info3.innerHTML = `Nom (s) &nbsp; &nbsp; : `
    var info4 = document.createElement('div')
    info4.setAttribute('class', 'info-student-style')
    info4.innerHTML = `Prénom (s) : `
    var info5 = document.createElement('div')
    info5.setAttribute('class', 'info-student-style')
    info5.innerHTML = `Nationalité : Camerounais(e)`

    var infostudent1 = document.createElement('div')
    infostudent1.setAttribute('id', 'info-student-1')
    infostudent1.appendChild(info1)
    infostudent1.appendChild(info2)
    infostudent1.appendChild(info3)
    infostudent1.appendChild(info4)
    infostudent1.appendChild(info5)

    var info11 = document.createElement('div')
    info11.setAttribute('class', 'info-student-style')
    info11.innerHTML = `Grade : LICENCE `
    var info22 = document.createElement('div')
    info22.setAttribute('class', 'info-student-style')
    info22.innerHTML = `Matricule : `
    var info33 = document.createElement('div')
    info33.setAttribute('class', 'info-student-style')
    info33.innerHTML = `Date de Naissance : `
    var info44 = document.createElement('div')
    info44.setAttribute('class', 'info-student-style')
    info44.innerHTML = `Lieu de Naissance : `
    var info55 = document.createElement('div')
    info55.setAttribute('class', 'info-student-style')
    info55.innerHTML = `Année Académique : `

    var infostudent2 = document.createElement('div')
    infostudent2.setAttribute('id', 'info-student-2')
    infostudent2.appendChild(info11)
    infostudent2.appendChild(info22)
    infostudent2.appendChild(info33)
    infostudent2.appendChild(info44)
    infostudent2.appendChild(info55)

    var info111 = document.createElement('div')
    info111.innerHTML = `Niveau: III`

    var infostudent3 = document.createElement('div')
    infostudent3.setAttribute('id', 'info-student-3')
    infostudent3.appendChild(info111)

    var infostudent = document.createElement('div')
    infostudent.setAttribute('id', 'info-student')
    infostudent.appendChild(infostudent1)
    infostudent.appendChild(infostudent2)
    infostudent.appendChild(infostudent3)

    //table1
    //thead -Line 1
    var tr1 = document.createElement('tr')
    var thvalue = ["", "Groupe UE", "Code UE", "Matière", "Note", "Coef", "Total", "Moyenne Groupe", "Rang", "Mention", "Session", "Crédits Obtenus"]
    for (i = 0; i < thvalue.length; i++) {
        var th = document.createElement('th')
        th.setAttribute("scope", "col")
        th.innerHTML = thvalue[i]
        tr1.appendChild(th)
    }
    var thead1 = document.createElement('thead')
    thead1.appendChild(tr1)
        //tbody
        //Line 2
    var th1 = document.createElement('th')
    th1.setAttribute('id', 'semestre')
    th1.setAttribute('rowspan', '7')
    th1.innerHTML = `SEMESTRE 5`
    var th2 = document.createElement('th')
    th2.setAttribute('scope', 'row')
    th2.setAttribute('rowspan', '4')
    th2.innerHTML = `UE Fondamentales`
    var td1 = document.createElement('td')
    td1.setAttribute('id', 'MAS315-codeue')
    td1.innerHTML = `MAS315`
    var td2 = document.createElement('td')
    td2.setAttribute('id', 'MAS315-matiere')
    td2.innerHTML = `Environnement Institutionnel de la pratique du Sport`
    var td3 = document.createElement('td')
    td3.setAttribute('id', 'MAS315-note')

    var td4 = document.createElement('td')
    td4.setAttribute('id', 'MAS315-coef')

    var td5 = document.createElement('td')
    td5.setAttribute('id', 'MAS315-total')

    var td6 = document.createElement('td')
    td6.setAttribute('id', 'MAS315-moyenne')
    td6.setAttribute('rowspan', '4')

    var td7 = document.createElement('td')
    td7.setAttribute('id', 'MAS315-rang')

    var td8 = document.createElement('td')
    td8.setAttribute('id', 'MAS315-mention')

    var td9 = document.createElement('td')
    td9.setAttribute('id', 'MAS315-session')

    var td10 = document.createElement('td')
    td10.setAttribute('id', 'MAS315-credits')

    var tr2 = document.createElement('tr')
    tr2.appendChild(th1)
    tr2.appendChild(th2)
    tr2.appendChild(td1)
    tr2.appendChild(td2)
    tr2.appendChild(td3)
    tr2.appendChild(td4)
    tr2.appendChild(td5)
    tr2.appendChild(td6)
    tr2.appendChild(td7)
    tr2.appendChild(td8)
    tr2.appendChild(td9)
    tr2.appendChild(td10)

    //Line 3
    var td11 = document.createElement('td')
    td11.setAttribute('id', 'MAS325-codeue')
    td11.innerHTML = `MAS325`

    var td12 = document.createElement('td')
    td12.setAttribute('id', 'MAS325-matiere')
    td12.innerHTML = `Montage Des Projets Et Entrepreneuriat Sportif`

    var td13 = document.createElement('td')
    td13.setAttribute('id', 'MAS325-note')

    var td14 = document.createElement('td')
    td14.setAttribute('id', 'MAS325-coef')

    var td15 = document.createElement('td')
    td15.setAttribute('id', 'MAS325-total')

    var td16 = document.createElement('td')
    td16.setAttribute('id', 'MAS325-rang')

    var td17 = document.createElement('td')
    td17.setAttribute('id', 'MAS325-mention')

    var td18 = document.createElement('td')
    td18.setAttribute('id', 'MAS325-session')

    var td19 = document.createElement('td')
    td19.setAttribute('id', 'EPS325-credits')

    var tr3 = document.createElement('tr')
    tr3.appendChild(td11)
    tr3.appendChild(td12)
    tr3.appendChild(td13)
    tr3.appendChild(td14)
    tr3.appendChild(td15)
    tr3.appendChild(td16)
    tr3.appendChild(td17)
    tr3.appendChild(td18)
    tr3.appendChild(td19)

    var td20 = document.createElement('td')
    td20.setAttribute("id", "MAS335-codeue")
    td20.innerHTML = `MAS335`

    var td21 = document.createElement('td')
    td21.setAttribute("id", "MAS335-matiere")
    td21.innerHTML = `Information Et Communication Stratégiques dans le Sport et les Loisirs`

    var td22 = document.createElement('td')
    td22.setAttribute("id", "MAS335-note")

    var td222 = document.createElement('td')
    td222.setAttribute("id", "MAS335-coef")

    var td23 = document.createElement('td')
    td23.setAttribute("id", "MAS335-total")

    var td25 = document.createElement('td')
    td25.setAttribute("id", "MAS335-rang")

    var td26 = document.createElement('td')
    td26.setAttribute("id", "MAS335-mention")

    var td27 = document.createElement('td')
    td27.setAttribute("id", "MAS335-session")

    var td28 = document.createElement('td')
    td28.setAttribute("id", "MAS335-credits")

    var tr4 = document.createElement('tr')
    tr4.appendChild(td20)
    tr4.appendChild(td21)
    tr4.appendChild(td22)
    tr4.appendChild(td222)
    tr4.appendChild(td23)
    tr4.appendChild(td25)
    tr4.appendChild(td26)
    tr4.appendChild(td27)
    tr4.appendChild(td28)

    //Line 5
    var td28 = document.createElement('td')
    td28.setAttribute("id", "MAS345-codeue")
    td28.innerHTML = `MAS345`

    var td29 = document.createElement('td')
    td29.setAttribute("id", "MAS345-matiere")
    td29.innerHTML = `E-sport`

    var td30 = document.createElement('td')
    td30.setAttribute("id", "MAS345-note")

    var td31 = document.createElement('td')
    td31.setAttribute("id", "MAS345-coef")

    var td32 = document.createElement('td')
    td32.setAttribute("id", "MAS345-total")

    var td33 = document.createElement('td')
    td33.setAttribute("id", "MAS345-rang")

    var td34 = document.createElement('td')
    td34.setAttribute("id", "MAS345-mention")

    var td35 = document.createElement('td')
    td35.setAttribute("id", "MAS345-session")

    var td36 = document.createElement('td')
    td36.setAttribute("id", "MAS345-credits")

    var tr5 = document.createElement('tr')
    tr5.appendChild(td28)
    tr5.appendChild(td29)
    tr5.appendChild(td30)
    tr5.appendChild(td31)
    tr5.appendChild(td32)
    tr5.appendChild(td33)
    tr5.appendChild(td34)
    tr5.appendChild(td35)
    tr5.appendChild(td36)

    //Line 8
    var th3 = document.createElement('th')
    th3.setAttribute('scope', 'row')
    th3.setAttribute('rowspan', '2')
    th3.innerHTML = `UE Spécialité`

    var td54 = document.createElement('td')
    td54.setAttribute("id", "MSO355-codeue")
    td54.innerHTML = `MSO355`

    var td56 = document.createElement('td')
    td56.setAttribute("id", "MSO355-matiere")
    td56.innerHTML = `Ethique Sportive Et Programmes Olympiques`

    var td57 = document.createElement('td')
    td57.setAttribute("id", "MSO355-note")

    var td58 = document.createElement('td')
    td58.setAttribute("id", "MSO355-coef")

    var td59 = document.createElement('td')
    td59.setAttribute("id", "MSO355-total")

    var td60 = document.createElement('td')
    td60.setAttribute("rowspan", "2")
    td60.setAttribute("id", "MSO355-moyenne")

    var td61 = document.createElement('td')
    td61.setAttribute("id", "MSO355-rang")

    var td62 = document.createElement('td')
    td62.setAttribute("id", "MSO355-mention")

    var td63 = document.createElement('td')
    td63.setAttribute("id", "MSO355-session")

    var td64 = document.createElement('td')
    td64.setAttribute("id", "MSO355-credits")

    var tr8 = document.createElement('tr')
    tr8.appendChild(th3)
    tr8.appendChild(td54)
    tr8.appendChild(td56)
    tr8.appendChild(td57)
    tr8.appendChild(td58)
    tr8.appendChild(td59)
    tr8.appendChild(td60)
    tr8.appendChild(td61)
    tr8.appendChild(td62)
    tr8.appendChild(td63)
    tr8.appendChild(td64)

    //Line 9
    var td45 = document.createElement('td')
    td45.setAttribute("id", "MSO365-codeue")
    td45.innerHTML = `MSO365`

    var td46 = document.createElement('td')
    td46.setAttribute("id", "MSO365-matiere")
    td46.innerHTML = `Psychologie de Travail Et des Organisations`

    var td47 = document.createElement('td')
    td47.setAttribute("id", "MSO365-note")

    var td48 = document.createElement('td')
    td48.setAttribute("id", "MSO365-coef")

    var td49 = document.createElement('td')
    td49.setAttribute("id", "MSO365-total")

    var td50 = document.createElement('td')
    td50.setAttribute("id", "MSO365-rang")

    var td51 = document.createElement('td')
    td51.setAttribute("id", "MSO365-mention")

    var td52 = document.createElement('td')
    td52.setAttribute("id", "MSO365-session")

    var td53 = document.createElement('td')
    td53.setAttribute("id", "MSO365-credits")

    var tr9 = document.createElement('tr')
    tr9.appendChild(td45)
    tr9.appendChild(td46)
    tr9.appendChild(td47)
    tr9.appendChild(td48)
    tr9.appendChild(td49)
    tr9.appendChild(td50)
    tr9.appendChild(td51)
    tr9.appendChild(td52)
    tr9.appendChild(td53)

    //Line 11
    var td100 = document.createElement('td')
    td100.setAttribute('colspan', '4')
    td100.innerHTML = `RESULTATS SEMESTRE 5`

    var td101 = document.createElement('td')
    td101.setAttribute("id", "resultat-coef")

    var td102 = document.createElement('td')
    td102.setAttribute("id", "resultat-total")

    var td103 = document.createElement('td')
    td103.setAttribute("id", "resultat-moyenne")

    var td104 = document.createElement('td')
    td104.setAttribute("id", "resultat-rang")

    var td105 = document.createElement('td')
    td105.setAttribute("colspan", "2")
    td105.setAttribute("id", "resultat")
    td105.innerHTML = `Total Crédits Semestre 5`

    var td106 = document.createElement('td')
    td106.setAttribute("id", "resultat-crédits")

    var tr11 = document.createElement('tr')
    tr11.appendChild(td100)
    tr11.appendChild(td101)
    tr11.appendChild(td102)
    tr11.appendChild(td103)
    tr11.appendChild(td104)
    tr11.appendChild(td105)
    tr11.appendChild(td106)

    //tbody
    var tbody = document.createElement('tbody')
    tbody.setAttribute('id', 'tbody01')
    tbody.appendChild(tr2)
    tbody.appendChild(tr3)
    tbody.appendChild(tr4)
    tbody.appendChild(tr5)
    tbody.appendChild(tr8)
    tbody.appendChild(tr9)
    tbody.appendChild(tr11)

    var table1 = document.createElement('table')
    table1.setAttribute('class', 'table-1')
    table1.appendChild(thead1)
    table1.appendChild(tbody)

    //table3
    //thead2
    var tr12 = document.createElement('tr')
    for (i = 0; i <= 11; i++) {
        var th = document.createElement('th')
        th.setAttribute('scope', 'col')
        if (i == 0) { th.innerHTML = `&nbsp;&nbsp;` }
        tr12.appendChild(th)
    }
    var thead2 = document.createElement('thead')
    thead2.appendChild(tr12)

    //tbody
    //Line 1
    var tr13 = document.createElement('tr')
    for (i = 0; i <= 8; i++) {
        var td = document.createElement('td')
        if (i == 1) {
            td.setAttribute('colspan', '3');
            td.innerHTML = `Moyenne de Classe de l'étudiant :`
        }
        if (i == 2) { td.innerHTML = `/ 20` }
        if (i == 3) {
            td.setAttribute('colspan', '2');
            td.innerHTML = `Maximum :`
        }
        if (i == 7) { td.innerHTML = `Retard :` }

        tr13.appendChild(td)
    }
    //Line 2
    var tr14 = document.createElement('tr')
    for (i = 0; i <= 8; i++) {
        var td = document.createElement('td')
        if (i == 1) {
            td.setAttribute('colspan', '3');
            td.innerHTML = `Moyenne Générale de la classe :`
        }
        if (i == 2) { td.innerHTML = `/ 20` }
        if (i == 3) {
            td.setAttribute('colspan', '2');
            td.innerHTML = `Minimum :`
        }
        if (i == 7) { td.innerHTML = `Absences:` }

        tr14.appendChild(td)
    }
    //Line 3
    var tr15 = document.createElement('tr')
    for (i = 0; i <= 8; i++) {
        var td = document.createElement('td')
        if (i == 1) { td.setAttribute('colspan', '3'); }
        if (i == 4) {
            td.setAttribute('colspan', '2');
            td.innerHTML = `Rang :`
        }
        if (i == 5) { td.innerHTML = ` sur ` }

        tr15.appendChild(td)
    }
    //Line 4
    var tbody3 = document.createElement('tbody')
    tbody3.setAttribute('id', 'tbody-3')
    tbody3.appendChild(tr13)
    tbody3.appendChild(tr14)
    tbody3.appendChild(tr15)

    var table3 = document.createElement('table')
    table3.setAttribute('id', 'table-3')
    table3.appendChild(thead2)
    table3.appendChild(tbody3)

    var semestreResult = document.createElement('div')
    semestreResult.setAttribute('id', 'semester-result')
    semestreResult.appendChild(table1)
    semestreResult.appendChild(table3)
        /**  s6 */
    bx6 = document.getElementById('recpas3s4')
    s6 = bx6.cloneNode(true)

    by6 = document.getElementById('visa')
    s5s6evevisa = by.cloneNode(true)

    var main = document.createElement('main')
    main.appendChild(bullchecktitle)
    main.appendChild(infostudent)
    main.appendChild(semestreResult)


    /*var visa = document.createElement('div')
    visa.setAttribute('class', 'visa')
    visa.innerHTML = "VISA CHEF ETABLISSEMENT"*/


    var footer = document.createElement('footer')
    footer.appendChild(visa)

    main.appendChild(by6)
    main.appendChild(s5s6evevisa)


    containerbull = document.createElement('div')
    containerbull.setAttribute('class', 'container-bull')
    containerbull.appendChild(header)
    containerbull.appendChild(hr)
    containerbull.appendChild(main)
    containerbull.appendChild(footer)

    /*body=document.getElementsByTagName('body')
    body[0].appendChild(containerbull)*/
    return (containerbull)
}



/**FONCTION BULLETIN MDS */
function BullMDS1(clone, i, mydata) {

    //DONNEES RECUPEREES DE LA BD
    listStudent = mydata[1]
        //semestre1 =

    //Info Utilisateur
    info1 = clone.children[2].children[1].children[0]
    info1.children[2].innerHTML = info1.children[2].innerHTML + ` ${listStudent[i][0]['nom']}`
    info1.children[3].innerHTML = info1.children[3].innerHTML + ` ${listStudent[i][0]['prenom']}`

    info2 = clone.children[2].children[1].children[1]
    info2.children[1].innerHTML = info2.children[1].innerHTML + ` ${listStudent[i][0]['matricule']}`
    info2.children[2].innerHTML = info2.children[2].innerHTML + ` ${listStudent[i][0]['date_naissance']}`
    info2.children[3].innerHTML = info2.children[3].innerHTML + ` ${listStudent[i][0]['lieu_naissance']}`
    info2.children[4].innerHTML = info2.children[4].innerHTML + ` 2022-2023`

    //Tableau de notes
    var tbody = clone.children[2].children[2].children[0].children[1]

    //LIGNE MDS11
    var ligneMDS111 = tbody.children[0]
    for (j = 0; j <= ligneMDS111.childElementCount - 1; j++) {
        if (j == 4) { ligneMDS111.children[j].innerHTML = listStudent[i][1][0] } //note math
        if (j == 5) { ligneMDS111.children[j].innerHTML = listStudent[i][1][1] } //coef math
        if (j == 6) { ligneMDS111.children[j].innerHTML = listStudent[i][1][2] } //total note math * coef
        if (j == 7) { ligneMDS111.children[j].innerHTML = listStudent[i][1][3] } //moyenne donc (totalmath + totalinfo)/2
        if (j == 8) { ligneMDS111.children[j].innerHTML = listStudent[i][1][4] /*ligneMDS111.children[j].innerHTML =  mds1sort.indexof(mds111[i]['note_Examen'])*/ } //Rang
        if (j == 9) {
            if (((listStudent[i][1][0] >= 7 && listStudent[i][1][0] < 10) && listStudent[i][1][3] >= 10)) { ligneMDS111.children[j].innerHTML = "Validée" } else if ((listStudent[i][1][0] >= 10)) { ligneMDS111.children[j].innerHTML = "Validée" } else if (listStudent[i][1][0] < 10) { ligneMDS111.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 10) { ligneMDS111.children[j].innerHTML = mydata[4] } //Session
        if (j == 11) {
            if ((listStudent[i][1][0] >= 7 && listStudent[i][1][3] >= 10) || (listStudent[i][1][0] >= 10)) { ligneMDS111.children[j].innerHTML = listStudent[i][1][6] } else { ligneMDS111.children[j].innerHTML = 0 }
            //if ((listStudent[i][1][0] + listStudent[i][2][0]) >= 20) { ligneMDS111.children[j].innerHTML = listStudent[i][1][6] } else { ligneMDS111.children[j].innerHTML = 0 } 
        } //Crédits
    }

    //LIGNE MDS11b
    ligneMDS111b = tbody.children[1]
    for (j = 0; j <= ligneMDS111b.childElementCount - 1; j++) {
        if (j == 2) { ligneMDS111b.children[j].innerHTML = listStudent[i][2][0] } //note info
        if (j == 3) { ligneMDS111b.children[j].innerHTML = listStudent[i][2][1] } //coef info
        if (j == 4) { /*val=ligneMDS111b.children[2].innerHTML*ligneMDS111b.children[3].innerHTML; val= val.toFixed(2); val = parseFloat(val);*/ ligneMDS111b.children[j].innerHTML = listStudent[i][2][2] } //total note math * coef
        if (j == 5) { ligneMDS111b.children[j].innerHTML = listStudent[i][2][4] } //Rang
        if (j == 6) {
            if (((listStudent[i][2][0] >= 7 && listStudent[i][2][0] < 10) && listStudent[i][1][3] >= 10)) { ligneMDS111b.children[j].innerHTML = "Validée" } else if ((listStudent[i][2][0] >= 10)) { ligneMDS111b.children[j].innerHTML = "Validée" } else if (listStudent[i][2][0] < 10) { ligneMDS111b.children[j].innerHTML = "Non validée" }
            //if (listStudent[i][2][5]) { ligneMDS111b.children[6].innerHTML = "Validée" } else { ligneMDS111b.children[6].innerHTML = "Non validée" }
        }
        if (j == 7) { ligneMDS111b.children[j].innerHTML = mydata[4] } //Session
        if (j == 8) {
            if ((listStudent[i][2][0] >= 7 && listStudent[i][1][3] >= 10) || (listStudent[i][2][0] >= 10)) { ligneMDS111b.children[j].innerHTML = listStudent[i][2][6] } else { ligneMDS111b.children[j].innerHTML = 0 }
            //if ((listStudent[i][1][0] + listStudent[i][2][0]) >= 20) { ligneMDS111b.children[j].innerHTML = listStudent[i][2][6] } else { ligneMDS111b.children[j].innerHTML = 0 } 
        } //Crédits
    }

    //LIGNE MDS112
    var ligneMDS112 = tbody.children[2]
    for (j = 0; j <= ligneMDS112.childElementCount - 1; j++) {
        if (j == 2) { ligneMDS112.children[j].innerHTML = listStudent[i][3][0] } //note info
        if (j == 3) { ligneMDS112.children[j].innerHTML = listStudent[i][3][1] } //coef info
        if (j == 4) { /*val=ligneMDS112.children[2].innerHTML*ligneMDS112.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneMDS112.children[j].innerHTML = listStudent[i][3][2] } //total note math * coef
        if (j == 5) { ligneMDS112.children[j].innerHTML = listStudent[i][3][4] } //Rang
        if (j == 6) {
            if (((listStudent[i][3][0] >= 7 && listStudent[i][3][0] < 10) && listStudent[i][1][3] >= 10)) { ligneMDS112.children[j].innerHTML = "Validée" } else if ((listStudent[i][3][0] >= 10)) { ligneMDS112.children[j].innerHTML = "Validée" } else if (listStudent[i][3][0] < 10) { ligneMDS112.children[j].innerHTML = "Non validée" }
            //if (listStudent[i][3][0] >= 20) { ligneMDS112.children[j].innerHTML = "Validée" } else { ligneMDS112.children[j].innerHTML = "Non validée" } 
        } //Mention
        if (j == 7) { ligneMDS112.children[j].innerHTML = mydata[4] } //Session
        if (j == 8) {
            if ((listStudent[i][3][0] >= 7 && listStudent[i][1][3] >= 10) || (listStudent[i][4][0] >= 7 && listStudent[i][1][3] >= 10) || (listStudent[i][3][0] >= 10 || listStudent[i][4][0] >= 10)) { ligneMDS112.children[j].innerHTML = listStudent[i][3][6] } else { ligneMDS112.children[j].innerHTML = 0 }
            //if ((listStudent[i][3][0] + listStudent[i][4][0]) >= 20) { ligneMDS112.children[j].innerHTML = listStudent[i][3][6] } else { ligneMDS112.children[j].innerHTML = 0 } 
        } //nombre_crédits
    }

    //LIGNE MDS112b
    var ligneMDS112b = tbody.children[3]
    for (j = 0; j <= ligneMDS112b.childElementCount - 1; j++) {
        if (j == 2) { ligneMDS112b.children[j].innerHTML = listStudent[i][4][0] } //note info
        if (j == 3) { ligneMDS112b.children[j].innerHTML = listStudent[i][4][1] } //coef info
        if (j == 4) { /*val=ligneMDS112b.children[2].innerHTML*ligneMDS112b.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneMDS112b.children[j].innerHTML = listStudent[i][4][2] } //total note math * coef
        if (j == 5) { ligneMDS112b.children[j].innerHTML = listStudent[i][4][4] } //Rang
        if (j == 6) {
            if (((listStudent[i][4][0] >= 7 && listStudent[i][4][0] < 10) && listStudent[i][1][3] >= 10)) { ligneMDS112b.children[j].innerHTML = "Validée" } else if ((listStudent[i][4][0] >= 10)) { ligneMDS112b.children[j].innerHTML = "Validée" } else if (listStudent[i][3][0] < 10) { ligneMDS112b.children[j].innerHTML = "Non validée" }
            //if (listStudent[i][4][0] >= 10) { ligneMDS112b.children[j].innerHTML = "Validée" } else { ligneMDS112b.children[j].innerHTML = "Non validée" } 
        } //Mention
        if (j == 7) { ligneMDS112b.children[j].innerHTML = mydata[4] } //Session
        //if ((listStudent[i][4][0] >= 7 && listStudent[i][1][3] >= 10) || (listStudent[i][4][0] >= 10)) { ligneMDS112b.children[j].innerHTML = listStudent[i][4][6] } else { ligneMDS112b.children[j].innerHTML = 0 }
        //if(j==8){if( /*ligneMDS112b.children[2].innerHTML>=10*/(ligneMDS112.children[2].innerHTML + ligneMDS112b.children[2].innerHTML) >=20 ){ligneMDS112.children[j].innerHTML = creditUe[2]['nombre_credit']}else{ligneMDS112.children[j].innerHTML = 0}} //nombre_crédits
    }

    //LIGNE MDS113
    var ligneMDS113 = tbody.children[4]
    for (j = 0; j <= ligneMDS113.childElementCount - 1; j++) {
        if (j == 3) { ligneMDS113.children[j].innerHTML = listStudent[i][5][0] } //note math
        if (j == 4) { ligneMDS113.children[j].innerHTML = listStudent[i][5][1] } //coef math
        if (j == 5) { /*val=ligneMDS113.children[3].innerHTML*ligneMDS113.children[4].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneMDS113.children[j].innerHTML = listStudent[i][5][2] } //total note math * coef
        if (j == 6) {
            ligneMDS113.children[j].innerHTML = listStudent[i][5][3]
        } //moyenne donc (totalmath + totalinfo)/2
        if (j == 7) { ligneMDS113.children[j].innerHTML = listStudent[i][5][4] } //Rang
        if (j == 8) {
            if (((listStudent[i][5][0] >= 7 && listStudent[i][5][0] < 10) && listStudent[i][5][3] >= 10)) { ligneMDS113.children[j].innerHTML = "Validée" } else if ((listStudent[i][3][0] >= 10)) { ligneMDS113.children[j].innerHTML = "Validée" } else if (listStudent[i][3][0] < 10) { ligneMDS113.children[j].innerHTML = "Non validée" }
            if (listStudent[i][5][0] >= 10) { ligneMDS113.children[j].innerHTML = "Validée" } else { ligneMDS113.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 9) { ligneMDS113.children[j].innerHTML = mydata[4] }
        if (j == 10) {
            if ((listStudent[i][5][0] >= 7 && listStudent[i][5][3] >= 10) || (listStudent[i][5][0] >= 10)) { ligneMDS113.children[j].innerHTML = listStudent[i][5][6] } else { ligneMDS113.children[j].innerHTML = 0 }
        } //Crédits
    }

    //LINE MDS114
    var ligneMDS114 = tbody.children[5]
    for (j = 0; j <= ligneMDS114.childElementCount - 1; j++) {
        if (j == 2) { ligneMDS114.children[j].innerHTML = listStudent[i][6][0] } //note info
        if (j == 3) { ligneMDS114.children[j].innerHTML = listStudent[i][6][1] } //coef info
        if (j == 4) { /*val=ligneMDS114.children[2].innerHTML*ligneMDS114.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneMDS114.children[j].innerHTML = listStudent[i][6][2] } //total note math * coef
        if (j == 5) { ligneMDS114.children[j].innerHTML = listStudent[i][6][4] } //Rang
        if (j == 6) {
            if (((listStudent[i][6][0] >= 7 && listStudent[i][6][0] < 10) && listStudent[i][5][3] >= 10)) { ligneMDS114.children[j].innerHTML = "Validée" } else if ((listStudent[i][6][0] >= 10)) { ligneMDS114.children[j].innerHTML = "Validée" } else if (listStudent[i][6][0] < 10) { ligneMDS114.children[j].innerHTML = "Non validée" }

        } //Mention
        if (j == 7) { ligneMDS114.children[j].innerHTML = mydata[4] } //Session
        if (j == 8) {
            if ((listStudent[i][6][0] >= 7 && listStudent[i][5][3] >= 10) || (listStudent[i][6][0] >= 10)) { ligneMDS114.children[j].innerHTML = listStudent[i][6][6] } else { ligneMDS114.children[j].innerHTML = 0 }
            //if ((listStudent[i][6][0] >= 7 && listStudent[i][5][3] >= 10) || (listStudent[i][6][0] >= 10)) { ligneMDS114.children[j].innerHTML = listStudent[i][6][6] } else { ligneMDS114.children[j].innerHTML = 0 }
        } //nombre_crédits
    }

    //LINE MDS115
    var ligneMDS115 = tbody.children[6]
    for (j = 0; j <= ligneMDS115.childElementCount - 1; j++) {
        if (j == 2) { ligneMDS115.children[j].innerHTML = listStudent[i][7][0] } //note info
        if (j == 3) { ligneMDS115.children[j].innerHTML = listStudent[i][7][1] } //coef info
        if (j == 4) { /*val=ligneMDS115.children[2].innerHTML*ligneMDS115.children[3].innerHTML; val=val.toFixed(2);val=parseFloat(val);*/ ligneMDS115.children[j].innerHTML = listStudent[i][7][2] } //total note math * coef
        if (j == 5) { ligneMDS115.children[j].innerHTML = listStudent[i][7][4] } //Rang
        if (j == 6) {
            if (((listStudent[i][7][0] >= 7 && listStudent[i][7][0] < 10) && listStudent[i][5][3] >= 10)) { ligneMDS115.children[j].innerHTML = "Validée" } else if ((listStudent[i][7][0] >= 10)) { ligneMDS115.children[j].innerHTML = "Validée" } else if (listStudent[i][7][0] < 10) { ligneMDS115.children[j].innerHTML = "Non validée" }
            //if (listStudent[i][7][0] >= 10) { ligneMDS115.children[j].innerHTML = "Validée" } else { ligneMDS115.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 7) { ligneMDS115.children[j].innerHTML = mydata[4] } //Session
        if (j == 8) {
            if ((listStudent[i][7][0] >= 7 && listStudent[i][5][3] >= 10) || (listStudent[i][7][0] >= 10)) { ligneMDS115.children[j].innerHTML = listStudent[i][7][6] } else { ligneMDS115.children[j].innerHTML = 0 }
            //if (listStudent[i][7][0] >= 10) { ligneMDS115.children[j].innerHTML = listStudent[i][7][6] } else { ligneMDS115.children[j].innerHTML = 0 }
        } //nombre_crédits
    }

    //LINE MD16
    var ligneMDS116 = tbody.children[7]
    for (j = 0; j <= ligneMDS116.childElementCount - 1; j++) {
        if (j == 2) { ligneMDS116.children[j].innerHTML = listStudent[i][8][0] } //note info
        if (j == 3) { ligneMDS116.children[j].innerHTML = listStudent[i][8][1] } //coef info
        if (j == 4) { /*val=ligneMDS116.children[2].innerHTML*ligneMDS116.children[3].innerHTML;val=val.toFixed(2);val=parseFloat(val);*/ ligneMDS116.children[j].innerHTML = listStudent[i][8][2] } //total note math * coef
        if (j == 5) { ligneMDS116.children[j].innerHTML = listStudent[i][8][4] } //Rang
        if (j == 6) {
            if (((listStudent[i][8][0] >= 7 && listStudent[i][8][0] < 10) && listStudent[i][5][3] >= 10)) { ligneMDS116.children[j].innerHTML = "Validée" } else if ((listStudent[i][8][0] >= 10)) { ligneMDS116.children[j].innerHTML = "Validée" } else if (listStudent[i][8][0] < 10) { ligneMDS116.children[j].innerHTML = "Non validée" }
            //if (listStudent[i][8][0] >= 10) { ligneMDS116.children[j].innerHTML = "Validée" } else { ligneMDS116.children[j].innerHTML = "Non validée" } 
        } //Mention
        if (j == 7) { ligneMDS116.children[j].innerHTML = mydata[4] } //Session
        if (j == 8) {
            if ((listStudent[i][8][0] >= 7 && listStudent[i][5][3] >= 10) || (listStudent[i][8][0] >= 10)) { ligneMDS116.children[j].innerHTML = listStudent[i][8][6] } else { ligneMDS116.children[j].innerHTML = 0 }
        } //nombre_crédits
    }

    //LINE 17
    var ligneMDS117 = tbody.children[8]
    for (j = 0; j <= ligneMDS117.childElementCount - 1; j++) {
        if (j == 3) { ligneMDS117.children[j].innerHTML = listStudent[i][9][0] } //note math
        if (j == 4) { ligneMDS117.children[j].innerHTML = listStudent[i][9][1] } //coef math
        if (j == 5) { /*val=ligneMDS117.children[3].innerHTML*ligneMDS117.children[4].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneMDS117.children[j].innerHTML = listStudent[i][9][2] } //total note math * coef
        if (j == 6) {
            ligneMDS117.children[j].innerHTML = listStudent[i][9][3]
                /*Moyenne2( 
                  ligneMDS117.children[5].innerHTML, 
                  mds117b[i]['note_Examen']*coefUe[9]['coefficient'], 
                  coefUe[8]['coefficient']+coefUe[9]['coefficient'] 
                  ) */
        } //moyenne donc (totalmath + totalinfo)/2

        if (j == 7) { ligneMDS117.children[j].innerHTML = listStudent[i][9][4] } //Rang
        if (j == 8) {
            if (((listStudent[i][9][0] >= 7 && listStudent[i][9][0] < 10) && listStudent[i][9][3] >= 10)) { ligneMDS117.children[j].innerHTML = "Validée" } else if ((listStudent[i][9][0] >= 10)) { ligneMDS117.children[j].innerHTML = "Validée" } else if (listStudent[i][9][0] < 10) { ligneMDS117.children[j].innerHTML = "Non validée" }
            //if (listStudent[i][6][0] >= 10) { ligneMDS114.children[j].innerHTML = listStudent[i][6][6] } else { ligneMDS114.children[j].innerHTML = 0 } 
            //if (listStudent[i][9][0] >= 10) { ligneMDS117.children[j].innerHTML = "Validée" } else { ligneMDS117.children[j].innerHTML = "Non validée" } 
        } //Mention
        if (j == 9) { ligneMDS117.children[j].innerHTML = mydata[4] }
        if (j == 10) {
            if ((listStudent[i][9][0] >= 7 && listStudent[i][9][3] >= 10) || (listStudent[i][9][0] >= 10)) { ligneMDS117.children[j].innerHTML = listStudent[i][9][6] } else { ligneMDS117.children[j].innerHTML = 0 }
            //if ((listStudent[i][9][0]) >= 10) { ligneMDS117.children[j].innerHTML = listStudent[i][9][6] } else { ligneMDS117.children[j].innerHTML = 0 } 
        } //Crédits
    }

    //LINE 17b
    var ligneMDS117b = tbody.children[9]
    for (j = 0; j <= ligneMDS117b.childElementCount - 1; j++) {
        if (j == 2) { ligneMDS117b.children[j].innerHTML = listStudent[i][10][0] } //note math
        if (j == 3) { ligneMDS117b.children[j].innerHTML = listStudent[i][10][1] } //coef math
        if (j == 4) { ligneMDS117b.children[j].innerHTML = listStudent[i][10][2] } //total note math * coef
        if (j == 5) { ligneMDS117b.children[j].innerHTML = listStudent[i][10][4] } //Rang
        if (j == 6) {
            if (((listStudent[i][10][0] >= 7 && listStudent[i][10][0] < 10) && listStudent[i][9][3] >= 10)) { ligneMDS117b.children[j].innerHTML = "Validée" } else if ((listStudent[i][10][0] >= 10)) { ligneMDS117b.children[j].innerHTML = "Validée" } else if (listStudent[i][10][0] < 10) { ligneMDS117b.children[j].innerHTML = "Non validée" }
            //if (listStudent[i][10][0] >= 10) { ligneMDS117b.children[j].innerHTML = "Validée" } else { ligneMDS117b.children[j].innerHTML = "Non validée" } 
        } //Mention
        if (j == 7) { ligneMDS117b.children[j].innerHTML = mydata[4] } //Session
        if (j == 8) {
            if ((listStudent[i][10][0] >= 7 && listStudent[i][9][3] >= 10) || (listStudent[i][10][0] >= 10)) { ligneMDS117b.children[j].innerHTML = listStudent[i][10][6] } else { ligneMDS117b.children[j].innerHTML = 0 }
        } //Credit

    }

    //LINE DEs RESULTATS
    resultat = tbody.children[10]
    resultat.style.backgroundColor = "#C7B54D"
    for (j = 0; j <= resultat.childElementCount - 1; j++) {
        if (j == 1) {
            resultat.children[1].innerHTML = listStudent[i][11][0] /*sommeInt1(ligneMDS111.children[5].innerHTML,ligneMDS111b.children[3].innerHTML,ligneMDS112.children[3].innerHTML,ligneMDS112b.children[3].innerHTML,ligneMDS113.children[4].innerHTML,ligneMDS114.children[3].innerHTML,ligneMDS115.children[3].innerHTML,ligneMDS116.children[3].innerHTML,ligneMDS117.children[4].innerHTML,ligneMDS117b.children[3].innerHTML);*/
        }
        if (j == 2) { resultat.children[2].innerHTML = listStudent[i][11][1] } /*sommeFloat(ligneMDS111b.children[4].innerHTML, ligneMDS111.children[6].innerHTML, ligneMDS112.children[4].innerHTML, ligneMDS113.children[5].innerHTML, ligneMDS114.children[4].innerHTML, ligneMDS115.children[4].innerHTML,ligneMDS116.children[4].innerHTML, ligneMDS117.children[5].innerHTML, ligneMDS112b.children[4].innerHTML, ligneMDS117b.children[4].innerHTML) }*/
        if (j == 3) { /*val = resultat.children[2].innerHTML / resultat.children[1].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ resultat.children[j].innerHTML = listStudent[i][11][2] }
        if (j == 4) { resultat.children[j].innerHTML = mydata[2].indexOf(listStudent[i][11][2]) + 1 /** "SDF" */ }
        if (j == 6) { resultat.children[j].innerHTML = sommeIntmds(ligneMDS111.children[11].innerHTML, ligneMDS112.children[8].innerHTML, ligneMDS113.children[10].innerHTML, ligneMDS114.children[8].innerHTML, ligneMDS115.children[8].innerHTML, ligneMDS116.children[8].innerHTML, ligneMDS117.children[10].innerHTML, ligneMDS117b.children[8].innerHTML) } /**TOtal Crédit */
    }

    //Tbody
    var body3 = clone.children[2].children[2].children[1].children[1]

    //LIGNE 0
    var ligne0 = body3.children[0]
    for (j = 0; j <= ligne0.childElementCount - 1; j++) {
        if (j == 2) { ligne0.children[2].innerHTML = `${resultat.children[3].innerHTML} / 20` }
        if (j == 4) { ligne0.children[j].innerHTML = `${mydata[2][0]} / 20` }
    }

    //LIGNE 1
    var ligne1 = body3.children[1]
    for (j = 0; j <= ligne1.childElementCount - 1; j++) {
        if (j == 2) { ligne1.children[j].innerHTML = `${mydata[3]} / 20` }
        if (j == 4) {
            v = mydata[2].length - 1;
            ligne1.children[j].innerHTML = `${mydata[2][v]} / 20`
        }
    }

    //LLIGNE 2
    var ligne2 = body3.children[2]
    for (j = 0; j <= ligne1.childElementCount - 1; j++) {
        if (j == 5) { ligne2.children[j].innerHTML = `${mydata[2].indexOf(listStudent[i][11][2])+1} sur ${mydata[1].length}` }
        if (j == 4) {}
    }

    /********************************************************************************* SEMESTRE 2 MDS1 LIGNE *************************************************************************************************/

    data = mydata[7][0]
    s2mds = clone.childNodes[2].children[3]
    s2mdsbody = s2mds.children[0].children[1]



    //LIGNE 1
    var ligne11 = s2mdsbody.children[0]
    ligne11.children[0].innerHTML = "SEMESTRE 2"
    ligne11.children[2].innerHTML = "MDS121"
    ligne11.children[3].innerHTML = "Mathématiques II"

    for (j = 0; j <= ligne11.childElementCount - 1; j++) {
        if (j == 4) { ligne11.children[j].innerHTML = data[i][1][0] }
        if (j == 5) { ligne11.children[j].innerHTML = data[i][1][1] }
        if (j == 6) { ligne11.children[j].innerHTML = data[i][1][2] }
        if (j == 7) { ligne11.children[j].innerHTML = data[i][1][3] }
        if (j == 8) { ligne11.children[j].innerHTML = data[i][1][4] }
        if (j == 9) {
            if (((data[i][1][0] >= 7 && data[i][1][0] < 10) && data[i][1][3] >= 10)) { ligne11.children[j].innerHTML = "Validée" } else if ((data[i][1][0] >= 10)) { ligne11.children[j].innerHTML = "Validée" } else if (data[i][1][0] < 10) { ligne11.children[j].innerHTML = "Non validée" }
            //if (data[i][1][5]) { ligne11.children[j].innerHTML = "Validée" } else { ligne11.children[j].innerHTML = "Non validée" }
        }
        if (j == 10) { if (data[i][1][8]) { ligne11.children[j].innerHTML = 'Rattrapage' } else { ligne11.children[j].innerHTML = mydata[8] } }
        if (j == 11) { if ((data[i][1][0] + data[i][2][0]) >= 20) { ligne11.children[j].innerHTML = data[i][1][7] } else { ligne11.children[j].innerHTML = 0 } }
    }

    //LIGNE 2
    var ligne22 = s2mdsbody.children[1]
    ligne22.children[0].innerHTML = "MDS121"
    ligne22.children[1].innerHTML = "Informatique II"

    for (j = 0; j <= ligne22.childElementCount - 1; j++) {
        if (j == 2) { ligne22.children[j].innerHTML = data[i][2][0] }
        if (j == 3) { ligne22.children[j].innerHTML = data[i][2][1] }
        if (j == 4) { ligne22.children[j].innerHTML = data[i][2][2] }
        if (j == 5) { ligne22.children[j].innerHTML = data[i][2][4] }
        if (j == 6) {
            if (((data[i][2][0] >= 7 && data[i][2][0] < 10) && data[i][1][3] >= 10)) { ligne22.children[j].innerHTML = "Validée" } else if ((data[i][2][0] >= 10)) { ligne22.children[j].innerHTML = "Validée" } else if (data[i][2][0] < 10) { ligne22.children[j].innerHTML = "Non validée" }
            //if (data[i][2][5]) { ligne22.children[j].innerHTML = "Validée" } else { ligne22.children[j].innerHTML = "Non validée" } 
        }
        if (j == 7) { if (data[i][2][8]) { ligne22.children[j].innerHTML = 'Rattrapage' } else { ligne22.children[j].innerHTML = mydata[8] } }
    }

    //LIGNE 3
    var ligne33 = s2mdsbody.children[2]
    ligne33.children[0].innerHTML = "MDS122"
    ligne33.children[1].innerHTML = "Mathématiques financières II"

    for (j = 0; j <= ligne33.childElementCount - 1; j++) {
        if (j == 2) { ligne33.children[j].innerHTML = data[i][3][0] }
        if (j == 3) { ligne33.children[j].innerHTML = data[i][3][1] }
        if (j == 4) { ligne33.children[j].innerHTML = data[i][3][2] }
        if (j == 5) { ligne33.children[j].innerHTML = data[i][3][4] }
        if (j == 6) {
            if (((data[i][3][0] >= 7 && data[i][3][0] < 10) && data[i][1][3] >= 10)) { ligne33.children[j].innerHTML = "Validée" } else if ((data[i][3][0] >= 10)) { ligne33.children[j].innerHTML = "Validée" } else if (data[i][3][0] < 10) { ligne33.children[j].innerHTML = "Non validée" }
            //if (data[i][3][5]) { ligne33.children[j].innerHTML = "Validée" } else { ligne33.children[j].innerHTML = "Non validée" } 
        }
        if (j == 7) { if (data[i][3][8]) { ligne33.children[j].innerHTML = 'Rattrapage' } else { ligne33.children[j].innerHTML = mydata[8] } }
        if (j == 8) { if ((data[i][3][0] + data[i][4][0]) >= 20) { ligne33.children[j].innerHTML = data[i][3][6] } else { ligne33.children[j].innerHTML = 0 } }
    }

    //LIGNE 4
    var ligne44 = s2mdsbody.children[3]
    ligne44.children[0].innerHTML = "MDS122"
    ligne44.children[1].innerHTML = "Statistiques descriptives II"

    for (j = 0; j <= ligne44.childElementCount - 1; j++) {
        if (j == 2) { ligne44.children[j].innerHTML = data[i][4][0] }
        if (j == 3) { ligne44.children[j].innerHTML = data[i][4][1] }
        if (j == 4) { ligne44.children[j].innerHTML = data[i][4][2] }
        if (j == 5) { ligne44.children[j].innerHTML = data[i][3][4] }
        if (j == 6) {
            if (((data[i][2][0] >= 7 && data[i][4][0] < 10) && data[i][1][3] >= 10)) { ligne44.children[j].innerHTML = "Validée" } else if ((data[i][4][0] >= 10)) { ligne44.children[j].innerHTML = "Validée" } else if (data[i][4][0] < 10) { ligne44.children[j].innerHTML = "Non validée" }
        }
        if (j == 7) { if (data[i][4][8]) { ligne44.children[j].innerHTML = 'Rattrapage' } else { ligne44.children[j].innerHTML = mydata[8] } }
        //if (j == 8) { if ((data[i][3][0] + data[i][4][0]) >= 20) { ligne44.children[j].innerHTML = data[i][3][7] } else { ligne44.children[j].innerHTML = 0 } }
    }

    //LIGNE 5
    var ligne55 = s2mdsbody.children[4]
    ligne55.children[1].innerHTML = "MDS123"
    ligne55.children[2].innerHTML = "Environnement juridique et comptable II"

    for (j = 0; j <= ligne55.childElementCount - 1; j++) {
        if (j == 3) { ligne55.children[j].innerHTML = data[i][5][0] }
        if (j == 4) { ligne55.children[j].innerHTML = data[i][5][1] }
        if (j == 5) { ligne55.children[j].innerHTML = data[i][5][2] }
        if (j == 6) { ligne55.children[j].innerHTML = data[i][5][3] }
        if (j == 7) { ligne55.children[j].innerHTML = data[i][5][4] }
        if (j == 8) {
            if (((data[i][5][0] >= 7 && data[i][5][0] < 10) && data[i][5][3] >= 10)) { ligne55.children[j].innerHTML = "Validée" } else if ((data[i][5][0] >= 10)) { ligne55.children[j].innerHTML = "Validée" } else if (data[i][5][0] < 10) { ligne55.children[j].innerHTML = "Non validée" }
            //if (data[i][5][5]) { ligne55.children[j].innerHTML = "Validée" } else { ligne55.children[j].innerHTML = "Non validée" } 
        }
        if (j == 9) { if (data[i][5][8]) { ligne55.children[j].innerHTML = 'Rattrapage' } else { ligne55.children[j].innerHTML = mydata[8] } }
        if (j == 10) {
            if ((data[i][5][0] >= 7 && data[i][5][3] >= 10) || (data[i][5][0] >= 10)) { ligne55.children[j].innerHTML = data[i][5][6] } else { ligne55.children[j].innerHTML = 0 } //Crédits
            //ligne55.children[j].innerHTML = data[i][5][7] 
        }
    }

    //LIGNE 6
    var ligne66 = s2mdsbody.children[5]
    ligne66.children[0].innerHTML = "MDS124"
    ligne66.children[1].innerHTML = "Management des ressources humaines et Méthodologie"

    for (j = 0; j <= ligne66.childElementCount - 1; j++) {
        if (j == 2) { ligne66.children[j].innerHTML = data[i][6][0] }
        if (j == 3) { ligne66.children[j].innerHTML = data[i][6][1] }
        if (j == 4) { ligne66.children[j].innerHTML = data[i][6][2] }
        if (j == 5) { ligne66.children[j].innerHTML = data[i][6][4] }
        if (j == 6) { if (data[i][6][5]) { ligne66.children[j].innerHTML = 'Validée' } else { ligne66.children[j].innerHTML = 'Non validée' } }
        if (j == 7) { if (data[i][6][8]) { ligne66.children[j].innerHTML = 'Rattrapage' } else { ligne66.children[j].innerHTML = mydata[8] } }
        if (j == 8) {
            if ((data[i][6][0] >= 7 && data[i][5][3] >= 10) || (data[i][6][0] >= 10)) { ligne66.children[j].innerHTML = data[i][6][6] } else { ligne66.children[j].innerHTML = 0 } //Crédits
            //ligne66.children[j].innerHTML = data[i][6][7] 
        }
        //if (j == 9) {}
    }

    //LIGNE 7
    var ligne77 = s2mdsbody.children[6]
    ligne77.children[0].innerHTML = "MDS125"
    ligne77.children[1].innerHTML = "Outils de gestion du sport II"

    for (j = 0; j <= ligne77.childElementCount - 1; j++) {
        if (j == 2) { ligne77.children[j].innerHTML = data[i][7][0] }
        if (j == 3) { ligne77.children[j].innerHTML = data[i][7][1] }
        if (j == 4) { ligne77.children[j].innerHTML = data[i][7][2] }
        if (j == 5) { ligne77.children[j].innerHTML = data[i][7][4] }
        if (j == 6) {
            if (((data[i][7][0] >= 7 && data[i][7][0] < 10) && data[i][5][3] >= 10)) { ligne77.children[j].innerHTML = "Validée" } else if ((data[i][7][0] >= 10)) { ligne77.children[j].innerHTML = "Validée" } else if (data[i][7][0] < 10) { ligne77.children[j].innerHTML = "Non validée" }
            //if (data[i][5][5]) { ligne55.children[j].innerHTML = "Validée" } else { ligne55.children[j].innerHTML = "Non validée" }
        }
        if (j == 7) { if (data[i][7][8]) { ligne77.children[j].innerHTML = 'Rattrapage' } else { ligne77.children[j].innerHTML = mydata[8] } }

        if (j == 8) {
            if ((data[i][7][0] >= 7 && data[i][5][3] >= 10) || (data[i][7][0] >= 10)) { ligne77.children[j].innerHTML = data[i][7][6] } else { ligne77.children[j].innerHTML = 0 } //Crédits
            //ligne77.children[j].innerHTML = data[i][7][7] 
        }
    }

    //LIGNE 8
    var ligne88 = s2mdsbody.children[7]
    ligne88.children[0].innerHTML = "MDS126"
    ligne88.children[1].innerHTML = "Gestion des structures et organisations sportives II"

    for (j = 0; j <= ligne88.childElementCount - 1; j++) {
        if (j == 2) { ligne88.children[j].innerHTML = data[i][8][0] }
        if (j == 3) { ligne88.children[j].innerHTML = data[i][8][1] }
        if (j == 4) { ligne88.children[j].innerHTML = data[i][8][2] }
        if (j == 5) { ligne88.children[j].innerHTML = data[i][8][4] }
        if (j == 6) { if (data[i][8][5]) { ligne88.children[j].innerHTML = 'Validée' } else { ligne88.children[j].innerHTML = 'Non validée' } }
        if (j == 7) { if (data[i][8][8]) { ligne88.children[j].innerHTML = 'Rattrapage' } else { ligne88.children[j].innerHTML = mydata[8] } }
        if (j == 8) { ligne88.children[j].innerHTML = data[i][8][7] }
    }

    //LIGNE 9
    var ligne99 = s2mdsbody.children[8]
        //ligne99.children[0].innerHTML = "MDS127"
    ligne99.children[1].innerHTML = "MDS127"
    ligne99.children[2].innerHTML = "Technique d'expression anglaise"

    for (j = 0; j <= ligne99.childElementCount - 1; j++) {
        if (j == 3) { ligne99.children[j].innerHTML = data[i][9][0] }
        if (j == 4) { ligne99.children[j].innerHTML = data[i][9][1] }
        if (j == 5) { ligne99.children[j].innerHTML = data[i][9][2] }
        if (j == 6) { ligne99.children[j].innerHTML = data[i][9][3] }
        if (j == 7) { ligne99.children[j].innerHTML = data[i][9][4] }
        if (j == 8) { if (data[i][9][5]) { ligne99.children[j].innerHTML = 'Validée' } else { ligne99.children[j].innerHTML = 'Non validée' } }
        if (j == 9) { if (data[i][9][8]) { ligne99.children[j].innerHTML = 'Rattrapage' } else { ligne99.children[j].innerHTML = mydata[8] } }
        if (j == 10) { ligne99.children[j].innerHTML = data[i][9][7] }
    }

    //LIGNE 10
    var ligne100 = s2mdsbody.children[9]
    ligne100.children[0].innerHTML = "MDS127"
    ligne100.children[1].innerHTML = "Technique d'expression française"

    for (j = 0; j <= ligne100.childElementCount - 1; j++) {
        if (j == 2) { ligne100.children[j].innerHTML = data[i][10][0] }
        if (j == 3) { ligne100.children[j].innerHTML = data[i][10][1] }
        if (j == 4) { ligne100.children[j].innerHTML = data[i][10][2] }
        if (j == 5) { ligne100.children[j].innerHTML = data[i][10][4] }
        if (j == 6) { if (data[i][10][5]) { ligne100.children[j].innerHTML = 'Validée' } else { ligne100.children[j].innerHTML = 'Non validée' } }
        if (j == 7) { if (data[i][10][8]) { ligne100.children[j].innerHTML = 'Rattrapage' } else { ligne100.children[j].innerHTML = mydata[8] } }
        if (j == 8) { ligne100.children[j].innerHTML = data[i][10][7] }
    }
    //style
    ligne100.setAttribute('class', 'line10')


    //LIGNE 11
    s2mdsResult = s2mdsbody.children[10]
    s2mdsResult.style.backgroundColor = "#C7B54D"
    s2mdsResult.children[0].innerHTML = "RESULTATS SEMESTRE 2"
    s2mdsResult.children[5].innerHTML = "Total Crédits Semestre 2"

    for (j = 0; j <= s2mdsResult.childElementCount - 1; j++) {
        if (j == 1) { s2mdsResult.children[j].innerHTML = data[i][11][0] }
        if (j == 2) { s2mdsResult.children[j].innerHTML = data[i][11][1] }
        if (j == 3) { s2mdsResult.children[j].innerHTML = data[i][11][2] }
        if (j == 4) { s2mdsResult.children[j].innerHTML = mydata[7][1].indexOf(data[i][11][2]) + 1 }
        if (j == 6) {
            s2mdsResult.children[j].innerHTML = sommeIntmds(ligne11.children[11].innerHTML, ligne33.children[8].innerHTML, ligne55.children[10].innerHTML, ligne66.children[8].innerHTML, ligne77.children[8].innerHTML, ligne88.children[8].innerHTML, ligne99.children[10].innerHTML, ligne100.children[8].innerHTML) //(data[i][1][7] + data[i][3][7] + data[i][5][7] + data[i][6][7] + data[i][7][7] + data[i][8][7] + data[i][9][7] + data[i][10][7])
                //(data[i][1][7] + data[i][3][7] + data[i][5][7] + data[i][6][7] + data[i][7][7] + data[i][8][7] + data[i][9][7] + data[i][10][7]) }
        }
    }
    /**RESULTATS S1 & S2 MDS */
    /*bx = document.getElementById('recpas1s2')
    s1s2mds = bx.cloneNode(true)

    s1s2mdsvisa = document.getElementById('visa')
    s1s2mdsvisa = s1s2mdsvisa.cloneNode(true)*/
    s1s2mdsrecap = clone.children[2].children[4].children[1].children[1]
        //s1s2mdsrecap.style.backgroundColor = "#C7B54D"
        // = tmps1s2mds.cloneNode(true)

    for (j = 0; j <= s1s2mdsrecap.childElementCount - 1; j++) {
        if (j == 0) { s1s2mdsrecap.children[j].innerHTML = sommeInt2(resultat.children[1].innerHTML, s2mdsResult.children[1].innerHTML) }
        if (j == 1) { s1s2mdsrecap.children[j].innerHTML = sommeFloat2(resultat.children[2].innerHTML, s2mdsResult.children[2].innerHTML) }
        if (j == 2) { s1s2mdsrecap.children[j].innerHTML = `${(parseFloat(s1s2mdsrecap.children[1].innerHTML) / s1s2mdsrecap.children[0].innerHTML).toFixed(2)} / 20` }
        if (j == 3) {
            var total = parseFloat(s1s2mdsrecap.children[1].innerHTML)
            s1s2mdsrecap.children[j].innerHTML = `${mydata[7][2].indexOf(total) + 1}  /  ${data.length}`
        }
        if (j == 4) { s1s2mdsrecap.children[j].innerHTML = `${ sommeInt2(resultat.lastChild.innerHTML, s2mdsResult.lastChild.innerHTML) }  /  60` }
        if (j == 5) {
            var moyenne = parseFloat(s1s2mdsrecap.children[2].innerHTML)
            if (moyenne >= 10) { s1s2mdsrecap.children[j].innerHTML = "ADMIS(E)" } else { s1s2mdsrecap.children[j].innerHTML = "REFUSE(E)" }
        }
    }

    return (clone)
}


/**FONCTION BULL 1er SEMESTRE */

/**FONCTION BULLETIN STAPS1 */
function BullSTAPS1(clone, i, mydata) {

    //DONNEES RECUPEREES DE LA BD
    listStudent = mydata[1]

    //Info Utilisateur
    info1 = clone.children[2].children[1].children[0]
    info1.children[2].innerHTML = info1.children[2].innerHTML + ` ${listStudent[i][0]['nom']}`
    info1.children[3].innerHTML = info1.children[3].innerHTML + ` ${listStudent[i][0]['prenom']}`

    info2 = clone.children[2].children[1].children[1]
    info2.children[1].innerHTML = info2.children[1].innerHTML + ` ${listStudent[i][0]['matricule']}`
    info2.children[2].innerHTML = info2.children[2].innerHTML + ` ${listStudent[i][0]['date_naissance']}`
    info2.children[3].innerHTML = info2.children[3].innerHTML + ` ${listStudent[i][0]['lieu_naissance']}`
    info2.children[4].innerHTML = info2.children[4].innerHTML + ` 2022-2023`

    //RESULTATS
    var tbody = clone.children[2].children[2].children[0].children[1]

    //LIGNE EPS111
    var ligneEPS111 = tbody.children[0]
    for (j = 0; j <= ligneEPS111.childElementCount - 1; j++) {
        if (j == 4) { ligneEPS111.children[j].innerHTML = listStudent[i][1][0] } //note 
        if (j == 5) { ligneEPS111.children[j].innerHTML = listStudent[i][1][1] } //coef
        if (j == 6) {
            val = ligneEPS111.children[4].innerHTML * ligneEPS111.children[5].innerHTML;
            val = val.toFixed(2);
            val = parseFloat(val);
            ligneEPS111.children[j].innerHTML = val
        } //total note  * coef
        if (j == 7) { ligneEPS111.children[j].innerHTML = listStudent[i][1][3] } //moyenne donc (totalmath + totalinfo)/2
        if (j == 8) { ligneEPS111.children[j].innerHTML = listStudent[i][1][4] } //Rang
        if (j == 9) {
            if (((listStudent[i][1][0] >= 7 && listStudent[i][1][0] < 10) && listStudent[i][1][3] >= 10)) { ligneEPS111.children[j].innerHTML = "Validée" } else if ((listStudent[i][1][0] >= 10)) { ligneEPS111.children[j].innerHTML = "Validée" } else if (listStudent[i][1][0] < 10) { ligneEPS111.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 10) { ligneEPS111.children[j].innerHTML = mydata[4] } //Session
        if (j == 11) {
            if ((listStudent[i][1][0] >= 7 && listStudent[i][1][2] >= 10) || (listStudent[i][1][0] >= 10)) { ligneEPS111.children[j].innerHTML = listStudent[i][1][6] } else { ligneEPS111.children[j].innerHTML = 0 }
        } //Crédits
    }

    //LIGNE EPS112
    ligneEPS112 = tbody.children[1]
    for (j = 0; j <= ligneEPS112.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS112.children[j].innerHTML = listStudent[i][2][0] } //note info
        if (j == 3) { ligneEPS112.children[j].innerHTML = listStudent[i][2][1] } //coef info
        if (j == 4) { ligneEPS112.children[j].innerHTML = listStudent[i][2][2] } //val=ligneEPS112.children[2].innerHTML*ligneEPS112.children[3].innerHTML; val= val.toFixed(2); val = parseFloat(val); ligneEPS112.children[j].innerHTML = val}//total note math * coef
        if (j == 5) { ligneEPS112.children[j].innerHTML = listStudent[i][2][4] } //Rang
        if (j == 6) {
            //if (listStudent[i][2][5]) { ligneEPS112.children[6].innerHTML = "Validée" } else { ligneEPS112.children[6].innerHTML = "Non validée" }
            if (((listStudent[i][2][0] >= 7 && listStudent[i][2][0] < 10) && listStudent[i][1][3] >= 10)) { ligneEPS112.children[j].innerHTML = "Validée" } else if ((listStudent[i][2][0] >= 10)) { ligneEPS112.children[j].innerHTML = "Validée" } else if (listStudent[i][2][0] < 10) { ligneEPS112.children[j].innerHTML = "Non validée" }
        }
        if (j == 7) { ligneEPS112.children[j].innerHTML = mydata[4] } //Session
        if (j == 8) {
            //if (listStudent[i][2][5]) { ligneEPS112.children[j].innerHTML = listStudent[i][2][6] } else { ligneEPS112.children[j].innerHTML = 0 } 
            if ((listStudent[i][2][0] >= 7 && listStudent[i][1][2] >= 10) || (listStudent[i][2][0] >= 10)) { ligneEPS112.children[j].innerHTML = listStudent[i][2][6] } else { ligneEPS112.children[j].innerHTML = 0 }
        } //Crédits
    }

    //LIGNE EPS113
    var ligneEPS113 = tbody.children[2]
    for (j = 0; j <= ligneEPS113.childElementCount - 1; j++) {
        if (j == 3) { ligneEPS113.children[j].innerHTML = listStudent[i][3][0] } //note info
        if (j == 4) { ligneEPS113.children[j].innerHTML = listStudent[i][3][1] } //coef info
        if (j == 5) {
            val = ligneEPS113.children[2].innerHTML * ligneEPS113.children[3].innerHTML;
            val = val.toFixed(2);
            val = parseFloat(val);
            ligneEPS113.children[j].innerHTML = listStudent[i][3][2]
        } //total note math * coef
        if (j == 6) { ligneEPS113.children[j].innerHTML = listStudent[i][3][3] } //
        if (j == 7) { ligneEPS113.children[j].innerHTML = listStudent[i][3][4] }
        if (j == 8) {
            if (((listStudent[i][3][0] >= 7 && listStudent[i][3][0] < 10) && listStudent[i][3][3] >= 10)) { ligneEPS113.children[j].innerHTML = "Validée" } else if ((listStudent[i][2][0] >= 10)) { ligneEPS113.children[j].innerHTML = "Validée" } else if (listStudent[i][3][0] < 10) { ligneEPS113.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 9) { ligneEPS113.children[j].innerHTML = mydata[4] } // Session
        if (j == 10) {
            if ((listStudent[i][3][0] >= 7 && listStudent[i][3][3] >= 10) || (listStudent[i][3][0] >= 10)) { ligneEPS113.children[j].innerHTML = listStudent[i][3][6] } else { ligneEPS113.children[j].innerHTML = 0 }
        } //nombre_crédits
    }

    //LIGNE EPS114
    var ligneEPS114 = tbody.children[3]
    for (j = 0; j <= ligneEPS114.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS114.children[j].innerHTML = listStudent[i][4][0] } //note info
        if (j == 3) { ligneEPS114.children[j].innerHTML = listStudent[i][4][1] } //coef info
        if (j == 4) { /*val=ligneEPS114.children[2].innerHTML*ligneEPS114.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS114.children[j].innerHTML = listStudent[i][4][2] } //total note math * coef
        if (j == 5) { ligneEPS114.children[j].innerHTML = listStudent[i][4][4] } //
        if (j == 6) {
            if (((listStudent[i][4][0] >= 7 && listStudent[i][4][0] < 10) && listStudent[i][3][3] >= 10)) { ligneEPS114.children[j].innerHTML = "Validée" } else if ((listStudent[i][4][0] >= 10)) { ligneEPS114.children[j].innerHTML = "Validée" } else if (listStudent[i][4][0] < 10) { ligneEPS114.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 7) { ligneEPS114.children[j].innerHTML = mydata[4] } //session
        if (j == 8) {
            if ((listStudent[i][4][0] >= 7 && listStudent[i][3][3] >= 10) || (listStudent[i][4][0] >= 10)) { ligneEPS114.children[j].innerHTML = listStudent[i][4][6] } else { ligneEPS114.children[j].innerHTML = 0 }
        } //nombre_crédits
    }

    //LIGNE EPS115a
    var ligneEPS115a = tbody.children[4]
    for (j = 0; j <= ligneEPS115a.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS115a.children[j].innerHTML = listStudent[i][5][0] } //note info
        if (j == 3) { ligneEPS115a.children[j].innerHTML = listStudent[i][5][1] } //coef info
        if (j == 4) { /*val=ligneEPS115a.children[2].innerHTML*ligneEPS115a.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS115a.children[j].innerHTML = listStudent[i][5][2] } //total note math * coef
        if (j == 5) { ligneEPS115a.children[j].innerHTML = listStudent[i][5][4] } //
        if (j == 6) {
            if (((listStudent[i][5][0] >= 7 && listStudent[i][5][0] < 10) && listStudent[i][3][3] >= 10)) { ligneEPS115a.children[j].innerHTML = "Validée" } else if ((listStudent[i][5][0] >= 10)) { ligneEPS115a.children[j].innerHTML = "Validée" } else if (listStudent[i][5][0] < 10) { ligneEPS115a.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 7) { ligneEPS115a.children[j].innerHTML = mydata[4] } //session
        if (j == 8) {
            if ((listStudent[i][5][0] >= 7 && listStudent[i][3][3] >= 10) || (listStudent[i][5][0] >= 10)) { ligneEPS115a.children[j].innerHTML = listStudent[i][5][6] } else { ligneEPS115a.children[j].innerHTML = 0 }
        } //nombre_crédits
    }

    //LIGNE EPS115b
    var ligneEPS115b = tbody.children[5]
    for (j = 0; j <= ligneEPS115b.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS115b.children[j].innerHTML = listStudent[i][6][0] } //note info
        if (j == 3) { ligneEPS115b.children[j].innerHTML = listStudent[i][6][1] } //coef info
        if (j == 4) { /*val=ligneEPS115b.children[2].innerHTML*ligneEPS115b.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS115b.children[j].innerHTML = listStudent[i][6][2] } //total note math * coef
        if (j == 5) { ligneEPS115b.children[j].innerHTML = listStudent[i][5][4] } //
        if (j == 6) {
            if (((listStudent[i][6][0] >= 7 && listStudent[i][6][0] < 10) && listStudent[i][3][3] >= 10)) { ligneEPS115b.children[j].innerHTML = "Validée" } else if ((listStudent[i][6][0] >= 10)) { ligneEPS115b.children[j].innerHTML = "Validée" } else if (listStudent[i][6][0] < 10) { ligneEPS115b.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 7) { ligneEPS115b.children[j].innerHTML = mydata[4] } //session
        if (j == 8) {
            if ((listStudent[i][6][0] >= 7 && listStudent[i][3][3] >= 10) || (listStudent[i][6][0] >= 10)) { ligneEPS115b.children[j].innerHTML = listStudent[i][6][6] } else { ligneEPS115b.children[j].innerHTML = 0 }
        } //nombre_crédits
    }

    //LIGNE EPS115j
    var ligneEPS115j = tbody.children[6]
    for (j = 0; j <= ligneEPS115j.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS115j.children[j].innerHTML = listStudent[i][7][0] } //note info
        if (j == 3) { ligneEPS115j.children[j].innerHTML = listStudent[i][7][1] } //coef info
        if (j == 4) { /*val=ligneEPS115j.children[2].innerHTML*ligneEPS115j.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS115j.children[j].innerHTML = listStudent[i][7][2] } //total note math * coef
        if (j == 5) { ligneEPS115j.children[j].innerHTML = listStudent[i][7][4] } //
        if (j == 6) {
            if (((listStudent[i][7][0] >= 7 && listStudent[i][7][0] < 10) && listStudent[i][3][3] >= 10)) { ligneEPS115j.children[j].innerHTML = "Validée" } else if ((listStudent[i][7][0] >= 10)) { ligneEPS115j.children[j].innerHTML = "Validée" } else if (listStudent[i][7][0] < 10) { ligneEPS115j.children[j].innerHTML = "Non validée" }
            //if (listStudent[i][7][5]) { ligneEPS115j.children[j].innerHTML = "Validée" } else { ligneEPS115j.children[j].innerHTML = "Non validée" } 
        } //Mention
        if (j == 7) { ligneEPS115j.children[j].innerHTML = mydata[4] } //session
        if (j == 8) {
            if ((listStudent[i][7][0] >= 7 && listStudent[i][3][3] >= 10) || (listStudent[i][7][0] >= 10)) { ligneEPS115j.children[j].innerHTML = listStudent[i][7][6] } else { ligneEPS115j.children[j].innerHTML = 0 }
        } //nombre_crédits
    }

    //LIGNE EPS115l
    var ligneEPS115l = tbody.children[7]
    for (j = 0; j <= ligneEPS115l.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS115l.children[j].innerHTML = listStudent[i][8][0] } //note info
        if (j == 3) { ligneEPS115l.children[j].innerHTML = listStudent[i][8][1] } //coef info
        if (j == 4) { /*val=ligneEPS115l.children[2].innerHTML*ligneEPS115l.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS115l.children[j].innerHTML = listStudent[i][8][2] } //total note math * coef
        if (j == 5) { ligneEPS115l.children[j].innerHTML = listStudent[i][8][4] } //
        if (j == 6) {
            if (((listStudent[i][8][0] >= 7 && listStudent[i][8][0] < 10) && listStudent[i][3][3] >= 10)) { ligneEPS115l.children[j].innerHTML = "Validée" } else if ((listStudent[i][8][0] >= 10)) { ligneEPS115l.children[j].innerHTML = "Validée" } else if (listStudent[i][8][0] < 10) { ligneEPS115l.children[j].innerHTML = "Non validée" }
            //if (listStudent[i][8][5]) { ligneEPS115l.children[j].innerHTML = "Validée" } else { ligneEPS115l.children[j].innerHTML = "Non validée" } 
        } //Mention
        if (j == 7) { ligneEPS115l.children[j].innerHTML = mydata[4] } //session
        if (j == 8) {
            if ((listStudent[i][8][0] >= 7 && listStudent[i][3][3] >= 10) || (listStudent[i][8][0] >= 10)) { ligneEPS115l.children[j].innerHTML = listStudent[i][8][6] } else { ligneEPS115l.children[j].innerHTML = 0 }
        } //nombre_crédits
    }

    //LIGNE EPS116
    var ligneEPS116 = tbody.children[8]
    for (j = 0; j <= ligneEPS116.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS116.children[j].innerHTML = listStudent[i][9][0] } //note info
        if (j == 3) { ligneEPS116.children[j].innerHTML = listStudent[i][9][1] } //coef info
        if (j == 4) { /*val=ligneEPS116.children[2].innerHTML*ligneEPS116.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS116.children[j].innerHTML = listStudent[i][9][2] } //total note math * coef
        if (j == 5) { ligneEPS116.children[j].innerHTML = listStudent[i][9][4] } //
        if (j == 6) {
            if (((listStudent[i][8][0] >= 7 && listStudent[i][9][0] < 10) && listStudent[i][3][3] >= 10)) { ligneEPS116.children[j].innerHTML = "Validée" } else if ((listStudent[i][9][0] >= 10)) { ligneEPS116.children[j].innerHTML = "Validée" } else if (listStudent[i][9][0] < 10) { ligneEPS116.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 7) { ligneEPS116.children[j].innerHTML = mydata[4] } //session
        if (j == 8) {
            if ((listStudent[i][9][0] >= 7 && listStudent[i][3][3] >= 10) || (listStudent[i][9][0] >= 10)) { ligneEPS116.children[j].innerHTML = listStudent[i][9][6] } else { ligneEPS116.children[j].innerHTML = 0 }
        } //nombre_crédits
    }

    //LIGNE EPS117
    var ligneEPS117 = tbody.children[9]
    for (j = 0; j <= ligneEPS117.childElementCount - 1; j++) {
        if (j == 3) { ligneEPS117.children[j].innerHTML = listStudent[i][10][0] } //note info
        if (j == 4) { ligneEPS117.children[j].innerHTML = listStudent[i][10][1] } //coef info
        if (j == 5) {
            val = ligneEPS117.children[2].innerHTML * ligneEPS117.children[3].innerHTML;
            val = val.toFixed(2);
            val = parseFloat(val);
            ligneEPS117.children[j].innerHTML = listStudent[i][10][2]
        } //total note math * coef
        if (j == 6) { ligneEPS117.children[j].innerHTML = listStudent[i][10][3] } //
        if (j == 7) { ligneEPS117.children[j].innerHTML = listStudent[i][10][4] }
        if (j == 8) {
            if (((listStudent[i][10][0] >= 7 && listStudent[i][10][0] < 10) && listStudent[i][10][3] >= 10)) { ligneEPS117.children[j].innerHTML = "Validée" } else if ((listStudent[i][10][0] >= 10)) { ligneEPS117.children[j].innerHTML = "Validée" } else if (listStudent[i][10][0] < 10) { ligneEPS117.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 9) { ligneEPS117.children[j].innerHTML = mydata[4] } // Session
        if (j == 10) {
            if ((listStudent[i][10][0] >= 7 && listStudent[i][10][3] >= 10) || (listStudent[i][10][0] >= 10 || listStudent[i][10][0] >= 10)) { ligneEPS117.children[j].innerHTML = listStudent[i][10][6] } else { ligneEPS117.children[j].innerHTML = 0 }
        } //nombre_crédits
    }

    //LIGNE EPS118
    var ligneEPS118 = tbody.children[10]
    for (j = 0; j <= ligneEPS118.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS118.children[j].innerHTML = listStudent[i][11][0] } //note info
        if (j == 3) { ligneEPS118.children[j].innerHTML = listStudent[i][11][1] } //coef info
        if (j == 4) { /*val=ligneEPS118.children[2].innerHTML*ligneEPS118.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS118.children[j].innerHTML = listStudent[i][11][2] } //total note math * coef
        if (j == 5) { ligneEPS118.children[j].innerHTML = listStudent[i][11][4] } //
        if (j == 6) {
            if (((listStudent[i][11][0] >= 7 && listStudent[i][11][0] < 10) && listStudent[i][10][3] >= 10)) { ligneEPS118.children[j].innerHTML = "Validée" } else if ((listStudent[i][11][0] >= 10)) { ligneEPS118.children[j].innerHTML = "Validée" } else if (listStudent[i][11][0] < 10) { ligneEPS118.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 7) { ligneEPS118.children[j].innerHTML = mydata[4] } //session
        if (j == 8) {
            if ((listStudent[i][11][0] >= 7 && listStudent[i][10][3] >= 10) || (listStudent[i][11][0] >= 10)) { ligneEPS118.children[j].innerHTML = listStudent[i][11][6] } else { ligneEPS118.children[j].innerHTML = 0 }
        } //nombre_crédits
    }

    //LIGNE EPS119
    var ligneEPS119 = tbody.children[11]
    for (j = 0; j <= ligneEPS119.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS119.children[j].innerHTML = listStudent[i][12][0] } //note info
        if (j == 3) { ligneEPS119.children[j].innerHTML = listStudent[i][12][1] } //coef info
        if (j == 4) { ligneEPS119.children[j].innerHTML = listStudent[i][1][2] } //total note math * coef
        if (j == 5) { ligneEPS119.children[j].innerHTML = listStudent[i][11][4] } //
        if (j == 6) {
            //if (listStudent[i][12][5]) { ligneEPS119.children[j].innerHTML = "Validée" } else { ligneEPS119.children[j].innerHTML = "Non validée" } 
            if (((listStudent[i][12][0] >= 7 && listStudent[i][12][0] < 10) && listStudent[i][10][3] >= 10)) { ligneEPS119.children[j].innerHTML = "Validée" } else if ((listStudent[i][12][0] >= 10)) { ligneEPS119.children[j].innerHTML = "Validée" } else if (listStudent[i][12][0] < 10) { ligneEPS119.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 7) { ligneEPS119.children[j].innerHTML = mydata[4] } //session
        if (j == 8) {
            if ((listStudent[i][12][0] >= 7 && listStudent[i][10][3] >= 10) || (listStudent[i][12][0] >= 10)) { ligneEPS119.children[j].innerHTML = listStudent[i][12][6] } else { ligneEPS119.children[j].innerHTML = 0 }
        } //nombre_crédits
    }

    //LINE DEs RESULTATS
    resultat = tbody.children[12]
    for (j = 0; j <= resultat.childElementCount - 1; j++) {
        if (j == 1) {
            resultat.children[1].innerHTML = listStudent[i][13][0];
        }
        if (j == 2) { resultat.children[2].innerHTML = listStudent[i][13][1] }
        if (j == 3) { resultat.children[j].innerHTML = listStudent[i][13][2] }
        if (j == 4) { resultat.children[j].innerHTML = mydata[2].indexOf(listStudent[i][13][2]) + 1 }
        if (j == 6) { resultat.children[6].innerHTML = sommeInt9(ligneEPS111.children[11].innerHTML, ligneEPS112.children[8].innerHTML, ligneEPS113.children[10].innerHTML, ligneEPS114.children[8].innerHTML, ligneEPS115a.children[8].innerHTML, ligneEPS116.children[8].innerHTML, ligneEPS117.children[10].innerHTML, ligneEPS118.children[8].innerHTML, ligneEPS119.children[8].innerHTML) } /**TOtal Crédit */
    }

    //Tbody
    var body3 = clone.children[2].children[2].children[1].children[1]

    //LIGNE 0
    var ligne0 = body3.children[0]
    for (j = 0; j <= ligne0.childElementCount - 1; j++) {
        if (j == 2) { ligne0.children[2].innerHTML = `${ listStudent[i][13][2] } / 20` }
        if (j == 4) { ligne0.children[j].innerHTML = `${mydata[2][0]} / 20` }
    }

    //LIGNE 1
    var ligne1 = body3.children[1]
    for (j = 0; j <= ligne1.childElementCount - 1; j++) {
        if (j == 2) { ligne1.children[j].innerHTML = `${mydata[3]} / 20` }
        if (j == 4) {
            var note_length = mydata[2].length - 1;
            ligne1.children[j].innerHTML = `${mydata[2][note_length]} / 20`
        } //
    }

    //LLIGNE 2
    var ligne2 = body3.children[2]
    for (j = 0; j <= ligne1.childElementCount - 1; j++) {
        if (j == 5) { ligne2.children[j].innerHTML = `${resultat.children[4].innerHTML} sur ${mydata[1].length}` }
        if (j == 4) {}
    }

    /*********************************************************************SEMESTRE 2 STAPS ************************************************************* */
    data2 = mydata[6]
    s2eps = clone.childNodes[2].children[3]
    s2epsbody = s2eps.children[0].children[1]


    //Ligne 1
    ligne11 = s2epsbody.children[0]
    ligne11.children[0].innerHTML = "SEMESTRE 2"
    ligne11.children[2].innerHTML = "EPS121"
    ligne11.children[3].innerHTML = "Activités phyiques adaptées - Sport pour tous"

    for (j = 0; j <= ligne11.childElementCount - 1; j++) {
        if (j == 4) { ligne11.children[j].innerHTML = data2[i][1][0] }
        if (j == 5) { ligne11.children[j].innerHTML = data2[i][1][1] }
        if (j == 6) { ligne11.children[j].innerHTML = data2[i][1][2] }
        if (j == 7) { ligne11.children[j].innerHTML = data2[i][1][3] }
        if (j == 8) { ligne11.children[j].innerHTML = data2[i][1][4] }
        if (j == 9) {
            //if (data2[i][1][5]) { ligne11.children[j].innerHTML = "Validée" } else { ligne11.children[j].innerHTML = "Non validée" }
            if (((data2[i][1][0] >= 7 && data2[i][1][0] < 10) && data2[i][1][3] >= 10)) { ligne11.children[j].innerHTML = "Validée" } else if ((data2[i][1][0] >= 10)) { ligne11.children[j].innerHTML = "Validée" } else if (data2[i][1][0] < 10) { ligne11.children[j].innerHTML = "Non validée" }
        }
        if (j == 10) { if (data2[i][1][8]) { ligne11.children[j].innerHTML = 'Rattrapage' } else { ligne11.children[j].innerHTML = mydata[9] } }
        if (j == 11) {
            if ((data2[i][1][0] >= 7 && data2[i][1][3] >= 10) || (data2[i][1][0] >= 10)) { ligne11.children[j].innerHTML = data2[i][1][6] } else { ligne11.children[j].innerHTML = 0 }
        }
    }

    //Ligne 2
    ligne22 = s2epsbody.children[1]
    ligne22.children[0].innerHTML = "EPS122"
    ligne22.children[1].innerHTML = "Traumatologie - Premiers secours"

    for (j = 0; j <= ligne22.childElementCount - 1; j++) {
        if (j == 2) { ligne22.children[j].innerHTML = data2[i][2][0] }
        if (j == 3) { ligne22.children[j].innerHTML = data2[i][2][1] }
        if (j == 4) { ligne22.children[j].innerHTML = data2[i][2][2] }
        if (j == 5) { ligne22.children[j].innerHTML = data2[i][2][4] }
        if (j == 6) {
            if (((data2[i][2][0] >= 7 && data2[i][2][0] < 10) && data2[i][1][3] >= 10)) { ligne22.children[j].innerHTML = "Validée" } else if ((data2[i][2][0] >= 10)) { ligne22.children[j].innerHTML = "Validée" } else if (data2[i][2][0] < 10) { ligne22.children[j].innerHTML = "Non validée" }
            //if (data2[i][2][5]) { ligne22.children[j].innerHTML = "Validée" } else { ligne22.children[j].innerHTML = "Non validée" } 
        }
        if (j == 7) { if (data2[i][2][8]) { ligne22.children[j].innerHTML = 'Rattrapage' } else { ligne22.children[j].innerHTML = mydata[9] } }
        if (j == 8) {
            if ((data2[i][2][0] >= 7 && data2[i][1][3] >= 10) || (data2[i][2][0] >= 10)) { ligne22.children[j].innerHTML = data2[i][2][6] } else { ligne22.children[j].innerHTML = 0 }
            //ligne22.children[j].innerHTML = data2[i][2][7] 
        }
    }

    //Ligne 3
    ligne33 = s2epsbody.children[2]
        //ligne33.children[0].innerHTML = "SEMESTRE 2"
    ligne33.children[1].innerHTML = "EPS123"
    ligne33.children[2].innerHTML = "Théorie et Méthodologie de l'entrainement"

    for (j = 0; j <= ligne33.childElementCount - 1; j++) {
        if (j == 3) { ligne33.children[j].innerHTML = data2[i][3][0] }
        if (j == 4) { ligne33.children[j].innerHTML = data2[i][3][1] }
        if (j == 5) { ligne33.children[j].innerHTML = data2[i][3][2] }
        if (j == 6) { ligne33.children[j].innerHTML = data2[i][3][3] }
        if (j == 7) { ligne33.children[j].innerHTML = data2[i][3][4] }
        if (j == 8) {
            if (((data2[i][3][0] >= 7 && data2[i][3][0] < 10) && data2[i][3][3] >= 10)) { ligne33.children[j].innerHTML = "Validée" } else if ((data2[i][3][0] >= 10)) { ligne33.children[j].innerHTML = "Validée" } else if (data2[i][2][0] < 10) { ligne33.children[j].innerHTML = "Non validée" }
        }
        if (j == 9) { if (data2[i][3][8]) { ligne33.children[j].innerHTML = 'Rattrapage' } else { ligne33.children[j].innerHTML = mydata[9] } }
        if (j == 10) {
            if ((data2[i][3][0] >= 7 && data2[i][3][3] >= 10) || (data2[i][2][0] >= 10)) { ligne33.children[j].innerHTML = data2[i][3][6] } else { ligne33.children[j].innerHTML = 0 }
            //ligne33.children[j].innerHTML = data2[i][3][7] 
        } //else { ligne11.children[j].innerHTML = 0,  + data2[i][2][0]) >= 20 
    }

    //Ligne 4
    ligne44 = s2epsbody.children[3]
        //ligne44.children[0].innerHTML = "SEMESTRE 2"
    ligne44.children[0].innerHTML = "EPS124"
    ligne44.children[1].innerHTML = "Anatomie II"

    for (j = 0; j <= ligne44.childElementCount - 1; j++) {
        if (j == 2) { ligne44.children[j].innerHTML = data2[i][4][0] }
        if (j == 3) { ligne44.children[j].innerHTML = data2[i][4][1] }
        if (j == 4) { ligne44.children[j].innerHTML = data2[i][4][2] }
        if (j == 5) { ligne44.children[j].innerHTML = data2[i][4][4] }
        if (j == 6) {
            if (((data2[i][4][0] >= 7 && data2[i][4][0] < 10) && data2[i][3][3] >= 10)) { ligne44.children[j].innerHTML = "Validée" } else if ((data2[i][4][0] >= 10)) { ligne44.children[j].innerHTML = "Validée" } else if (data2[i][4][0] < 10) { ligne44.children[j].innerHTML = "Non validée" }
        }
        if (j == 7) { if (data2[i][4][8]) { ligne44.children[j].innerHTML = 'Rattrapage' } else { ligne44.children[j].innerHTML = mydata[9] } }
        if (j == 8) {
            if ((data2[i][4][0] >= 7 && data2[i][3][3] >= 10) || (data2[i][4][0] >= 10)) { ligne44.children[j].innerHTML = data2[i][4][6] } else { ligne44.children[j].innerHTML = 0 }
        }
    }

    //Ligne 5
    ligne55 = s2epsbody.children[4]
        //ligne55.children[0].innerHTML = "SEMESTRE 2"
    ligne55.children[0].innerHTML = "EPS125"
    ligne55.children[1].innerHTML = "Didactique de APS: Athlétisme II"

    for (j = 0; j <= ligne55.childElementCount - 1; j++) {
        if (j == 2) { ligne55.children[j].innerHTML = data2[i][5][0] }
        if (j == 3) { ligne55.children[j].innerHTML = data2[i][5][1] }
        if (j == 4) { ligne55.children[j].innerHTML = data2[i][5][2] }
        if (j == 5) { ligne55.children[j].innerHTML = data2[i][4][4] }
        if (j == 6) {
            if (((data2[i][5][0] >= 7 && data2[i][5][0] < 10) && data2[i][3][3] >= 10)) { ligne55.children[j].innerHTML = "Validée" } else if ((data2[i][5][0] >= 10)) { ligne55.children[j].innerHTML = "Validée" } else if (data2[i][5][0] < 10) { ligne55.children[j].innerHTML = "Non validée" }
        }
        if (j == 7) { if (data2[i][5][8]) { ligne55.children[j].innerHTML = 'Rattrapage' } else { ligne55.children[j].innerHTML = mydata[9] } }
        if (j == 8) {
            if ((data2[i][5][0] >= 7 && data2[i][3][3] >= 10) || (data2[i][5][0] >= 10)) { ligne55.children[j].innerHTML = data2[i][5][6] } else { ligne55.children[j].innerHTML = 0 }
            //ligne55.children[j].innerHTML = data2[i][5][7] 
        }
    }

    //Ligne 6
    ligne66 = s2epsbody.children[5]
        //ligne66.children[0].innerHTML = "SEMESTRE 2"
    ligne66.children[0].innerHTML = "EPS125"
    ligne66.children[1].innerHTML = "Didactique de APS: Gymnastique"

    for (j = 0; j <= ligne66.childElementCount - 1; j++) {
        if (j == 2) { ligne66.children[j].innerHTML = data2[i][6][0] }
        if (j == 3) { ligne66.children[j].innerHTML = data2[i][6][1] }
        if (j == 4) { ligne66.children[j].innerHTML = data2[i][6][2] }
        //if (j == 5) { ligne66.children[j].innerHTML = data2[i][4][3] }
        if (j == 5) { ligne66.children[j].innerHTML = data2[i][6][4] }
        if (j == 6) {
            if (((data2[i][6][0] >= 7 && data2[i][6][0] < 10) && data2[i][3][3] >= 10)) { ligne66.children[j].innerHTML = "Validée" } else if ((data2[i][6][0] >= 10)) { ligne66.children[j].innerHTML = "Validée" } else if (data2[i][6][0] < 10) { ligne66.children[j].innerHTML = "Non validée" }
        }
        if (j == 7) { if (data2[i][6][8]) { ligne66.children[j].innerHTML = 'Rattrapage' } else { ligne66.children[j].innerHTML = mydata[9] } }
        if (j == 8) {
            if ((data2[i][6][0] >= 7 && data2[i][3][3] >= 10) || (data2[i][6][0] >= 10)) { ligne66.children[j].innerHTML = data2[i][6][6] } else { ligne66.children[j].innerHTML = 0 }
        }
    }

    //Ligne 7
    ligne77 = s2epsbody.children[6]
        //ligne77.children[0].innerHTML = "SEMESTRE 2"
    ligne77.children[0].innerHTML = "EPS125"
    ligne77.children[1].innerHTML = "Didactique de APS: Judo"

    for (j = 0; j <= ligne77.childElementCount - 1; j++) {
        if (j == 2) { ligne77.children[j].innerHTML = data2[i][7][0] }
        if (j == 3) { ligne77.children[j].innerHTML = data2[i][7][1] }
        if (j == 4) { ligne77.children[j].innerHTML = data2[i][7][2] }
        //if (j == 5) { ligne77.children[j].innerHTML = data2[i][4][3] }
        if (j == 5) { ligne77.children[j].innerHTML = data2[i][7][4] }
        if (j == 6) {
            if (((data2[i][7][0] >= 7 && data2[i][7][0] < 10) && data2[i][3][3] >= 10)) { ligne77.children[j].innerHTML = "Validée" } else if ((data2[i][7][0] >= 10)) { ligne77.children[j].innerHTML = "Validée" } else if (data2[i][7][0] < 10) { ligne77.children[j].innerHTML = "Non validée" }
        }
        if (j == 7) { if (data2[i][7][8]) { ligne77.children[j].innerHTML = 'Rattrapage' } else { ligne77.children[j].innerHTML = mydata[9] } }
        if (j == 8) {
            if ((data2[i][7][0] >= 7 && data2[i][3][3] >= 10) || (data2[i][7][0] >= 10)) { ligne77.children[j].innerHTML = data2[i][7][6] } else { ligne77.children[j].innerHTML = 0 }
        }
    }

    //Ligne 8
    ligne88 = s2epsbody.children[7]
        //ligne88.children[0].innerHTML = "SEMESTRE 2"
    ligne88.children[0].innerHTML = "EPS125"
    ligne88.children[1].innerHTML = "Didactique de APS: Football"

    for (j = 0; j <= ligne88.childElementCount - 1; j++) {
        if (j == 2) { ligne88.children[j].innerHTML = data2[i][8][0] }
        if (j == 3) { ligne88.children[j].innerHTML = data2[i][8][1] }
        if (j == 4) { ligne88.children[j].innerHTML = data2[i][8][2] }
        //if (j == 5) { ligne88.children[j].innerHTML = data2[i][4][3] }
        if (j == 5) { ligne88.children[j].innerHTML = data2[i][8][4] }
        if (j == 6) {
            if (((data2[i][8][0] >= 7 && data2[i][8][0] < 10) && data2[i][3][3] >= 10)) { ligne88.children[j].innerHTML = "Validée" } else if ((data2[i][8][0] >= 10)) { ligne88.children[j].innerHTML = "Validée" } else if (data2[i][8][0] < 10) { ligne88.children[j].innerHTML = "Non validée" }
        }
        if (j == 7) { if (data2[i][8][8]) { ligne88.children[j].innerHTML = 'Rattrapage' } else { ligne88.children[j].innerHTML = mydata[9] } }
        if (j == 8) {
            if ((data2[i][8][0] >= 7 && data2[i][3][3] >= 10) || (data2[i][8][0] >= 10)) { ligne88.children[j].innerHTML = data2[i][8][6] } else { ligne88.children[j].innerHTML = 0 }
        }
    }

    //Ligne 9
    ligne99 = s2epsbody.children[8]
        //ligne99.children[0].innerHTML = "SEMESTRE 2"
    ligne99.children[0].innerHTML = "EPS126"
    ligne99.children[1].innerHTML = "Pédagogie pratique"

    for (j = 0; j <= ligne99.childElementCount - 1; j++) {
        if (j == 2) { ligne99.children[j].innerHTML = data2[i][9][0] }
        if (j == 3) { ligne99.children[j].innerHTML = data2[i][9][1] }
        if (j == 4) { ligne99.children[j].innerHTML = data2[i][9][2] }
        //if (j == 5) { ligne99.children[j].innerHTML = data2[i][4][3] }
        if (j == 5) { ligne99.children[j].innerHTML = data2[i][9][4] }
        if (j == 6) {
            if (((data2[i][9][0] >= 7 && data2[i][9][0] < 10) && data2[i][3][3] >= 10)) { ligne99.children[j].innerHTML = "Validée" } else if ((data2[i][9][0] >= 10)) { ligne99.children[j].innerHTML = "Validée" } else if (data2[i][9][0] < 10) { ligne99.children[j].innerHTML = "Non validée" }
        }
        if (j == 7) { if (data2[i][9][8]) { ligne99.children[j].innerHTML = 'Rattrapage' } else { ligne99.children[j].innerHTML = mydata[9] } }
        if (j == 8) {
            if ((data2[i][9][0] >= 7 && data2[i][3][3] >= 10) || (data2[i][9][0] >= 10)) { ligne99.children[j].innerHTML = data2[i][9][6] } else { ligne99.children[j].innerHTML = 0 }
        }
    }

    //Ligne 10
    ligne100 = s2epsbody.children[9]
        //ligne100.children[0].innerHTML = "SEMESTRE 2"
    ligne100.children[1].innerHTML = "EPS127"
    ligne100.children[2].innerHTML = "Technique d'expression française II"

    for (j = 0; j <= ligne100.childElementCount - 1; j++) {
        if (j == 3) { ligne100.children[j].innerHTML = data2[i][10][0] }
        if (j == 4) { ligne100.children[j].innerHTML = data2[i][10][1] }
        if (j == 5) { ligne100.children[j].innerHTML = data2[i][10][2] }
        if (j == 6) { ligne100.children[j].innerHTML = data2[i][10][3] }
        if (j == 7) { ligne100.children[j].innerHTML = data2[i][10][4] }
        if (j == 8) {
            if (((data2[i][10][0] >= 7 && data2[i][10][0] < 10) && data2[i][10][3] >= 10)) { ligne100.children[j].innerHTML = "Validée" } else if ((data2[i][10][0] >= 10)) { ligne100.children[j].innerHTML = "Validée" } else if (data2[i][10][0] < 10) { ligne100.children[j].innerHTML = "Non validée" }
        }
        if (j == 9) { if (data2[i][10][8]) { ligne100.children[j].innerHTML = 'Rattrapage' } else { ligne100.children[j].innerHTML = mydata[9] } }
        if (j == 10) {
            if ((data2[i][10][0] >= 7 && data2[i][10][3] >= 10) || (data2[i][10][0] >= 10)) { ligne100.children[j].innerHTML = data2[i][10][6] } else { ligne100.children[j].innerHTML = 0 }
        } //else { ligne11.children[j].innerHTML = 0,  + data2[i][2][0]) >= 20 
    }

    //Ligne 11
    ligne111 = s2epsbody.children[10]
        //ligne111.children[0].innerHTML = "SEMESTRE 2"
    ligne111.children[0].innerHTML = "EPS128"
    ligne111.children[1].innerHTML = "Droit du sport"

    for (j = 0; j <= ligne111.childElementCount - 1; j++) {
        if (j == 2) { ligne111.children[j].innerHTML = data2[i][11][0] }
        if (j == 3) { ligne111.children[j].innerHTML = data2[i][11][1] }
        if (j == 4) { ligne111.children[j].innerHTML = data2[i][11][2] }
        //if (j == 6) { ligne111.children[j].innerHTML = data2[i][11][3] }
        if (j == 5) { ligne111.children[j].innerHTML = data2[i][11][4] }
        if (j == 6) {
            if (((data2[i][11][0] >= 7 && data2[i][11][0] < 10) && data2[i][10][3] >= 10)) { ligne111.children[j].innerHTML = "Validée" } else if ((data2[i][11][0] >= 10)) { ligne111.children[j].innerHTML = "Validée" } else if (data2[i][11][0] < 10) { ligne111.children[j].innerHTML = "Non validée" }
        }
        if (j == 7) { if (data2[i][11][8]) { ligne111.children[j].innerHTML = 'Rattrapage' } else { ligne111.children[j].innerHTML = mydata[9] } }
        if (j == 8) {
            if ((data2[i][11][0] >= 7 && data2[i][10][3] >= 10) || (data2[i][11][0] >= 10)) { ligne111.children[j].innerHTML = data2[i][11][6] } else { ligne111.children[j].innerHTML = 0 }
        } //else { ligne11.children[j].innerHTML = 0,  + data2[i][2][0]) >= 20 
    }

    //Ligne 12
    ligne112 = s2epsbody.children[11]
        //ligne111.children[0].innerHTML = "SEMESTRE 2"
    ligne112.children[0].innerHTML = "EPS129"
    ligne112.children[1].innerHTML = "Stage-Pratique"

    for (j = 0; j <= ligne112.childElementCount - 1; j++) {
        if (j == 2) { ligne112.children[j].innerHTML = data2[i][12][0] }
        if (j == 3) { ligne112.children[j].innerHTML = data2[i][12][1] }
        if (j == 4) { ligne112.children[j].innerHTML = data2[i][12][2] }
        //if (j == 6) { ligne112.children[j].innerHTML = data2[i][11][3] }
        if (j == 5) { ligne112.children[j].innerHTML = data2[i][12][4] }
        if (j == 6) {
            if (((data2[i][2][0] >= 7 && data2[i][12][0] < 10) && data2[i][10][3] >= 10)) { ligne112.children[j].innerHTML = "Validée" } else if ((data2[i][12][0] >= 10)) { ligne112.children[j].innerHTML = "Validée" } else if (data2[i][12][0] < 10) { ligne112.children[j].innerHTML = "Non validée" }
        }
        if (j == 7) { if (data2[i][12][8]) { ligne112.children[j].innerHTML = 'Rattrapage' } else { ligne112.children[j].innerHTML = mydata[9] } }
        if (j == 8) {
            if ((data2[i][12][0] >= 7 && data2[i][10][3] >= 10) || (data2[i][12][0] >= 10)) { ligne112.children[j].innerHTML = data2[i][11][6] } else { ligne112.children[j].innerHTML = 0 }
        } //else { ligne11.children[j].innerHTML = 0,  + data2[i][2][0]) >= 20 
    }

    //Ligne 13
    /*var ligne13 = document.getElementById('ligne-13')
    ligne13.style.backgroundColor = "#C7B54D"*/
    //LIGNE 11
    s2epsResult = s2epsbody.children[12]
    s2epsResult.style.backgroundColor = "#C7B54D"
    s2epsResult.children[0].innerHTML = "RESULTATS SEMESTRE 2"
    s2epsResult.children[5].innerHTML = "Total Crédits Semestre 2"

    for (j = 0; j <= s2epsResult.childElementCount - 1; j++) {
        if (j == 1) { s2epsResult.children[j].innerHTML = data2[i][13][0] }
        if (j == 2) { s2epsResult.children[j].innerHTML = data2[i][13][1] }
        if (j == 3) { s2epsResult.children[j].innerHTML = data2[i][13][2] }
        if (j == 4) { s2epsResult.children[j].innerHTML = mydata[7].indexOf(data2[i][13][2]) + 1 }
        if (j == 6) { s2epsResult.children[j].innerHTML = sommeInt9(ligne11.children[11].innerHTML, ligne22.children[8].innerHTML, ligne33.children[10].innerHTML, ligne44.children[8].innerHTML, ligne55.children[8].innerHTML, ligne99.children[8].innerHTML, ligne100.children[10].innerHTML, ligne111.children[8].innerHTML, ligne112.children[8].innerHTML) }
        //(data2[i][1][7] + data2[i][2][7] + data2[i][3][7] + data2[i][4][7] + data2[i][5][7] + data2[i][9][7] + data2[i][10][7] + data2[i][11][7] + data2[i][12][7]) }
    }

    /**RESULTATS S1 & S2 MDS */

    s1s2epsrecap = clone.children[2].children[4].children[1].children[1]

    for (j = 0; j <= s1s2epsrecap.childElementCount - 1; j++) {
        if (j == 0) { s1s2epsrecap.children[j].innerHTML = sommeInt2(resultat.children[1].innerHTML, s2epsResult.children[1].innerHTML) }
        if (j == 1) { s1s2epsrecap.children[j].innerHTML = sommeFloat2(resultat.children[2].innerHTML, s2epsResult.children[2].innerHTML) }
        if (j == 2) { s1s2epsrecap.children[j].innerHTML = `${(parseFloat(s1s2epsrecap.children[1].innerHTML) / s1s2epsrecap.children[0].innerHTML).toFixed(2)} / 20` }
        if (j == 3) {
            var total = parseFloat(s1s2epsrecap.children[1].innerHTML)
            s1s2epsrecap.children[j].innerHTML = `${mydata[7].indexOf(data2[i][13][2]) + 1}  /  ${data2.length}`
        }
        if (j == 4) { s1s2epsrecap.children[j].innerHTML = `${ sommeInt2(resultat.lastChild.innerHTML, s2epsResult.lastChild.innerHTML) }  /  60` }
        if (j == 5) {
            var moyenne = parseFloat(s1s2epsrecap.children[2].innerHTML)
            if (moyenne >= 10) { s1s2epsrecap.children[j].innerHTML = "ADMIS(E)" } else { s1s2epsrecap.children[j].innerHTML = "REFUSE(E)" }
        }
    }




    return (clone)
}

/**FONCTION BULLETIN STAPS2 */
function BullSTAPS2(clone, i, mydata) {

    //DONNEES RECUPEREES DE LA BD
    var listStudent = mydata[1]

    //Info Utilisateur
    var info1 = clone.children[2].children[1].children[0]
    info1.children[2].innerHTML = info1.children[2].innerHTML + ` ${listStudent[i][0]['nom']}`
    info1.children[3].innerHTML = info1.children[3].innerHTML + ` ${listStudent[i][0]['prenom']}`

    var info2 = clone.children[2].children[1].children[1]
    info2.children[1].innerHTML = info2.children[1].innerHTML + ` ${listStudent[i][0]['matricule']}`
    info2.children[2].innerHTML = info2.children[2].innerHTML + ` ${listStudent[i][0]['date_naissance']}`
    info2.children[3].innerHTML = info2.children[3].innerHTML + ` ${listStudent[i][0]['lieu_naissance']}`
    info2.children[4].innerHTML = info2.children[4].innerHTML + ` 2022-2023`   //Ajout de la variable  de la date

    //RESULTATS
    var tbody = clone.children[2].children[2].children[0].children[1]

    //LIGNE EPS111
    var ligneEPS111 = tbody.children[0]
    for (var j = 0; j <= ligneEPS111.childElementCount - 1; j++) {
        if (j == 4) { ligneEPS111.children[j].innerHTML = listStudent[i][1][0] } //note 
        if (j == 5) { ligneEPS111.children[j].innerHTML = listStudent[i][1][1] } //coef
        if (j == 6) {
            var val = ligneEPS111.children[4].innerHTML * ligneEPS111.children[5].innerHTML;
            val = val.toFixed(2);
            val = parseFloat(val);
            ligneEPS111.children[j].innerHTML = val
        } //total note  * coef
        if (j == 7) { ligneEPS111.children[j].innerHTML = listStudent[i][1][3] } //moyenne donc (totalmath + totalinfo)/2
        if (j == 8) { ligneEPS111.children[j].innerHTML = listStudent[i][1][4] } //Rang
        if (j == 9) {
            if (((listStudent[i][1][0] >= 7 && listStudent[i][1][0] < 10) && listStudent[i][1][3] >= 10)) { ligneEPS111.children[j].innerHTML = "Validée" } else if ((listStudent[i][1][0] >= 10)) { ligneEPS111.children[j].innerHTML = "Validée" } else if (listStudent[i][1][0] < 10) { ligneEPS111.children[j].innerHTML = "Non validée" }
            /*if (listStudent[i][1][5]) {
                ligneEPS111.children[j].innerHTML = "Validée"
                ligneEPS111.children[9].innerHTML = "Validée"
            } else { ligneEPS111.children[9].innerHTML = "Non validée" }*/
        } //Mention
        if (j == 10) { ligneEPS111.children[j].innerHTML = mydata[4] } //Session
        if (j == 11) { 
            //if (listStudent[i][1][0] >= 10) { ligneEPS111.children[j].innerHTML = listStudent[i][1][6] } else { ligneEPS111.children[j].innerHTML = 0 } 
            if ((listStudent[i][1][0] >= 7 && listStudent[i][1][2] >= 10) || (listStudent[i][1][0] >= 10)) { ligneEPS111.children[j].innerHTML = listStudent[i][1][6] } else { ligneEPS111.children[j].innerHTML = 0 }
        } //Crédits
        
    }

    //LIGNE EPS112
    var ligneEPS112 = tbody.children[1]
    for (j = 0; j <= ligneEPS112.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS112.children[j].innerHTML = listStudent[i][2][0] } //note info
        if (j == 3) { ligneEPS112.children[j].innerHTML = listStudent[i][2][1] } //coef info
        if (j == 4) { ligneEPS112.children[j].innerHTML = listStudent[i][2][2] } //val=ligneEPS112.children[2].innerHTML*ligneEPS112.children[3].innerHTML; val= val.toFixed(2); val = parseFloat(val); ligneEPS112.children[j].innerHTML = val}//total note math * coef
        if (j == 5) { ligneEPS112.children[j].innerHTML = listStudent[i][2][4] } //Rang
        if (j == 6) {
            if (listStudent[i][2][5]) { ligneEPS112.children[6].innerHTML = "Validée" } else { ligneEPS112.children[6].innerHTML = "Non validée" }
        }
        if (j == 7) { ligneEPS112.children[j].innerHTML = mydata[4] } //Session
        if (j == 8) { if (listStudent[i][2][5]) { ligneEPS112.children[j].innerHTML = listStudent[i][2][6] } else { ligneEPS112.children[j].innerHTML = 0 } } //Crédits
    }

    //LIGNE EPS113
    var ligneEPS113 = tbody.children[2]
    for (j = 0; j <= ligneEPS113.childElementCount - 1; j++) {
        if (j == 3) { ligneEPS113.children[j].innerHTML = listStudent[i][3][0] } //note info
        if (j == 4) { ligneEPS113.children[j].innerHTML = listStudent[i][3][1] } //coef info
        if (j == 5) {
            val = ligneEPS113.children[2].innerHTML * ligneEPS113.children[3].innerHTML;
            val = val.toFixed(2);
            val = parseFloat(val);
            ligneEPS113.children[j].innerHTML = listStudent[i][3][2]
        } //total note math * coef
        if (j == 6) { ligneEPS113.children[j].innerHTML = listStudent[i][3][3] } //
        if (j == 7) { ligneEPS113.children[j].innerHTML = listStudent[i][3][4] }
        if (j == 8) { if (listStudent[i][3][5]) { ligneEPS113.children[j].innerHTML = "Validée" } else { ligneEPS113.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 9) { ligneEPS113.children[j].innerHTML = mydata[4] } // Session
        if (j == 10) { if (listStudent[i][3][5]) { ligneEPS113.children[j].innerHTML = listStudent[i][3][6] } else { ligneEPS113.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS114
    var ligneEPS114 = tbody.children[3]
    for (j = 0; j <= ligneEPS114.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS114.children[j].innerHTML = listStudent[i][4][0] } //note info
        if (j == 3) { ligneEPS114.children[j].innerHTML = listStudent[i][4][1] } //coef info
        if (j == 4) { /*val=ligneEPS114.children[2].innerHTML*ligneEPS114.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS114.children[j].innerHTML = listStudent[i][4][2] } //total note math * coef
        if (j == 5) { ligneEPS114.children[j].innerHTML = listStudent[i][4][4] } //
        if (j == 6) { if (listStudent[i][4][5]) { ligneEPS114.children[j].innerHTML = "Validée" } else { ligneEPS114.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS114.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][4][5]) { ligneEPS114.children[j].innerHTML = listStudent[i][4][6] } else { ligneEPS114.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS115a
    var ligneEPS115a = tbody.children[4]
    for (j = 0; j <= ligneEPS115a.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS115a.children[j].innerHTML = listStudent[i][5][0] } //note info
        if (j == 3) { ligneEPS115a.children[j].innerHTML = listStudent[i][5][1] } //coef info
        if (j == 4) { /*val=ligneEPS115a.children[2].innerHTML*ligneEPS115a.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS115a.children[j].innerHTML = listStudent[i][5][2] } //total note math * coef
        if (j == 5) { ligneEPS115a.children[j].innerHTML = listStudent[i][5][4] } //
        if (j == 6) { 
            if (((listStudent[i][5][5] >= 7 && listStudent[i][5][0] < 10) && listStudent[i][3][3] >= 10)) { ligneEPS115a.children[j].innerHTML = "Validée" } else if ((listStudent[i][5][0] >= 10)) { ligneEPS115a.children[j].innerHTML = "Validée" } else if (listStudent[i][5][0] < 10) { ligneEPS115a.children[j].innerHTML = "Non validée" }
            //if (listStudent[i][5][5]) { ligneEPS115a.children[j].innerHTML = "Validée" } else { ligneEPS115a.children[j].innerHTML = "Non validée" } 
        } //Mention
        if (j == 7) { ligneEPS115a.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { 
            //if ((listStudent[i][5][0] + listStudent[i][6][0] + listStudent[i][7][0] + listStudent[i][8][0] + listStudent[i][9][0] + listStudent[i][10][0]) >= 48) { ligneEPS115a.children[j].innerHTML = listStudent[i][5][6] } else { ligneEPS115a.children[j].innerHTML = 0 } 
            if ((listStudent[i][5][0] >= 7 && listStudent[i][3][3] >= 10) || (listStudent[i][5][0] >= 10)) { ligneEPS115a.children[j].innerHTML = listStudent[i][5][6] } else { ligneEPS115a.children[j].innerHTML = 0 }
        } //nombre_crédits
    }

    //LIGNE EPS115b
    var ligneEPS115b = tbody.children[5]
    for (j = 0; j <= ligneEPS115b.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS115b.children[j].innerHTML = listStudent[i][6][0] } //note info
        if (j == 3) { ligneEPS115b.children[j].innerHTML = listStudent[i][6][1] } //coef info
        if (j == 4) { /*val=ligneEPS115b.children[2].innerHTML*ligneEPS115b.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS115b.children[j].innerHTML = listStudent[i][6][2] } //total note math * coef
        if (j == 5) { ligneEPS115b.children[j].innerHTML = listStudent[i][5][4] } //
        if (j == 6) { if (listStudent[i][6][5]) { ligneEPS115b.children[j].innerHTML = "Validée" } else { ligneEPS115b.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS115b.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][6][5]) { ligneEPS115b.children[j].innerHTML = listStudent[i][6][6] } else { ligneEPS115b.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //Ligne EPS115f
    var ligneEPS115f = tbody.children[6]
    for (j = 0; j <= ligneEPS115f.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS115f.children[j].innerHTML = listStudent[i][7][0] } //note info
        if (j == 3) { ligneEPS115f.children[j].innerHTML = listStudent[i][7][1] } //coef info
        if (j == 4) { /*val=ligneEPS115f.children[2].innerHTML*ligneEPS115f.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS115f.children[j].innerHTML = listStudent[i][7][2] } //total note math * coef
        if (j == 5) { ligneEPS115f.children[j].innerHTML = listStudent[i][7][4] } //
        if (j == 6) { if (listStudent[i][7][5]) { ligneEPS115f.children[j].innerHTML = "Validée" } else { ligneEPS115f.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS115f.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][7][5]) { ligneEPS115f.children[j].innerHTML = listStudent[i][7][6] } else { ligneEPS115f.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //Ligne EPS115g
    var ligneEPS115g = tbody.children[7]
    for (j = 0; j <= ligneEPS115g.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS115g.children[j].innerHTML = listStudent[i][8][0] } //note info
        if (j == 3) { ligneEPS115g.children[j].innerHTML = listStudent[i][8][1] } //coef info
        if (j == 4) { /*val=ligneEPS115g.children[2].innerHTML*ligneEPS115g.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS115g.children[j].innerHTML = listStudent[i][8][2] } //total note math * coef
        if (j == 5) { ligneEPS115g.children[j].innerHTML = listStudent[i][8][4] } //
        if (j == 6) { if (listStudent[i][8][5]) { ligneEPS115g.children[j].innerHTML = "Validée" } else { ligneEPS115g.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS115g.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][8][5]) { ligneEPS115g.children[j].innerHTML = listStudent[i][8][6] } else { ligneEPS115g.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS115j
    var ligneEPS115j = tbody.children[8]
    for (j = 0; j <= ligneEPS115j.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS115j.children[j].innerHTML = listStudent[i][9][0] } //note info
        if (j == 3) { ligneEPS115j.children[j].innerHTML = listStudent[i][9][1] } //coef info
        if (j == 4) { /*val=ligneEPS115j.children[2].innerHTML*ligneEPS115j.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS115j.children[j].innerHTML = listStudent[i][9][2] } //total note math * coef
        if (j == 5) { ligneEPS115j.children[j].innerHTML = listStudent[i][9][4] } //
        if (j == 6) { if (listStudent[i][9][5]) { ligneEPS115j.children[j].innerHTML = "Validée" } else { ligneEPS115j.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS115j.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][9][5]) { ligneEPS115j.children[j].innerHTML = listStudent[i][9][6] } else { ligneEPS115j.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS115l
    var ligneEPS115l = tbody.children[9]
    for (j = 0; j <= ligneEPS115l.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS115l.children[j].innerHTML = listStudent[i][10][0] } //note info
        if (j == 3) { ligneEPS115l.children[j].innerHTML = listStudent[i][10][1] } //coef info
        if (j == 4) { /*val=ligneEPS115l.children[2].innerHTML*ligneEPS115l.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS115l.children[j].innerHTML = listStudent[i][10][2] } //total note math * coef
        if (j == 5) { ligneEPS115l.children[j].innerHTML = listStudent[i][10][4] } //
        if (j == 6) { if (listStudent[i][10][5]) { ligneEPS115l.children[j].innerHTML = "Validée" } else { ligneEPS115l.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS115l.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][10][5]) { ligneEPS115l.children[j].innerHTML = listStudent[i][10][6] } else { ligneEPS115l.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS116
    var ligneEPS116 = tbody.children[10]
    for (j = 0; j <= ligneEPS116.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS116.children[j].innerHTML = listStudent[i][11][0] } //note info
        if (j == 3) { ligneEPS116.children[j].innerHTML = listStudent[i][11][1] } //coef info
        if (j == 4) { /*val=ligneEPS116.children[2].innerHTML*ligneEPS116.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS116.children[j].innerHTML = listStudent[i][11][2] } //total note math * coef
        if (j == 5) { ligneEPS116.children[j].innerHTML = listStudent[i][9][4] } //
        if (j == 6) { if (listStudent[i][11][5]) { ligneEPS116.children[j].innerHTML = "Validée" } else { ligneEPS116.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS116.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][11][5]) { ligneEPS116.children[j].innerHTML = listStudent[i][11][6] } else { ligneEPS116.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS117
    var ligneEPS117 = tbody.children[11]
    for (j = 0; j <= ligneEPS117.childElementCount - 1; j++) {
        if (j == 3) { ligneEPS117.children[j].innerHTML = listStudent[i][12][0] } //note info
        if (j == 4) { ligneEPS117.children[j].innerHTML = listStudent[i][12][1] } //coef info
        if (j == 5) {
            val = ligneEPS117.children[2].innerHTML * ligneEPS117.children[3].innerHTML;
            val = val.toFixed(2);
            val = parseFloat(val);
            ligneEPS117.children[j].innerHTML = listStudent[i][12][2]
        } //total note math * coef
        if (j == 6) { ligneEPS117.children[j].innerHTML = listStudent[i][12][3] } //
        if (j == 7) { ligneEPS117.children[j].innerHTML = listStudent[i][12][4] }
        if (j == 8) { if (listStudent[i][12][5]) { ligneEPS117.children[j].innerHTML = "Validée" } else { ligneEPS117.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 9) { ligneEPS117.children[j].innerHTML = mydata[4] } // Session
        if (j == 10) { if (listStudent[i][12][5]) { ligneEPS117.children[j].innerHTML = listStudent[i][12][6] } else { ligneEPS117.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS118
    var ligneEPS118 = tbody.children[12]
    for (j = 0; j <= ligneEPS118.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS118.children[j].innerHTML = listStudent[i][13][0] } //note info
        if (j == 3) { ligneEPS118.children[j].innerHTML = listStudent[i][13][1] } //coef info
        if (j == 4) { /*val=ligneEPS118.children[2].innerHTML*ligneEPS118.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS118.children[j].innerHTML = listStudent[i][13][2] } //total note math * coef
        if (j == 5) { ligneEPS118.children[j].innerHTML = listStudent[i][13][4] } //
        if (j == 6) { if (listStudent[i][13][5]) { ligneEPS118.children[j].innerHTML = "Validée" } else { ligneEPS118.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS118.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][13][5]) { ligneEPS118.children[j].innerHTML = listStudent[i][13][6] } else { ligneEPS118.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS119
    var ligneEPS119 = tbody.children[13]
    for (j = 0; j <= ligneEPS119.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS119.children[j].innerHTML = listStudent[i][14][0] } //note info
        if (j == 3) { ligneEPS119.children[j].innerHTML = listStudent[i][14][1] } //coef info
        if (j == 4) { ligneEPS119.children[j].innerHTML = listStudent[i][14][2] } //total note math * coef
        if (j == 5) { ligneEPS119.children[j].innerHTML = listStudent[i][14][4] } //
        if (j == 6) { if (listStudent[i][14][5]) { ligneEPS119.children[j].innerHTML = "Validée" } else { ligneEPS119.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS119.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][14][5]) { ligneEPS119.children[j].innerHTML = listStudent[i][14][6] } else { ligneEPS119.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LINE DEs RESULTATS
    var resultat = tbody.children[14]
    for (j = 0; j <= resultat.childElementCount - 1; j++) {
        if (j == 1) {
            resultat.children[1].innerHTML = listStudent[i][15][0];
        }
        if (j == 2) { resultat.children[2].innerHTML = listStudent[i][15][1] }
        if (j == 3) { resultat.children[j].innerHTML = listStudent[i][15][2] }
        if (j == 4) { resultat.children[j].innerHTML = mydata[2].indexOf(listStudent[i][15][2]) + 1 }
        if (j == 6) { resultat.children[6].innerHTML = sommeInt9(ligneEPS111.children[11].innerHTML, ligneEPS112.children[8].innerHTML, ligneEPS113.children[10].innerHTML, ligneEPS114.children[8].innerHTML, ligneEPS115a.children[8].innerHTML, ligneEPS116.children[8].innerHTML, ligneEPS117.children[10].innerHTML, ligneEPS118.children[8].innerHTML, ligneEPS119.children[8].innerHTML) }
    }

    //Tbody
    var body3 = clone.children[2].children[2].children[1].children[1]

    //LIGNE 0
    var ligne0 = body3.children[0]
    for (j = 0; j <= ligne0.childElementCount - 1; j++) {
        if (j == 2) { ligne0.children[2].innerHTML = `${ listStudent[i][15][2] } / 20` }
        if (j == 4) { ligne0.children[j].innerHTML = `${mydata[2][0]} / 20` }
    }

    //LIGNE 1
    var ligne1 = body3.children[1]
    for (j = 0; j <= ligne1.childElementCount - 1; j++) {
        if (j == 2) { ligne1.children[j].innerHTML = `${mydata[3]} / 20` }
        if (j == 4) {
            var note_length = mydata[2].length - 1;
            ligne1.children[j].innerHTML = `${mydata[2][note_length]} / 20`
        } //
    }

    //LLIGNE 2
    var ligne2 = body3.children[2]
    for (j = 0; j <= ligne1.childElementCount - 1; j++) {
        if (j == 5) { ligne2.children[j].innerHTML = `${resultat.children[4].innerHTML} sur ${mydata[1].length}` }
        if (j == 4) {}
    }
    resultat.style.backgroundColor = "#C7B54D"

    // ##################### SEMESTRE 4 ###################################################################################
    var listStudent2 = mydata[10][0]
    var s4body = clone.children[2].children[3].children[0].children[1]

    //Ligne 3
    var ligne33 = s4body.children[2]
    for (var j = 0; j <= ligne33.childElementCount - 1; j++) {
        if (j == 3) { ligne33.children[j].innerHTML = listStudent2[i][1][0] }
        if (j == 4) { ligne33.children[j].innerHTML = listStudent2[i][1][1] }
        if (j == 5) { ligne33.children[j].innerHTML = listStudent2[i][1][2] }
        if (j == 6) { ligne33.children[j].innerHTML = listStudent2[i][10][3] }
        if (j == 7) { ligne33.children[j].innerHTML = listStudent2[i][1][4] }
        if (j == 8) {
            if (listStudent2[i][1][5]) { ligne33.children[j].innerHTML = 'Validée' } else {
                ligne33.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 9) {
            if (listStudent2[i][1][10]) { ligne33.children[j].innerHTML = "Rattrapage" } else { ligne33.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 10) { ligne33.children[j].innerHTML = listStudent2[i][1][7] }
    }
    //Ligne 4
    var ligne44 = s4body.children[3]
    for (j = 0; j <= ligne44.childElementCount - 1; j++) {
        if (j == 2) { ligne44.children[j].innerHTML = listStudent2[i][2][0] }
        if (j == 3) { ligne44.children[j].innerHTML = listStudent2[i][2][1] }
        if (j == 4) { ligne44.children[j].innerHTML = listStudent2[i][2][2] }
        if (j == 5) { ligne44.children[j].innerHTML = listStudent2[i][2][4] }
        if (j == 6) {
            if (listStudent2[i][2][5]) { ligne44.children[j].innerHTML = 'Validée' } else {
                ligne44.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][2][10]) { ligne44.children[j].innerHTML = "Rattrapage" } else { ligne44.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 8) { ligne44.children[j].innerHTML = listStudent2[i][2][7] }
    }

    //Ligne 5
    var ligne55 = s4body.children[4]
    for (j = 0; j <= ligne55.childElementCount - 1; j++) {
        if (j == 2) { ligne55.children[j].innerHTML = listStudent2[i][3][0] }
        if (j == 3) { ligne55.children[j].innerHTML = listStudent2[i][3][1] }
        if (j == 4) { ligne55.children[j].innerHTML = listStudent2[i][3][2] }
        if (j == 5) { ligne55.children[j].innerHTML = listStudent2[i][3][4] }
        if (j == 6) {
            if (listStudent2[i][3][5]) { ligne55.children[j].innerHTML = 'Validée' } else {
                ligne55.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][3][10]) { ligne55.children[j].innerHTML = "Rattrapage" } else { ligne55.children[j].innerHTML = "Mai 2023" }
        }
        //if (j == 8) { ligne55.children[j].innerHTML = listStudent2[i][2][7] }
    }

    //Ligne 6
    var ligne66 = s4body.children[5]
    for (j = 0; j <= ligne66.childElementCount - 1; j++) {
        if (j == 2) { ligne66.children[j].innerHTML = listStudent2[i][4][0] }
        if (j == 3) { ligne66.children[j].innerHTML = listStudent2[i][4][1] }
        if (j == 4) { ligne66.children[j].innerHTML = listStudent2[i][4][2] }
        if (j == 5) { ligne66.children[j].innerHTML = listStudent2[i][4][4] }
        if (j == 6) {
            if (listStudent2[i][4][5]) { ligne66.children[j].innerHTML = 'Validée' } else {
                ligne66.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][4][10]) { ligne66.children[j].innerHTML = "Rattrapage" } else { ligne66.children[j].innerHTML = "Mai 2023" }
        }
        //if (j == 8) { ligne55.children[j].innerHTML = listStudent2[i][2][7] }
    }

    //Ligne 7
    var ligne77 = s4body.children[6]
    for (j = 0; j <= ligne77.childElementCount - 1; j++) {
        if (j == 2) { ligne77.children[j].innerHTML = listStudent2[i][5][0] }
        if (j == 3) { ligne77.children[j].innerHTML = listStudent2[i][5][1] }
        if (j == 4) { ligne77.children[j].innerHTML = listStudent2[i][5][2] }
        if (j == 5) { ligne77.children[j].innerHTML = listStudent2[i][5][4] }
        if (j == 6) {
            if (listStudent2[i][5][5]) { ligne77.children[j].innerHTML = 'Validée' } else {
                ligne77.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][5][10]) { ligne77.children[j].innerHTML = "Rattrapage" } else { ligne77.children[j].innerHTML = "Mai 2023" }
        }
        //if (j == 8) { ligne55.children[j].innerHTML = listStudent2[i][2][7] }
    }

    //Ligne 8
    var ligne88 = s4body.children[7]
    for (j = 0; j <= ligne88.childElementCount - 1; j++) {
        if (j == 2) { ligne88.children[j].innerHTML = listStudent2[i][6][0] }
        if (j == 3) { ligne88.children[j].innerHTML = listStudent2[i][6][1] }
        if (j == 4) { ligne88.children[j].innerHTML = listStudent2[i][6][2] }
        if (j == 5) { ligne88.children[j].innerHTML = listStudent2[i][6][4] }
        if (j == 6) {
            if (listStudent2[i][6][5]) { ligne88.children[j].innerHTML = 'Validée' } else {
                ligne88.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][6][10]) { ligne88.children[j].innerHTML = "Rattrapage" } else { ligne88.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 8) { ligne88.children[j].innerHTML = listStudent2[i][6][7] }
    }
    //Ligne 9
    var lignee99 = s4body.children[8]
    for (j = 0; j <= lignee99.childElementCount - 1; j++) {
        if (j == 2) { lignee99.children[j].innerHTML = listStudent2[i][7][0] }
        if (j == 3) { lignee99.children[j].innerHTML = listStudent2[i][7][1] }
        if (j == 4) { lignee99.children[j].innerHTML = listStudent2[i][7][2] }
        if (j == 5) { lignee99.children[j].innerHTML = listStudent2[i][7][4] }
        if (j == 6) {
            if (listStudent2[i][7][5]) { lignee99.children[j].innerHTML = 'Validée' } else {
                lignee99.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][7][10]) { lignee99.children[j].innerHTML = "Rattrapage" } else { lignee99.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 8) { lignee99.children[j].innerHTML = listStudent2[i][7][7] }
    }
    //Ligne 10
    var ligne10 = s4body.children[9]
    for (j = 0; j <= ligne10.childElementCount - 1; j++) {
        if (j == 2) { ligne10.children[j].innerHTML = listStudent2[i][8][0] }
        if (j == 3) { ligne10.children[j].innerHTML = listStudent2[i][8][1] }
        if (j == 4) { ligne10.children[j].innerHTML = listStudent2[i][8][2] }
        if (j == 5) { ligne10.children[j].innerHTML = listStudent2[i][8][4] }
        if (j == 6) {
            if (listStudent2[i][8][5]) { ligne10.children[j].innerHTML = 'Validée' } else {
                ligne10.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][8][10]) { ligne10.children[j].innerHTML = "Rattrapage" } else { ligne10.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 8) { ligne10.children[j].innerHTML = listStudent2[i][8][7] }
    }

    //Ligne 11
    var ligne11 = s4body.children[10]
    for (j = 0; j <= ligne11.childElementCount - 1; j++) {
        if (j == 2) { ligne11.children[j].innerHTML = listStudent2[i][9][0] }
        if (j == 3) { ligne11.children[j].innerHTML = listStudent2[i][9][1] }
        if (j == 4) { ligne11.children[j].innerHTML = listStudent2[i][9][2] }
        if (j == 5) { ligne11.children[j].innerHTML = listStudent2[i][9][4] }
        if (j == 6) {
            if (listStudent2[i][9][5]) { ligne11.children[j].innerHTML = 'Validée' } else {
                ligne11.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][9][10]) { ligne11.children[j].innerHTML = "Rattrapage" } else { ligne11.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 8) { ligne11.children[j].innerHTML = listStudent2[i][9][7] }
    }

    //Ligne 12
    var ligne12 = s4body.children[11]
    for (j = 0; j <= ligne12.childElementCount - 1; j++) {
        if (j == 2) { ligne12.children[j].innerHTML = listStudent2[i][10][0] }
        if (j == 3) { ligne12.children[j].innerHTML = listStudent2[i][10][1] }
        if (j == 4) { ligne12.children[j].innerHTML = listStudent2[i][10][2] }
        if (j == 5) { ligne12.children[j].innerHTML = listStudent2[i][10][4] }
        if (j == 6) {
            if (listStudent2[i][10][5]) { ligne12.children[j].innerHTML = 'Validée' } else {
                ligne12.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][10][10]) { ligne12.children[j].innerHTML = "Rattrapage" } else { ligne12.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 8) { ligne12.children[j].innerHTML = listStudent2[i][10][7] }
    }

    //Ligne 13
    var ligne13 = s4body.children[12]
    for (j = 0; j <= ligne13.childElementCount - 1; j++) {
        if (j == 3) { ligne13.children[j].innerHTML = listStudent2[i][11][0] }
        if (j == 4) { ligne13.children[j].innerHTML = listStudent2[i][11][1] }
        if (j == 5) { ligne13.children[j].innerHTML = listStudent2[i][11][2] }
        if (j == 6) { ligne13.children[j].innerHTML = listStudent2[i][12][3] }
        if (j == 7) { ligne13.children[j].innerHTML = listStudent2[i][11][4] }
        if (j == 8) {
            if (listStudent2[i][11][5]) { ligne13.children[j].innerHTML = 'Validée' } else {
                ligne13.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 9) {
            if (listStudent2[i][11][10]) { ligne13.children[j].innerHTML = "Rattrapage" } else { ligne13.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 10) { ligne13.children[j].innerHTML = listStudent2[i][11][7] }

    }

    //Ligne 14
    var ligne14 = s4body.children[13]
    for (j = 0; j <= ligne14.childElementCount - 1; j++) {
        if (j == 2) { ligne14.children[j].innerHTML = listStudent2[i][12][0] }
        if (j == 3) { ligne14.children[j].innerHTML = listStudent2[i][12][1] }
        if (j == 4) { ligne14.children[j].innerHTML = listStudent2[i][12][2] }
        if (j == 5) { ligne14.children[j].innerHTML = listStudent2[i][12][4] }
        if (j == 6) {
            if (listStudent2[i][12][5]) { ligne14.children[j].innerHTML = 'Validée' } else {
                ligne14.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][12][10]) { ligne14.children[j].innerHTML = "Rattrapage" } else { ligne14.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 8) { ligne14.children[j].innerHTML = listStudent2[i][12][7] }

    }

    //Ligne 16 
    /*var*/
    var ligne16 = s4body.children[15]
    ligne16.style.backgroundColor = 'rgb(199, 181, 77)'
    for (j = 0; j <= 6; j++) {
        //if (j == 0) { ligne16.children[j].innerHTML = "" }
        if (j == 1) { ligne16.children[j].innerHTML = listStudent2[i][13][0] }
        if (j == 2) { ligne16.children[j].innerHTML = listStudent2[i][13][1] }
        if (j == 3) { ligne16.children[j].innerHTML = listStudent2[i][13][2] }
        if (j == 4) { ligne16.children[j].innerHTML = mydata[10][1].indexOf(listStudent2[i][13][2]) + 1 }
        //if (j == 5) { ligne16.children[j].innerHTML = "OBOSSO" }
        if (j == 6) {
            ligne16.children[j].innerHTML = sommeInt9(ligne33.lastChild.innerHTML, ligne44.lastChild.innerHTML, ligne88.lastChild.innerHTML, lignee99.lastChild.innerHTML, ligne10.lastChild.innerHTML, ligne11.lastChild.innerHTML, ligne12.lastChild.innerHTML, ligne13.lastChild.innerHTML, ligne14.lastChild.innerHTML)
        }
    }

    // SEMESTRE 4 & 3 RESULT
    var resultats4s3 = clone.children[2].children[4]

    var ligneresultat = resultats4s3.children[1].children[1]

    for (j = 0; j <= ligneresultat.childElementCount - 1; j++) {
        if (j == 0) { ligneresultat.children[j].innerHTML = sommeInt2(resultat.children[1].innerHTML, ligne16.children[1].innerHTML) }
        if (j == 1) { ligneresultat.children[j].innerHTML = sommeFloat2(resultat.children[2].innerHTML, ligne16.children[2].innerHTML) }
        if (j == 2) { ligneresultat.children[j].innerHTML = `${(parseFloat(ligneresultat.children[1].innerHTML) / ligneresultat.children[0].innerHTML).toFixed(2)} / 20` }
        if (j == 3) {
            var total = parseFloat(ligneresultat.children[1].innerHTML)
            ligneresultat.children[j].innerHTML = `${mydata[10][2].indexOf(total) + 1}  /  ${listStudent2.length}`
        }
        if (j == 4) { ligneresultat.children[j].innerHTML = `${ sommeInt2(resultat.lastChild.innerHTML, ligne16.lastChild.innerHTML) }  /  60` }
        if (j == 5) {
            var moyenne = parseFloat(ligneresultat.children[2].innerHTML)
            if (moyenne >= 10) { ligneresultat.children[j].innerHTML = "ADMIS(E)" } else { ligneresultat.children[j].innerHTML = "ECHEC" }
        }
    }







    return clone
}

/**FONCTION BULLETIN EVE */
function BullEVE(clone, i) {
    //DONNEES RECUPEREES DE LA BD
    listStudent = mydata[1]

    //Info Utilisateur
    info1 = clone.children[2].children[1].children[0]
    info1.children[2].innerHTML = info1.children[2].innerHTML + ` ${listStudent[i][0]['nom']}`
    info1.children[3].innerHTML = info1.children[3].innerHTML + ` ${listStudent[i][0]['prenom']}`

    info2 = clone.children[2].children[1].children[1]
    info2.children[1].innerHTML = info2.children[1].innerHTML + ` ${listStudent[i][0]['matricule']}`
    info2.children[2].innerHTML = info2.children[2].innerHTML + ` ${listStudent[i][0]['date_naissance']}`
    info2.children[3].innerHTML = info2.children[3].innerHTML + ` ${listStudent[i][0]['lieu_naissance']}`
    info2.children[4].innerHTML = info2.children[4].innerHTML + ` 2022-2023`

    //Tableau de notes
    var tbody = clone.children[2].children[2].children[0].children[1]

    //LIGNE MAS 315
    var ligneMAS315 = tbody.children[0]
    for (j = 0; j <= ligneMAS315.childElementCount - 1; j++) {
        if (j == 4) { ligneMAS315.children[j].innerHTML = listStudent[i][1][0] } //note math
        if (j == 5) { ligneMAS315.children[j].innerHTML = listStudent[i][1][1] } //coef math
        if (j == 6) { ligneMAS315.children[j].innerHTML = listStudent[i][1][2] } //total note math * coef
        if (j == 7) { ligneMAS315.children[j].innerHTML = listStudent[i][1][3] } //moyenne donc (totalmath + totalinfo)/2
        if (j == 8) { ligneMAS315.children[j].innerHTML = listStudent[i][1][4] /*ligneMAS315.children[j].innerHTML =  mds1sort.indexof(mds111[i]['note_Examen'])*/ } //Rang
        if (j == 9) {
            if (((listStudent[i][1][0] >= 7 && listStudent[i][1][0] < 10) && listStudent[i][1][3] >= 10)) { ligneMAS315.children[j].innerHTML = "Validée" } else if ((listStudent[i][1][0] >= 10)) { ligneMAS315.children[j].innerHTML = "Validée" } else if (listStudent[i][1][0] < 10) { ligneMAS315.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 10) { if (listStudent[i][1][8] == "Rattrapage") { ligneMAS315.children[j].innerHTML = listStudent[i][1][8] } else { ligneMAS315.children[j].innerHTML = "Janvier 2023" } } //Session
        if (j == 11) { if ((listStudent[i][1][0] >= 7 && listStudent[i][1][3] >= 10) || (listStudent[i][1][0] >= 10)) { ligneMAS315.children[j].innerHTML = listStudent[i][1][6] } else { ligneMAS315.children[j].innerHTML = 0 } } //Crédits
    }

    //LIGNE MAS 325
    var ligneMAS325 = tbody.children[1]
    for (j = 0; j <= ligneMAS325.childElementCount - 1; j++) {
        if (j == 2) { ligneMAS325.children[j].innerHTML = listStudent[i][2][0] } //note info
        if (j == 3) { ligneMAS325.children[j].innerHTML = listStudent[i][2][1] } //coef info
        if (j == 4) { /*val=ligneMAS325.children[2].innerHTML*ligneMAS325.children[3].innerHTML; val= val.toFixed(2); val = parseFloat(val);*/ ligneMAS325.children[j].innerHTML = listStudent[i][2][2] } //total note math * coef
        if (j == 5) { ligneMAS325.children[j].innerHTML = listStudent[i][2][4] } //Rang
        if (j == 6) {
            if (((listStudent[i][2][0] >= 7 && listStudent[i][2][0] < 10) && listStudent[i][1][3] >= 10)) { ligneMAS325.children[j].innerHTML = "Validée" } else if ((listStudent[i][2][0] >= 10)) { ligneMAS325.children[j].innerHTML = "Validée" } else if (listStudent[i][2][0] < 10) { ligneMAS325.children[j].innerHTML = "Non validée" }
        }
        if (j == 7) { if (listStudent[i][2][8] == "Rattrapage") { ligneMAS325.children[j].innerHTML = listStudent[i][2][8] } else { ligneMAS325.children[j].innerHTML = "Janvier 2023" } } //Session
        if (j == 8) { if ((listStudent[i][2][0] >= 7 && listStudent[i][1][3] >= 10) || (listStudent[i][2][0] >= 10)) { ligneMAS325.children[j].innerHTML = listStudent[i][2][6] } else { ligneMAS325.children[j].innerHTML = 0 } } //Crédits
    }

    //LIGNE MAS 335
    var ligneMAS335 = tbody.children[2]
    for (j = 0; j <= ligneMAS335.childElementCount - 1; j++) {
        if (j == 2) { ligneMAS335.children[j].innerHTML = listStudent[i][3][0] } //note info
        if (j == 3) { ligneMAS335.children[j].innerHTML = listStudent[i][3][1] } //coef info
        if (j == 4) { ligneMAS335.children[j].innerHTML = listStudent[i][3][2] } //total note math * coef
        if (j == 5) { ligneMAS335.children[j].innerHTML = listStudent[i][3][4] } //Rang
        if (j == 6) {
            //if (listStudent[i][3][0] >= 10) { ligneMAS335.children[j].innerHTML = "Validée" } else { ligneMAS335.children[j].innerHTML = "Non validée" } 
            if (((listStudent[i][3][0] >= 7 && listStudent[i][3][0] < 10) && listStudent[i][1][3] >= 10)) { ligneMAS335.children[j].innerHTML = "Validée" } else if ((listStudent[i][3][0] >= 10)) { ligneMAS335.children[j].innerHTML = "Validée" } else if (listStudent[i][3][0] < 10) { ligneMAS335.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 7) { if (listStudent[i][3][8] == "Rattrapage") { ligneMAS335.children[j].innerHTML = listStudent[i][3][8] } else { ligneMAS335.children[j].innerHTML = "Janvier 2023" } }
        if (j == 8) { if ((listStudent[i][3][0] >= 7 && listStudent[i][1][3] >= 10) || (listStudent[i][3][0] >= 10)) { ligneMAS335.children[j].innerHTML = listStudent[i][3][6] } else { ligneMAS335.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE MAS 345
    var ligneMAS345 = tbody.children[3]
    for (j = 0; j <= ligneMAS345.childElementCount - 1; j++) {
        if (j == 2) { ligneMAS345.children[j].innerHTML = listStudent[i][4][0] } //note info
        if (j == 3) { ligneMAS345.children[j].innerHTML = listStudent[i][4][1] } //coef info
        if (j == 4) { ligneMAS345.children[j].innerHTML = listStudent[i][4][2] } //total note math * coef
        if (j == 5) { ligneMAS345.children[j].innerHTML = listStudent[i][4][4] } //Rang
        if (j == 6) {
            //if (listStudent[i][4][0] >= 10) { ligneMAS345.children[j].innerHTML = "Validée" } else { ligneMAS345.children[j].innerHTML = "Non validée" } 
            if (((listStudent[i][4][0] >= 7 && listStudent[i][4][0] < 10) && listStudent[i][1][3] >= 10)) { ligneMAS345.children[j].innerHTML = "Validée" } else if ((listStudent[i][4][0] >= 10)) { ligneMAS345.children[j].innerHTML = "Validée" } else if (listStudent[i][4][0] < 10) { ligneMAS345.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 7) { if (listStudent[i][4][8] == "Rattrapage") { ligneMAS345.children[j].innerHTML = listStudent[i][4][8] } else { ligneMAS345.children[j].innerHTML = "Janvier 2023" } }
        if (j == 8) { if ((listStudent[i][4][0] >= 7 && listStudent[i][1][3] >= 10) || (listStudent[i][4][0] >= 10)) { ligneMAS345.children[j].innerHTML = listStudent[i][4][6] } else { ligneMAS345.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE MAS 355
    var ligneMAS355 = tbody.children[4]
    for (j = 0; j <= ligneMAS355.childElementCount - 1; j++) {
        if (j == 3) { ligneMAS355.children[j].innerHTML = listStudent[i][5][0] } //note math
        if (j == 4) { ligneMAS355.children[j].innerHTML = listStudent[i][5][1] } //coef math
        if (j == 5) { ligneMAS355.children[j].innerHTML = listStudent[i][5][2] } //total note math * coef
        if (j == 6) { ligneMAS355.children[j].innerHTML = listStudent[i][5][3] }
        if (j == 7) { ligneMAS355.children[j].innerHTML = listStudent[i][5][4] } //Rang
        if (j == 8) {
            if (((listStudent[i][5][0] >= 7 && listStudent[i][5][0] < 10) && listStudent[i][5][3] >= 10)) { ligneMAS355.children[j].innerHTML = "Validée" } else if ((listStudent[i][5][0] >= 10)) { ligneMAS355.children[j].innerHTML = "Validée" } else if (listStudent[i][5][0] < 10) { ligneMAS355.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 9) { if (listStudent[i][5][8] == "Rattrapage") { ligneMAS355.children[j].innerHTML = listStudent[i][5][8] } else { ligneMAS355.children[j].innerHTML = "Janvier 2023" } }
        if (j == 10) { if ((listStudent[i][5][0] >= 7 && listStudent[i][5][3] >= 10) || (listStudent[i][5][0] >= 10)) { ligneMAS355.children[j].innerHTML = listStudent[i][5][6] } else { ligneMAS355.children[j].innerHTML = 0 } } //Crédits
    }


    //LIGNE MAS 365
    var ligneMAS365 = tbody.children[5]
    for (j = 0; j <= ligneMAS365.childElementCount - 1; j++) {
        if (j == 2) { ligneMAS365.children[j].innerHTML = listStudent[i][6][0] } //note info
        if (j == 3) { ligneMAS365.children[j].innerHTML = listStudent[i][6][1] } //coef info
        if (j == 4) { ligneMAS365.children[j].innerHTML = listStudent[i][6][2] } //total note math * coef
        if (j == 5) { ligneMAS365.children[j].innerHTML = listStudent[i][6][4] } //Rang
        if (j == 6) {
            if (((listStudent[i][6][0] >= 7 && listStudent[i][6][0] < 10) && listStudent[i][5][3] >= 10)) { ligneMAS365.children[j].innerHTML = "Validée" } else if ((listStudent[i][6][0] >= 10)) { ligneMAS365.children[j].innerHTML = "Validée" } else if (listStudent[i][6][0] < 10) { ligneMAS365.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 7) { if (listStudent[i][6][8] == "Rattrapage") { ligneMAS365.children[j].innerHTML = listStudent[i][6][8] } else { ligneMAS365.children[j].innerHTML = "Janvier 2023" } } //Session
        if (j == 8) { if ((listStudent[i][6][0] >= 7 && listStudent[i][5][3] >= 10) || (listStudent[i][6][0] >= 10)) { ligneMAS365.children[j].innerHTML = listStudent[i][6][6] } else { ligneMAS365.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LINE DEs RESULTATS
    resultat = tbody.children[6]
    resultat.style.backgroundColor = "#C7B54D"
    for (j = 0; j <= resultat.childElementCount - 1; j++) {
        if (j == 1) { resultat.children[1].innerHTML = listStudent[i][7][0] }
        if (j == 2) { resultat.children[2].innerHTML = listStudent[i][7][1] }
        if (j == 3) { resultat.children[j].innerHTML = listStudent[i][7][2] }
        if (j == 4) { resultat.children[j].innerHTML = mydata[2].indexOf(listStudent[i][7][2]) + 1 }
        if (j == 6) { resultat.children[j].innerHTML = sommeInt6(ligneMAS315.children[11].innerHTML, ligneMAS325.children[8].innerHTML, ligneMAS335.children[8].innerHTML, ligneMAS345.children[8].innerHTML, ligneMAS355.children[10].innerHTML, ligneMAS365.children[8].innerHTML) } /**TOtal Crédit */
    }

    //Tbody
    var body3 = clone.children[2].children[2].children[1].children[1]

    //LIGNE 0
    var ligne0 = body3.children[0]
    for (j = 0; j <= ligne0.childElementCount - 1; j++) {
        if (j == 2) { ligne0.children[2].innerHTML = `${resultat.children[3].innerHTML} / 20` }
        if (j == 4) { ligne0.children[j].innerHTML = `${mydata[2][0]} / 20` }
    }

    //LIGNE 1
    var ligne1 = body3.children[1]
    for (j = 0; j <= ligne1.childElementCount - 1; j++) {
        if (j == 2) { ligne1.children[j].innerHTML = `${mydata[3]} / 20` }
        if (j == 4) {
            v = mydata[2].length - 1;
            ligne1.children[j].innerHTML = `${mydata[2][v]} / 20`
        }
    }

    //LLIGNE 2
    var ligne2 = body3.children[2]
    for (j = 0; j <= ligne1.childElementCount - 1; j++) {
        if (j == 5) { ligne2.children[j].innerHTML = `${mydata[2].indexOf(listStudent[i][7][2])+1} sur ${mydata[1].length}` }
        if (j == 4) {}
    }

    /*###################### SEMESTRE 6 ################################################################################### */
    semestre6 = mydata[9]
    s6body = clone.children[2].children[3].children[0].children[1]

    //LIGNE MAS 316
    /*var*/
    ligneMAS316 = s6body.children[0]
    for (j = 0; j <= ligneMAS316.childElementCount - 1; j++) {
        if (j == 0) { ligneMAS316.children[j].innerHTML = "SEMESTRE 6" }
        if (j == 2) { ligneMAS316.children[j].innerHTML = "MAS316" }
        if (j == 3) { ligneMAS316.children[j].innerHTML = "Management des infrastructures et équipements sportifs" }

        if (j == 4) { ligneMAS316.children[j].innerHTML = semestre6[i][1][0] } //note math
        if (j == 5) { ligneMAS316.children[j].innerHTML = semestre6[i][1][1] } //coef math
        if (j == 6) { ligneMAS316.children[j].innerHTML = semestre6[i][1][2] } //total note math * coef
        if (j == 7) { ligneMAS316.children[j].innerHTML = semestre6[i][1][3] } //moyenne donc (totalmath + totalinfo)/2
        if (j == 8) { ligneMAS316.children[j].innerHTML = semestre6[i][1][4] /*ligneMAS316.children[j].innerHTML =  mds1sort.indexof(mds111[i]['note_Examen'])*/ } //Rang
        if (j == 9) {
            if (((semestre6[i][1][0] >= 7 && semestre6[i][1][0] < 10) && semestre6[i][1][3] >= 10)) { ligneMAS316.children[j].innerHTML = "Validée" } else if ((semestre6[i][1][0] >= 10)) { ligneMAS316.children[j].innerHTML = "Validée" } else if (semestre6[i][1][0] < 7) { ligneMAS316.children[j].innerHTML = "Non validée" }
            /*if (semestre6[i][1][5]) {
                ligneMAS316.children[9].innerHTML = "Validée"
            } else { ligneMAS316.children[9].innerHTML = "Non validée" }*/
        } //Mention
        if (j == 10) { ligneMAS316.children[j].innerHTML = 'Mai 2023' } //Session
        if (j == 11) {
            if ((semestre6[i][1][0] >= 7 && semestre6[i][1][3] >= 10) || (semestre6[i][1][0] >= 10)) { ligneMAS316.children[j].innerHTML = semestre6[i][1][6] } else { ligneMAS316.children[j].innerHTML = 0 }
        } //Crédits
    }

    //LIGNE MAS 325
    /*var*/
    ligneMAS326 = s6body.children[1]
    for (j = 0; j <= ligneMAS326.childElementCount - 1; j++) {
        if (j == 0) { ligneMAS326.children[j].innerHTML = "MAS326" }
        if (j == 1) { ligneMAS326.children[j].innerHTML = "Management des ressources financières" }


        if (j == 2) { ligneMAS326.children[j].innerHTML = semestre6[i][2][0] } //note info
        if (j == 3) { ligneMAS326.children[j].innerHTML = semestre6[i][2][1] } //coef info
        if (j == 4) { /*val=ligneMAS326.children[2].innerHTML*ligneMAS326.children[3].innerHTML; val= val.toFixed(2); val = parseFloat(val);*/ ligneMAS326.children[j].innerHTML = semestre6[i][2][2] } //total note math * coef
        if (j == 5) { ligneMAS326.children[j].innerHTML = semestre6[i][2][4] } //Rang
        if (j == 6) {
            if (((semestre6[i][2][0] >= 7 && semestre6[i][2][0] < 10) && semestre6[i][1][3] >= 10)) { ligneMAS326.children[j].innerHTML = "Validée" } else if ((semestre6[i][2][0] >= 10)) { ligneMAS326.children[j].innerHTML = "Validée" } else /*if ( /*semestre6[i][2][0] < 7 || semestre6[i][2][0] < 10)*/ { ligneMAS326.children[j].innerHTML = "Non validée" }
            //if (semestre6[i][2][5]) { ligneMAS326.children[6].innerHTML = "Validée" } else { ligneMAS326.children[6].innerHTML = "Non validée" }
        }
        if (j == 7) { ligneMAS326.children[j].innerHTML = 'Mai 2023' } //Session
        if (j == 8) { if ((semestre6[i][2][0] >= 7 && semestre6[i][1][3] >= 10) || (semestre6[i][2][0] >= 10)) { ligneMAS326.children[j].innerHTML = semestre6[i][2][6] } else { ligneMAS326.children[j].innerHTML = 0 } } //Crédits
    }

    //LIGNE MAS 335
    /*var*/
    ligneMAS336 = s6body.children[2]
    for (j = 0; j <= ligneMAS336.childElementCount - 1; j++) {
        if (j == 0) { ligneMAS336.children[j].innerHTML = "MAS336" }
        if (j == 1) { ligneMAS336.children[j].innerHTML = "Gestion des Ressources Humaines" }

        if (j == 2) { ligneMAS336.children[j].innerHTML = semestre6[i][3][0] } //note info
        if (j == 3) { ligneMAS336.children[j].innerHTML = semestre6[i][3][1] } //coef info
        if (j == 4) { /*val=ligneMAS336.children[2].innerHTML*ligneMAS336.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneMAS336.children[j].innerHTML = semestre6[i][3][2] } //total note math * coef
        if (j == 5) { ligneMAS336.children[j].innerHTML = semestre6[i][3][4] } //Rang
        if (j == 6) {
            if (((semestre6[i][3][0] >= 7 && semestre6[i][3][0] < 10) && semestre6[i][1][3] >= 10)) { ligneMAS336.children[j].innerHTML = "Validée" } else if ((semestre6[i][3][0] >= 10)) { ligneMAS336.children[j].innerHTML = "Validée" } else if (semestre6[i][3][0] < 7) { ligneMAS336.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 7) { ligneMAS336.children[j].innerHTML = 'Mai 2023' } //Session
        if (j == 8) { if ((semestre6[i][3][0] >= 7 && semestre6[i][1][3] >= 10) || (semestre6[i][3][0] >= 10)) { ligneMAS336.children[j].innerHTML = semestre6[i][3][6] } else { ligneMAS336.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE MAS 345
    /*var*/
    ligneMAS346 = s6body.children[3]
    for (j = 0; j <= ligneMAS346.childElementCount - 1; j++) {
        if (j == 0) { ligneMAS346.children[j].innerHTML = "MAS346" }
        if (j == 1) { ligneMAS346.children[j].innerHTML = "Stage Professionnel" }

        if (j == 2) { ligneMAS346.children[j].innerHTML = semestre6[i][4][0] } //note info
        if (j == 3) { ligneMAS346.children[j].innerHTML = semestre6[i][4][1] } //coef info
        if (j == 4) { ligneMAS346.children[j].innerHTML = semestre6[i][4][2] } //total note math * coef
        if (j == 5) { ligneMAS346.children[j].innerHTML = semestre6[i][4][4] } //Rang
        if (j == 6) {
            if (((semestre6[i][4][0] >= 7 && semestre6[i][4][0] < 10) && semestre6[i][1][3] >= 10)) { ligneMAS346.children[j].innerHTML = "Validée" } else if ((semestre6[i][4][0] >= 10)) { ligneMAS346.children[j].innerHTML = "Validée" } else if (semestre6[i][4][0] < 7) { ligneMAS346.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 7) { ligneMAS346.children[j].innerHTML = 'Mai 2023' } //Session
        if (j == 8) { if ((semestre6[i][4][0] >= 7 && semestre6[i][1][3] >= 10) || (semestre6[i][4][0] >= 10)) { ligneMAS346.children[j].innerHTML = semestre6[i][4][6] } else { ligneMAS346.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EVE356
    /*var*/
    ligneEVE356 = s6body.children[4]
    for (j = 0; j <= ligneEVE356.childElementCount - 1; j++) {
        if (j == 1) { ligneEVE356.children[j].innerHTML = "EVE356" }
        if (j == 2) { ligneEVE356.children[j].innerHTML = "Outils de soutien à l'Organisation des Evènements Sportifs" }

        if (j == 3) { ligneEVE356.children[j].innerHTML = semestre6[i][5][0] } //note math
        if (j == 4) { ligneEVE356.children[j].innerHTML = semestre6[i][5][1] } //coef math
        if (j == 5) { ligneEVE356.children[j].innerHTML = semestre6[i][5][2] } //total note math * coef
        if (j == 6) { ligneEVE356.children[j].innerHTML = semestre6[i][5][3] }
        if (j == 7) { ligneEVE356.children[j].innerHTML = semestre6[i][5][4] } //Rang
        if (j == 8) {
            //ligneEVE356.children[j].innerHTML = "zeze"
            if (((semestre6[i][5][0] >= 7 && semestre6[i][5][0] < 10) && semestre6[i][5][3] >= 10)) { ligneEVE356.children[j].innerHTML = "Validée" } else if ((semestre6[i][5][0] >= 10)) { ligneEVE356.children[j].innerHTML = "Validée" } else if (semestre6[i][5][0] < 10) { ligneEVE356.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 9) { ligneEVE356.children[j].innerHTML = 'Mai 2023' } //Session
        if (j == 10) { if ((semestre6[i][5][0] >= 7 && semestre6[i][5][3] >= 10) || (semestre6[i][5][0] >= 10)) { ligneEVE356.children[j].innerHTML = semestre6[i][5][6] } else { ligneEVE356.children[j].innerHTML = 0 } } //Crédits
    }


    //LIGNE EVE366
    /*var*/
    ligneEVE366 = s6body.children[5]
    for (j = 0; j <= ligneEVE366.childElementCount - 1; j++) {
        if (j == 0) { ligneEVE366.children[j].innerHTML = "EVE366" }
        if (j == 1) { ligneEVE366.children[j].innerHTML = "Méthodologie de Rédaction des Rapports de Stage" }

        if (j == 2) { ligneEVE366.children[j].innerHTML = semestre6[i][6][0] } //note info
        if (j == 3) { ligneEVE366.children[j].innerHTML = semestre6[i][6][1] } //coef info
        if (j == 4) { ligneEVE366.children[j].innerHTML = semestre6[i][6][2] } //total note math * coef
        if (j == 5) { ligneEVE366.children[j].innerHTML = semestre6[i][6][4] } //Rang
        if (j == 6) {

            if (((semestre6[i][6][0] >= 7 && semestre6[i][6][0] < 10) && semestre6[i][5][3] >= 10)) { ligneEVE366.children[j].innerHTML = "Validée" } else if ((semestre6[i][6][0] >= 10)) { ligneEVE366.children[j].innerHTML = "Validée" } else /*if (semestre6[i][6][0] < 7)*/ { ligneEVE366.children[j].innerHTML = "Non validée" }
        } //Mention
        if (j == 7) { ligneEVE366.children[j].innerHTML = 'Mai 2023' } //Session
        if (j == 8) { if ((semestre6[i][6][0] >= 7 && semestre6[i][5][3] >= 10) || (semestre6[i][6][0] >= 10)) { ligneEVE366.children[j].innerHTML = semestre6[i][6][6] } else { ligneEVE366.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LINE DEs RESULTATS
    resultats6 = s6body.children[6]
    resultats6.style.backgroundColor = "#C7B54D"
    for (j = 0; j <= resultats6.childElementCount - 1; j++) {
        if (j == 0) { resultats6.children[j].innerHTML = 'RESULTATS SEMESTRE 6' }
        if (j == 1) {
            resultats6.children[1].innerHTML = semestre6[i][7][0] /*sommeInt1(ligneMDS111.children[5].innerHTML,ligneMDS111b.children[3].innerHTML,ligneMDS112.children[3].innerHTML,ligneMDS112b.children[3].innerHTML,ligneMDS113.children[4].innerHTML,ligneMDS114.children[3].innerHTML,ligneMDS115.children[3].innerHTML,ligneMDS116.children[3].innerHTML,ligneMDS117.children[4].innerHTML,ligneMDS117b.children[3].innerHTML);*/
        }
        if (j == 2) { resultats6.children[2].innerHTML = semestre6[i][7][1] } /*sommeFloat(ligneMDS111b.children[4].innerHTML, ligneMDS111.children[6].innerHTML, ligneMDS112.children[4].innerHTML, ligneMDS113.children[5].innerHTML, ligneMDS114.children[4].innerHTML, ligneMDS115.children[4].innerHTML,ligneMDS116.children[4].innerHTML, ligneMDS117.children[5].innerHTML, ligneMDS112b.children[4].innerHTML, ligneMDS117b.children[4].innerHTML) }*/
        if (j == 3) { resultats6.children[j].innerHTML = semestre6[i][7][2] }

        if (j == 4) { resultats6.children[j].innerHTML = mydata[10].indexOf(semestre6[i][7][2]) + 1 }
        if (j == 5) { resultats6.children[j].innerHTML = 'Total Crédits Semestre 6' }
        if (j == 6) { resultats6.children[j].innerHTML = sommeInt6(ligneMAS316.children[11].innerHTML, ligneMAS326.children[8].innerHTML, ligneMAS336.children[8].innerHTML, ligneMAS346.children[8].innerHTML, ligneEVE356.children[10].innerHTML, ligneEVE366.children[8].innerHTML) } /**TOtal Crédit */
    }

    // SEMESTRE 5 & 6 RESULT
    resultats5s6 = clone.children[2].children[4]

    ligneresultat = resultats5s6.children[1].children[1]

    for (j = 0; j <= ligneresultat.childElementCount - 1; j++) {
        if (j == 0) { ligneresultat.children[j].innerHTML = sommeInt2(resultat.children[1].innerHTML, resultats6.children[1].innerHTML) }
        if (j == 1) { ligneresultat.children[j].innerHTML = sommeFloat2(resultat.children[2].innerHTML, resultats6.children[2].innerHTML) }
        if (j == 2) { ligneresultat.children[j].innerHTML = `${(parseFloat(ligneresultat.children[1].innerHTML) / ligneresultat.children[0].innerHTML).toFixed(2)} / 20` }
        if (j == 3) {
            var total = parseFloat(ligneresultat.children[1].innerHTML)
            ligneresultat.children[j].innerHTML = `${mydata[11].indexOf(total) + 1}  /  ${semestre6.length}`
        }
        if (j == 4) { ligneresultat.children[j].innerHTML = `${ sommeInt2(resultat.lastChild.innerHTML, resultats6.lastChild.innerHTML) }  /  60` }
        if (j == 5) {
            var moyenne = parseFloat(ligneresultat.children[2].innerHTML)
            if (moyenne >= 10) { ligneresultat.children[j].innerHTML = "ADMIS(E)" } else { ligneresultat.children[j].innerHTML = "ECHEC" }
        }
    }



    return (clone)
}


//FONCTIONS
function Moyenne3(a, b, c, coef) {
    a = parseFloat(a);
    b = parseFloat(b);
    c = parseFloat(c);
    result = (a + b + c) / coef;
    result = result.toFixed(2);
    result = parseFloat(result);
    return (result)
}

function Moyenne2(a, b, coef) {
    a = parseFloat(a);
    b = parseFloat(b);
    result = (a + b) / coef;
    result = result.toFixed(2);
    result = parseFloat(result);
    return (result)
}

function Moyenne4(a, b, c, d, coef) {
    a = parseFloat(a);
    b = parseFloat(b);
    c = parseFloat(c);
    d = parseFloat(d);
    result = (a + b + c + d) / coef;
    result = result.toFixed(2);
    result = parseFloat(result);
    return (result)
}

function sommeInt1(a, b, c, d, e, f, g, h, i, j) {
    a = parseInt(a)
    b = parseInt(b);
    c = parseInt(c);
    d = parseInt(d);
    e = parseInt(e);
    f = parseInt(f);
    g = parseInt(g);
    h = parseInt(h);
    i = parseInt(i);
    j = parseInt(j);

    result = a + b + c + d + e + f + g + h + i + j

    return (result)
}

function sommeInt2(a, b) {
    a = parseInt(a)
    b = parseInt(b);

    var result = a + b

    return (result)
}

function sommeInt(a, b, c, d, e, f, g) {
    a = parseInt(a);
    b = parseInt(b);
    c = parseInt(c);
    d = parseInt(d);
    e = parseInt(e);
    f = parseInt(f);
    g = parseInt(g);

    result = a + b + c + d + e + f + g
    return (result)
}

function sommeIntmds(a, b, c, d, e, f, g, h) {
    a = parseInt(a);
    b = parseInt(b);
    c = parseInt(c);
    d = parseInt(d);
    e = parseInt(e);
    f = parseInt(f);
    g = parseInt(g);
    h = parseInt(h);


    result = a + b + c + d + e + f + g + h
    return (result)
}

function sommeInt6(a, b, c, d, e, f) {
    a = parseInt(a);
    b = parseInt(b);
    c = parseInt(c);
    d = parseInt(d);
    e = parseInt(e);
    f = parseInt(f);
    //g = parseInt(g);

    result = a + b + c + d + e + f /*+ g*/
    return (result)
}

function sommeInt9(a, b, c, d, e, f, g, h, i) {
    a = parseInt(a);
    b = parseInt(b);
    c = parseInt(c);
    d = parseInt(d);
    e = parseInt(e);
    f = parseInt(f);
    g = parseInt(g);
    h = parseInt(h);
    i = parseInt(i)

    var result = a + b + c + d + e + f + g + h + i
    return (result)
}

function sommeInt12(a, b, c, d, e, f, g, h, i) {
    a = parseInt(a);
    b = parseInt(b);
    c = parseInt(c);
    d = parseInt(d);
    e = parseInt(e);
    f = parseInt(f);
    g = parseInt(g);
    h = parseInt(h);
    i = parseInt(i)

    result = a + b + c + d + e + f + g + h + i
    return (result)
}

function sommeInt8(a, b, c, d, e, f, g, h) {
    a = parseInt(a);
    b = parseInt(b);
    c = parseInt(c);
    d = parseInt(d);
    e = parseInt(e);
    f = parseInt(f);
    g = parseInt(g);
    h = parseInt(h);

    result = a + b + c + d + e + f + g + h
    return (result)
}

function sommeFloat(a, b, c, d, e, f, g, h) {
    a = parseFloat(a)
    b = parseFloat(b);
    c = parseFloat(c);
    d = parseFloat(d);
    e = parseFloat(e);
    f = parseFloat(f);
    g = parseFloat(g);
    h = parseFloat(h);

    result = a + b + c + d + e + f + g + h + i + j
    result = result.toFixed(2)
    result = parseFloat(result)

    return (result)
}

function sommeFloat2(a, b) {
    a = parseFloat(a)
    b = parseFloat(b);

    var result = a + b
    result = result.toFixed(2)
    result = parseFloat(result)

    return (result)
}

function triCroissant(b) {
    for (i = 0; i <= b.length; i++) {

        for (j = i + 1; j <= b.length; j++) {
            if (b[i] >= b[j]) {
                tmp = b[i]
                b[i] = b[j]
                b[j] = tmp
            }
        }
    }

    return (b)
}

function triDecroissant(b) {
    for (i = 0; i <= b.length; i++) {

        for (j = i + 1; j <= b.length; j++) {
            if (b[i] <= b[j]) {
                tmp = b[i]
                b[i] = b[j]
                b[j] = tmp
            }
        }
    }

    return (b)
}

function formatAsArray(b) {
    ar = [];
    for (var i = 0; i <= b.length; i++) {
        console.log(b[i]['note_Examen']);
    }
    return (ar)
}

function epuration(a) {
    var sort111 = []
    for (k = 0; k <= a.length - 1; k++) {
        sort111[k] = a[k]["note_Examen"]
    }
    //sort111 = triDecroissant(sort111)
    return (sort111)
}

function stringToIntArray(a) {
    //val = []

    for (k = 0; k <= a.length - 1; k++) {
        tmp = parseFloat(a[k]);
        a[k] = tmp;
    }
    return (a)
}
/*return (a)
}*/