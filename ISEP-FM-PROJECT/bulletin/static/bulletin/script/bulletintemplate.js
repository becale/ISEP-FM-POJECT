window.addEventListener('load',()=>{
    //Recuperation de la variable des données
     mydata = JSON.parse(document.getElementById('semestre1MDS').textContent);
     
    
    b = [...mydata[5]]
    mds12sort = b[0]
    ///////////////////////////////////
    c = [...mydata[6]]
    ///////////////////////////////////
    d = [...mydata[7]]
    ///////////////////////////////////
    e = [...mydata[8]]
    ///////////////////////////////////
    f = [...mydata[9]]
    ///////////////////////////////////
    g = [...mydata[10]]
    ///////////////////////////////////
    h = [...mydata[11]]
    ///////////////////////////////////
     console.log(mydata) 

    //Génération dynamique du tableau de bulletin
    //TEST GENERAL POUR TOUS LES BULLETINS SEMESTRE  1 3 5S
    
    body = document.getElementById('body')

    if( mydata[0] == 'GESTION' ){
      containerrr = GenerateBullMDS1Semestre1()
      listcontainer = document.createElement('div')
      for(i=0; i<mydata[1].length; i++){
        clone = containerrr.cloneNode(true);
        //Execution des traitements sur container
        clone = BullMDS1(clone)
        //Puis ajout au containerList
        listcontainer.appendChild(clone)
      }
      //Fixation de ContainerList sur le body de la page
      body.appendChild(listcontainer)
    }
    else if ( mydata[0] == 'STAPS1'){    
      containeer = GenerateBullStaps1Semestre1()
      listcontainer = document.createElement('div')
      for(i=0; i<mydata[1].length; i++){
        clone = containeer.cloneNode(true);
        //Execution des traitements sur container
        //clone = BullMDS1(clone)
        //Puis ajout au containerList
        listcontainer.appendChild(clone)
      }
      //Fixation de ContainerList sur le body de la page
      body.appendChild(listcontainer)
   }
    else if ( mydata[0] == 'STAPS2' ){
      body = document.getElementById('body')
      containeer = GenerateBullStaps2Semestre3()
      listcontainer = document.createElement('div')
      for(i=0; i<mydata[1].length; i++){
        clone = containeer.cloneNode(true);
        //Execution des traitements sur container
        //clone = BullMDS1(clone)
        //Puis ajout au containerList
        listcontainer.appendChild(clone)
      }
      //Fixation de ContainerList sur le body de la page
      body.appendChild(listcontainer)
    }
    else if( mydata[0] == 'EVENEMENTIEL' ){
      containeer = GenerateBullEVEsemestre5()
      listcontainer = document.createElement('div')
      for(i=0; i<mydata[1].length; i++){
        clone = containeer.cloneNode(true);
        //Execution des traitements sur container
        //clone = BullMDS1(clone)
        //Puis ajout au containerList
        listcontainer.appendChild(clone)
      }
      //Fixation de ContainerList sur le body de la page
      var body = document.getElementById('body')
      body.appendChild(listcontainer)
    }
    else if( mydata[0] == 'MSO' ){ 
      containeer = GenerateBullMSOsemestre5()
      listcontainer = document.createElement('div')
      for(i=0; i<mydata[1].length; i++){
        clone = containeer.cloneNode(true);
        //Execution des traitements sur container
        //clone = BullMDS1(clone)
        //Puis ajout au containerList
        listcontainer.appendChild(clone)
      }
      //Fixation de ContainerList sur le body de la page
      body.appendChild(listcontainer)
    }
})



/**
 * DECLARATION DES FONCTIONS DE GENERATION DES BULLETTINS DES SEMESTRES 1, 3, 5
 */
/*DECLARATION S1 MDS*/
function GenerateBullMDS1Semestre1(){
  //title
  var br = document.createElement('br')
  var slogan=document.createElement('div')
  slogan.innerHTML=`Au-delà de la limite`
  slogan.setAttribute('class','slogan')

  var titleinfo=document.createElement('div')
  titleinfo.innerHTML=`BP : 7403 Yaoundé  Tél : (237) 695 548 821 / 653 764 050 <br> Site Web : www.institutfrançoisembango.com Email : isep_fm@yahoo.com`
  titleinfo.setAttribute('class', 'title-info')
  
  title=document.createElement('div')
  title.setAttribute("id", "title")
  title.appendChild(slogan)
  title.appendChild(titleinfo)

  //Logo
  var headleft=document.createElement('div')
  headleft.setAttribute('id', 'head-left')
  
  var image=document.createElement('img')
  image.setAttribute("src",`/static/bulletin/image/logo.jpeg`)
  image.setAttribute("alt","logo")

  var logo=document.createElement('div')
  logo.setAttribute("id","logo")
  logo.appendChild(image)

  var headright=document.createElement('div')
  headright.setAttribute('id','head-right')

  containertitle=document.createElement('div')
  containertitle.appendChild(headleft)
  containertitle.appendChild(logo)
  containertitle.appendChild(headright)

  logoTitle=document.createElement('div')
  logoTitle.setAttribute('id','logo-title')
  logoTitle.appendChild(containertitle)
  logoTitle.appendChild(title)

  header=document.createElement('div')
  header.appendChild(logoTitle)
  
  hr=document.createElement('hr')

  first=document.createElement('div')
  first.appendChild(header)
  first.appendChild(hr)

  //MAIN
  var bullcheck=document.createElement('div')
  bullcheck.setAttribute('id','bull-check')
  bullcheck.innerHTML=`DAF/SER/DFF/FFFF/FFFF`

  var bulltitle=document.createElement('div')
  bulltitle.setAttribute('id','bull-title')
  bulltitle.innerHTML=`BULLETIN DE NOTES SEMESTRE 1`

  var bullchecktitle=document.createElement('div')
  bullchecktitle.setAttribute('id','bull-check-title')
  bullchecktitle.appendChild(bullcheck)
  bullchecktitle.appendChild(bulltitle)

  //info student
  var info1=document.createElement('div')
  info1.setAttribute('class','info-student-style')
  info1.innerHTML=`Filière &nbsp;&nbsp; : GESTION`
  var info2=document.createElement('div')
  info2.setAttribute('class','info-student-style')
  info2.innerHTML=`Spécialité &nbsp;:  MDS`
  var info3=document.createElement('div')
  info3.setAttribute('class','info-student-style')
  info3.innerHTML=`Nom (s) &nbsp; &nbsp; : `
  var info4=document.createElement('div')
  info4.setAttribute('class','info-student-style')
  info4.innerHTML=`Prénom (s) : `
  var info5=document.createElement('div')
  info5.setAttribute('class','info-student-style')
  info5.innerHTML=`Nationalité : Camerounais(e)`

  var infostudent1=document.createElement('div')
  infostudent1.setAttribute('id','info-student-1')
  infostudent1.appendChild(info1)
  infostudent1.appendChild(info2)
  infostudent1.appendChild(info3)
  infostudent1.appendChild(info4)
  infostudent1.appendChild(info5)
  
  var info11=document.createElement('div')
  info11.setAttribute('class','info-student-style')
  info11.innerHTML=`Grade : BTS  `
  var info22=document.createElement('div')
  info22.setAttribute('class','info-student-style')
  info22.innerHTML=`Matricule : `
  var info33=document.createElement('div')
  info33.setAttribute('class','info-student-style')
  info33.innerHTML=`Date De Naissance : `
  var info44=document.createElement('div')
  info44.setAttribute('class','info-student-style')
  info44.innerHTML=`Lieu De Naissance : `
  var info55=document.createElement('div')
  info55.setAttribute('class','info-student-style')
  info55.innerHTML=`Année Académique : `

  var infostudent2=document.createElement('div')
  infostudent2.setAttribute('id','info-student-2')
  infostudent2.appendChild(info11)
  infostudent2.appendChild(info22)
  infostudent2.appendChild(info33)
  infostudent2.appendChild(info44)
  infostudent2.appendChild(info55)

  var info111=document.createElement('div')
  info111.innerHTML=`Niveau: I`

  var infostudent3=document.createElement('div')
  infostudent3.setAttribute('id','info-student-3')
  infostudent3.appendChild(info111)

  infostudent=document.createElement('div')
  infostudent.setAttribute('id','info-student')
  infostudent.appendChild(infostudent1)
  infostudent.appendChild(infostudent2)
  infostudent.appendChild(infostudent3)

  //table1
  //thead -Line 1
  var tr1=document.createElement('tr')
  var thvalue=["","Groupe UE","Code UE","Matière","Note","Coef","Total","Moyenne Groupe","Rang","Mention","Session","Crédits Obtenus"]
  for(i=0; i<thvalue.length; i++){
    var th=document.createElement('th')
    th.setAttribute("scope", "col")
    th.innerHTML=thvalue[i]
    tr1.appendChild(th)
  }
  var thead1=document.createElement('thead')
  thead1.appendChild(tr1)
  //tbody
  //Line 2
  var th1 =document.createElement('th')
  th1.setAttribute('id','semestre')
  th1.setAttribute('rowspan','9')
  th1.innerHTML=`SEMESTRE 1`
  var th2=document.createElement('th')
  th2.setAttribute('scope','row')
  th2.setAttribute('rowspan','3')
  th2.innerHTML=`UE Fondamentales`
  var td1=document.createElement('td')
  td1.setAttribute('id','MDS111-codeue')
  td1.innerHTML=`MDS111`
  var td2=document.createElement('td')
  td2.setAttribute('id', 'MDS111-matiere')
  td2.innerHTML=`Mathématiques I`
  var td3=document.createElement('td')
  td3.setAttribute('id','MDS111-note')
  
  var td4=document.createElement('td')
  td4.setAttribute('id','MDS111-coef')

  var td5=document.createElement('td')
  td5.setAttribute('id','MDS111-total')

  var td6=document.createElement('td')
  td6.setAttribute('id','MDS111-moyenne')
  td6.setAttribute('rowspan','3')

  var td7=document.createElement('td')
  td7.setAttribute('id','MDS111-rang')
  
  var td8=document.createElement('td')
  td8.setAttribute('id','MDS111-mention')

  var td9=document.createElement('td')
  td9.setAttribute('id','MDS111-session')

  var td10=document.createElement('td')
  td10.setAttribute('id','MDS111-credits')

  var tr2=document.createElement('tr')
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
  var td1=document.createElement('td')
  td1.setAttribute('id','MDS111-codeue')
  td1.innerHTML=`MDS111`
  var td2=document.createElement('td')
  td2.setAttribute('id', 'MDS111-matiere')
  td2.innerHTML=`Informatique I`
  var td3=document.createElement('td')
  td3.setAttribute('id','MDS111-note')
  
  var td4=document.createElement('td')
  td4.setAttribute('id','MDS111-coef')

  var td5=document.createElement('td')
  td5.setAttribute('id','MDS111-total')

  var td6=document.createElement('td')
  td6.setAttribute('id','MDS111-rang')

  var td7=document.createElement('td')
  td7.setAttribute('id','MDS111-mention')
  
  var td8=document.createElement('td')
  td8.setAttribute('id','MDS111-session')

  var td9=document.createElement('td')
  td9.setAttribute('id','MDS111-credits')

  var tr3=document.createElement('tr')
  tr3.appendChild(td1)
  tr3.appendChild(td2)
  tr3.appendChild(td3)
  tr3.appendChild(td4)
  tr3.appendChild(td5)
  tr3.appendChild(td6)
  tr3.appendChild(td7)
  tr3.appendChild(td8)
  tr3.appendChild(td9)

  //Line 33
  var td11=document.createElement('td')
  td11.setAttribute('id','MDS112-codeue')
  td11.innerHTML=`MDS112`
  
  var td12=document.createElement('td')
  td12.setAttribute('id','MDS112-matiere')
  td12.innerHTML=`Techniques Quantitatives de Gestion I`

  var td13=document.createElement('td')
  td13.setAttribute('id','MDS112-note')

  var td14=document.createElement('td')
  td14.setAttribute('id','MDS112-coef')

  var td15=document.createElement('td')
  td15.setAttribute('id','MDS112-total')

  /*var td166=document.createElement('td')
  td166.setAttribute('id','MDS112-moyenne')*/

  var td16=document.createElement('td')
  td16.setAttribute('id','MDS112-rang')

  var td17=document.createElement('td')
  td17.setAttribute('id','MDS112-mention')

  var td18=document.createElement('td')
  td18.setAttribute('id','MDS112-session')

  var td19=document.createElement('td')
  td19.setAttribute('id','MDS112-credits')

  var tr33=document.createElement('tr')
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
  
  //Line 4 //REGROUPER L4 et L5 dans une boucle
  var th2=document.createElement('th')
  th2.setAttribute('scope','row')
  th2.setAttribute('rowspan','4')
  th2.innerHTML=`UE Professionnelles`

  var td20=document.createElement('td')
  td20.setAttribute("id","MDS113-codeue")
  td20.innerHTML=`MDS113`

  var td21=document.createElement('td')
  td21.setAttribute("id","MDS113-matiere")
  td21.innerHTML=`Environnement Jurique Et Comptable I`

  var td22=document.createElement('td')
  td22.setAttribute("id","MDS113-note")

  var td222=document.createElement('td')
  td222.setAttribute("id","MDS113-coef")

  var td23=document.createElement('td')
  td23.setAttribute("id","MDS113-total")

  var td24=document.createElement('td')
  td24.setAttribute("rowspan","4")
  td24.setAttribute("id","MDS113-moyenne")

  var td25=document.createElement('td')
  td25.setAttribute("id","MDS113-rang")

  var td26=document.createElement('td')
  td26.setAttribute("id","MDS113-mention")

  var td27=document.createElement('td')
  td27.setAttribute("id","MDS113-session")

  var td28=document.createElement('td')
  td28.setAttribute("id","MDS113-credits")

  var tr4=document.createElement('tr')
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
  var td28=document.createElement('td')
  td28.setAttribute("id","MDS114-codeue")
  td28.innerHTML=`MDS114`

  var td29=document.createElement('td')
  td29.setAttribute("id","MDS114-matiere")
  td29.innerHTML=`Marketing`

  var td30=document.createElement('td')
  td30.setAttribute("id","MDS114-note")

  var td31=document.createElement('td')
  td31.setAttribute("id","MDS114-coef")

  var td32=document.createElement('td')
  td32.setAttribute("id","MDS114-total")

  var td33=document.createElement('td')
  td33.setAttribute("id","MDS114-rang")

  var td34=document.createElement('td')
  td34.setAttribute("id","MDS114-mention")

  var td35=document.createElement('td')
  td35.setAttribute("id","MDS114-session")

  var td36=document.createElement('td')
  td36.setAttribute("id","MDS114-credits")

  var tr5=document.createElement('tr')
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
  var td377=document.createElement('td')
  td377.setAttribute("id","MDS115-codeue")
  td377.innerHTML=`MDS115`

  var td37=document.createElement('td')
  td37.setAttribute("id","MDS115-matiere")
  td37.innerHTML=`Outils De Gestion Du Sport I`

  var td38=document.createElement('td')
  td38.setAttribute("id","MDS115-note")

  var td39=document.createElement('td')
  td39.setAttribute("id","MDS115-coef")

  var td40=document.createElement('td')
  td40.setAttribute("id","MDS115-total")

  var td41=document.createElement('td')
  td41.setAttribute("id","MDS115-rang")

  var td42=document.createElement('td')
  td42.setAttribute("id","MDS115-mention")

  var td43=document.createElement('td')
  td43.setAttribute("id","MDS115-session")

  var td44=document.createElement('td')
  td44.setAttribute("id","MDS115-credits")

  var tr6=document.createElement('tr')
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
  var td45=document.createElement('td')
  td45.setAttribute("id","MDS116-codeue")
  td45.innerHTML=`MDS116`

  var td46=document.createElement('td')
  td46.setAttribute("id","MDS116-matiere")
  td46.innerHTML=`Gestion Des Structures Et organisation Sportives I`

  var td47=document.createElement('td')
  td47.setAttribute("id","MDS116-note")

  var td48=document.createElement('td')
  td48.setAttribute("id","MDS116-coef")

  var td49=document.createElement('td')
  td49.setAttribute("id","MDS116-total")

  var td50=document.createElement('td')
  td50.setAttribute("id","MDS116-rang")

  var td51=document.createElement('td')
  td51.setAttribute("id","MDS116-mention")

  var td52=document.createElement('td')
  td52.setAttribute("id","MDS116-session")

  var td53=document.createElement('td')
  td53.setAttribute("id","MDS116-credits")

  var tr7=document.createElement('tr')
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
  var th3=document.createElement('th')
  th3.setAttribute('scope','row')
  //th3.setAttribute('rowspan','3')
  th3.innerHTML=`UE Transversales`

  var td54=document.createElement('td')
  td54.setAttribute("id","MDS117-codeue")
  td54.innerHTML=`MDS117`

  var td56=document.createElement('td')
  td56.setAttribute("id","MDS117-matiere")
  td56.innerHTML=`Formation Bilingue I et Environnement`

  var td57=document.createElement('td')
  td57.setAttribute("id","MDS117-note")

  var td58=document.createElement('td')
  td58.setAttribute("id","MDS117-coef")

  var td59=document.createElement('td')
  td59.setAttribute("id","MDS117-total")

  var td60=document.createElement('td')
  //td60.setAttribute("rowspan","3")
  td60.setAttribute("id","MDS117-moyenne")

  var td61=document.createElement('td')
  td61.setAttribute("id","MDS117-rang")

  var td62=document.createElement('td')
  td62.setAttribute("id","MDS117-mention")

  var td63=document.createElement('td')
  td63.setAttribute("id","MDS117-session")

  var td64=document.createElement('td')
  td64.setAttribute("id","MDS117-credits")

  var tr8=document.createElement('tr')
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
  var tr9=document.createElement('tr')
  for(i=0; i<=6; i++){
    var td=document.createElement('td')
    if(i==0){td.innerHTML=`RESULTATS SEMESTRE 1`; td.setAttribute('colspan','4')}
    if(i==1){td.setAttribute('id','resultat-coef')}
    if(i==2){td.setAttribute('id','resultat-total')}
    if(i==3){td.setAttribute('id','resultat-moyenne')}
    if(i==4){td.setAttribute('id','resultat-rang')}
    if(i==5){td.setAttribute('id','resultat'); td.setAttribute('colspan','2'); td.innerHTML=`Total Crédits Semestre 1`}
    if(i==6){td.setAttribute('id','resultat-crédits')}

    tr9.appendChild(td)
  }
  
  //tbody
  var tbody=document.createElement('tbody')
  tbody.setAttribute('id','tbody00')
  tbody.appendChild(tr2)
  tbody.appendChild(tr3)
  tbody.appendChild(tr33)
  tbody.appendChild(tr4)
  tbody.appendChild(tr5)
  tbody.appendChild(tr6)
  tbody.appendChild(tr7)
  tbody.appendChild(tr8)
  tbody.appendChild(tr9)

  var table1=document.createElement('table')
  table1.setAttribute('class', 'table-1')
  table1.appendChild(thead1)
  table1.appendChild(tbody)

  //table3
  //thead2
  var tr12=document.createElement('tr')
  for(i=0; i<=11; i++){
    var th=document.createElement('th')
    th.setAttribute('scope','col')
    if(i==0){th.innerHTML=`&nbsp;&nbsp;`}
    tr12.appendChild(th)
  }
  var thead2=document.createElement('thead')
  thead2.appendChild(tr12)

  //tbody
  //Line 1
  var tr13=document.createElement('tr')
  for(i=0; i<=8; i++){
    var td=document.createElement('td')
    if(i==1){td.setAttribute('colspan','3'); td.innerHTML=`Moyenne de Classe de l'étudiant :`}
    if(i==2){td.innerHTML=`/ 20`}
    if(i==3){td.setAttribute('colspan','2'); td.innerHTML=`Maximum :`}
    if(i==7){td.innerHTML=`Retard :`}

    tr13.appendChild(td)
  }
  //Line 2
  var tr14=document.createElement('tr')
  for(i=0; i<=8; i++){
    var td=document.createElement('td')
    if(i==1){td.setAttribute('colspan','3'); td.innerHTML=`Moyenne Générale de la classe :`}
    if(i==2){td.innerHTML=`/ 20`}
    if(i==3){td.setAttribute('colspan','2'); td.innerHTML=`Minimum :`}
    if(i==7){td.innerHTML=`Absences:`}

    tr14.appendChild(td)
  }
  //Line 3
  var tr15=document.createElement('tr')
  for(i=0; i<=8; i++){
    var td=document.createElement('td')
    if(i==1){td.setAttribute('colspan','3'); /*td.innerHTML=`Moyenne Générale de la classe :`*/}
    //if(i==3){/*td.innerHTML=`/ 20`*/}
    if(i==4){td.setAttribute('colspan','2'); td.innerHTML=`Rang :`}
    //if(i==8){td.innerHTML=`Absences:`}
    if(i==5){td.innerHTML=` sur `}

    tr15.appendChild(td)
  }
  //Line 4

  //TABLEAU 3
  var tbody3=document.createElement('tbody')
  tbody3.setAttribute('id', 'tbody-3')
  tbody3.appendChild(tr13)
  tbody3.appendChild(tr14)
  tbody3.appendChild(tr15)

  var table3=document.createElement('table')
  table3.setAttribute('id','table-3')
  table3.appendChild(thead2)
  table3.appendChild(tbody3)

  //semester Result
  var semestreResult=document.createElement('div')
  semestreResult.setAttribute('id','semester-result')
  semestreResult.appendChild(table1)
  semestreResult.appendChild(table3)

  //Main
  var main=document.createElement('main')
  main.appendChild(bullchecktitle)
  main.appendChild(infostudent)
  main.appendChild(semestreResult)

  //Footer
  var visa=document.createElement('div')
  visa.setAttribute('class','visa')
  visa.innerHTML="VISA CHEF ETABLISSEMENT"

  var footer=document.createElement('footer')
  footer.appendChild(visa)

  //TEST
  containerbull=document.createElement('div')
  containerbull.setAttribute('class','container-bull')
  containerbull.appendChild(header)
  containerbull.appendChild(hr)
  containerbull.appendChild(main)
  containerbull.appendChild(footer)

  //Retour Du composant Bulletin
  return(containerbull)
}
/*DECLARATION S1 STAPS*/
function GenerateBullStaps1Semestre1(){
  var br = document.createElement('br')
  var slogan=document.createElement('div')
  slogan.innerHTML=`Au-delà de la limite`
  slogan.setAttribute('class','slogan')

  var titleinfo=document.createElement('div')
  titleinfo.innerHTML=`BP : 7403 Yaoundé  Tél : (237) 695 548 821 / 653 764 050 <br> Site Web : www.institutfrançoisembango.com Email : isep_fm@yahoo.com`
  titleinfo.setAttribute('class', 'title-info')
  
  var title=document.createElement('div')
  title.setAttribute("id", "title")
  title.appendChild(slogan)
  title.appendChild(titleinfo)

  //Logo
  var headleft=document.createElement('div')
  headleft.setAttribute('id', 'head-left')
  
  var image=document.createElement('img')
  image.setAttribute("src",`/static/bulletin/image/logo.jpeg`)
  image.setAttribute("alt","logo")

  var logo=document.createElement('div')
  logo.setAttribute("id","logo")
  logo.appendChild(image)

  var headright=document.createElement('div')
  headright.setAttribute('id','head-right')

  var containertitle=document.createElement('div')
  containertitle.appendChild(headleft)
  containertitle.appendChild(logo)
  containertitle.appendChild(headright)

  var logoTitle=document.createElement('div')
  logoTitle.setAttribute('id','logo-title')
  logoTitle.appendChild(containertitle)
  logoTitle.appendChild(title)

  var header=document.createElement('header')
  header.appendChild(logoTitle)
  
  var body = document.getElementsByTagName('body')
  body[0].appendChild(header)

  var hr=document.createElement('hr')

  //MAIN
  var bullcheck=document.createElement('div')
  bullcheck.setAttribute('id','bull-check')
  bullcheck.innerHTML=`DAF/SER/DFF/FFFF/FFFF`

  var bulltitle=document.createElement('div')
  bulltitle.setAttribute('id','bull-title')
  bulltitle.innerHTML=`BULLETIN DE NOTES SEMESTRE 1`

  var bullchecktitle=document.createElement('div')
  bullchecktitle.setAttribute('id','bull-check-title')
  bullchecktitle.appendChild(bullcheck)
  bullchecktitle.appendChild(bulltitle)

  //info student
  var info1=document.createElement('div')
  info1.setAttribute('class','info-student-style')
  info1.innerHTML=`Filière &nbsp;&nbsp; : STAPS`
  var info2=document.createElement('div')
  info2.setAttribute('class','info-student-style')
  info2.innerHTML=`Spécialité &nbsp;:  EPS`
  var info3=document.createElement('div')
  info3.setAttribute('class','info-student-style')
  info3.innerHTML=`Nom (s) &nbsp; &nbsp; : `
  var info4=document.createElement('div')
  info4.setAttribute('class','info-student-style')
  info4.innerHTML=`Prénom (s) : `
  var info5=document.createElement('div')
  info5.setAttribute('class','info-student-style')
  info5.innerHTML=`Nationalité : Camerounais(e)`

  var infostudent1=document.createElement('div')
  infostudent1.setAttribute('id','info-student-1')
  infostudent1.appendChild(info1)
  infostudent1.appendChild(info2)
  infostudent1.appendChild(info3)
  infostudent1.appendChild(info4)
  infostudent1.appendChild(info5)
  
  var info11=document.createElement('div')
  info11.setAttribute('class','info-student-style')
  info11.innerHTML=`Grade : BTS  `
  var info22=document.createElement('div')
  info22.setAttribute('class','info-student-style')
  info22.innerHTML=`Matricule : `
  var info33=document.createElement('div')
  info33.setAttribute('class','info-student-style')
  info33.innerHTML=`Date De Naissance : `
  var info44=document.createElement('div')
  info44.setAttribute('class','info-student-style')
  info44.innerHTML=`Lieu De Naissance : `
  var info55=document.createElement('div')
  info55.setAttribute('class','info-student-style')
  info55.innerHTML=`Année Académique : `

  var infostudent2=document.createElement('div')
  infostudent2.setAttribute('id','info-student-2')
  infostudent2.appendChild(info11)
  infostudent2.appendChild(info22)
  infostudent2.appendChild(info33)
  infostudent2.appendChild(info44)
  infostudent2.appendChild(info55)

  var info111=document.createElement('div')
  info111.innerHTML=`Niveau: I`

  var infostudent3=document.createElement('div')
  infostudent3.setAttribute('id','info-student-3')
  infostudent3.appendChild(info111)

  var infostudent=document.createElement('div')
  infostudent.setAttribute('id','info-student')
  infostudent.appendChild(infostudent1)
  infostudent.appendChild(infostudent2)
  infostudent.appendChild(infostudent3)

  
  //table1
  //thead -Line 1
  var tr1=document.createElement('tr')
  var thvalue=["","Groupe UE","Code UE","Matière","Note","Coef","Total","Moyenne Groupe","Rang","Mention","Session","Crédits Obtenus"]
  for(i=0; i<thvalue.length; i++){
    var th=document.createElement('th')
    th.setAttribute("scope", "col")
    th.innerHTML=thvalue[i]
    tr1.appendChild(th)
  }
  var thead1=document.createElement('thead')
  thead1.appendChild(tr1)
  //tbody
  //Line 2
  var th1 =document.createElement('th')
  th1.setAttribute('id','semestre')
  th1.setAttribute('rowspan','10')
  th1.innerHTML=`SEMESTRE 1`
  var th2=document.createElement('th')
  th2.setAttribute('scope','row')
  th2.setAttribute('rowspan','2')
  th2.innerHTML=`UE Fondamentales`
  var td1=document.createElement('td')
  td1.setAttribute('id','EPS111-codeue')
  td1.innerHTML=`EPS111`
  var td2=document.createElement('td')
  td2.setAttribute('id', 'EPS111-matiere')
  td2.innerHTML=`Histoire et principes de base de l'éducation Physique`
  var td3=document.createElement('td')
  td3.setAttribute('id','EPS111-note')
  
  var td4=document.createElement('td')
  td4.setAttribute('id','EPS111-coef')

  var td5=document.createElement('td')
  td5.setAttribute('id','EPS111-total')

  var td6=document.createElement('td')
  td6.setAttribute('id','EPS111-moyenne')
  td6.setAttribute('rowspan','2')

  var td7=document.createElement('td')
  td7.setAttribute('id','EPS111-rang')
  
  var td8=document.createElement('td')
  td8.setAttribute('id','EPS111-mention')

  var td9=document.createElement('td')
  td9.setAttribute('id','EPS111-session')

  var td10=document.createElement('td')
  td10.setAttribute('id','EPS111-credits')

  var tr2=document.createElement('tr')
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
  var td11=document.createElement('td')
  td11.setAttribute('id','EPS112-codeue')
  td11.innerHTML=`EPS112`
  
  var td12=document.createElement('td')
  td12.setAttribute('id','EPS112-matiere')
  td12.innerHTML=`Psychologie du Sport-Sociologie du Sport`

  var td13=document.createElement('td')
  td13.setAttribute('id','EPS112-note')

  var td14=document.createElement('td')
  td14.setAttribute('id','EPS112-coef')

  var td15=document.createElement('td')
  td15.setAttribute('id','EPS112-total')

  var td16=document.createElement('td')
  td16.setAttribute('id','EPS112-rang')

  var td17=document.createElement('td')
  td17.setAttribute('id','EPS112-mention')

  var td18=document.createElement('td')
  td18.setAttribute('id','EPS112-session')

  var td19=document.createElement('td')
  td19.setAttribute('id','EPS112-credits')

  var tr3=document.createElement('tr')
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
  var th2=document.createElement('th')
  th2.setAttribute('scope','row')
  th2.setAttribute('rowspan','4')
  th2.innerHTML=`UE Professionnelles`

  var td20=document.createElement('td')
  td20.setAttribute("id","EPS113-codeue")
  td20.innerHTML=`EPS113`

  var td21=document.createElement('td')
  td21.setAttribute("id","EPS113-matiere")
  td21.innerHTML=`Didactique De l'EPS I`

  var td22=document.createElement('td')
  td22.setAttribute("id","EPS113-note")

  var td222=document.createElement('td')
  td222.setAttribute("id","EPS113-coef")

  var td23=document.createElement('td')
  td23.setAttribute("id","EPS113-total")

  var td24=document.createElement('td')
  td24.setAttribute("rowspan","4")
  td24.setAttribute("id","EPS113-moyenne")

  var td25=document.createElement('td')
  td25.setAttribute("id","EPS113-rang")

  var td26=document.createElement('td')
  td26.setAttribute("id","EPS113-mention")

  var td27=document.createElement('td')
  td27.setAttribute("id","EPS113-session")

  var td28=document.createElement('td')
  td28.setAttribute("id","EPS113-credits")

  var tr4=document.createElement('tr')
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
  var td28=document.createElement('td')
  td28.setAttribute("id","EPS114-codeue")
  td28.innerHTML=`EPS114`

  var td29=document.createElement('td')
  td29.setAttribute("id","EPS114-matiere")
  td29.innerHTML=`Anatomie I`

  var td30=document.createElement('td')
  td30.setAttribute("id","EPS114-note")

  var td31=document.createElement('td')
  td31.setAttribute("id","EPS114-coef")

  var td32=document.createElement('td')
  td32.setAttribute("id","EPS114-total")

  var td33=document.createElement('td')
  td33.setAttribute("id","EPS114-rang")

  var td34=document.createElement('td')
  td34.setAttribute("id","EPS114-mention")

  var td35=document.createElement('td')
  td35.setAttribute("id","EPS114-session")

  var td36=document.createElement('td')
  td36.setAttribute("id","EPS114-credits")

  var tr5=document.createElement('tr')
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
  var td377=document.createElement('td')
  td377.setAttribute("id","EPS115-codeue")
  td377.innerHTML=`EPS115`

  var td37=document.createElement('td')
  td37.setAttribute("id","EPS115-matiere")
  td37.innerHTML=`Didactique des APS ( Sports collectifs)`

  var td38=document.createElement('td')
  td38.setAttribute("id","EPS115-note")

  var td39=document.createElement('td')
  td39.setAttribute("id","EPS115-coef")

  var td40=document.createElement('td')
  td40.setAttribute("id","EPS115-total")

  var td41=document.createElement('td')
  td41.setAttribute("id","EPS115-rang")

  var td42=document.createElement('td')
  td42.setAttribute("id","EPS115-mention")

  var td43=document.createElement('td')
  td43.setAttribute("id","EPS115-session")

  var td44=document.createElement('td')
  td44.setAttribute("id","EPS115-credits")

  var tr6=document.createElement('tr')
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
  var td45=document.createElement('td')
  td45.setAttribute("id","EPS116-codeue")
  td45.innerHTML=`EPS116`

  var td46=document.createElement('td')
  td46.setAttribute("id","EPS116-matiere")
  td46.innerHTML=`La Physiologie de l’Execice I`

  var td47=document.createElement('td')
  td47.setAttribute("id","EPS116-note")

  var td48=document.createElement('td')
  td48.setAttribute("id","EPS116-coef")

  var td49=document.createElement('td')
  td49.setAttribute("id","EPS116-total")

  var td50=document.createElement('td')
  td50.setAttribute("id","EPS116-rang")

  var td51=document.createElement('td')
  td51.setAttribute("id","EPS116-mention")

  var td52=document.createElement('td')
  td52.setAttribute("id","EPS116-session")

  var td53=document.createElement('td')
  td53.setAttribute("id","EPS116-credits")

  var tr7=document.createElement('tr')
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
  var th3=document.createElement('th')
  th3.setAttribute('scope','row')
  th3.setAttribute('rowspan','3')
  th3.innerHTML=`UE Transversales`

  var td54=document.createElement('td')
  td54.setAttribute("id","EPS117-codeue")
  td54.innerHTML=`EPS117`

  var td56=document.createElement('td')
  td56.setAttribute("id","EPS117-matiere")
  td56.innerHTML=`Informatique`

  var td57=document.createElement('td')
  td57.setAttribute("id","EPS117-note")

  var td58=document.createElement('td')
  td58.setAttribute("id","EPS117-coef")

  var td59=document.createElement('td')
  td59.setAttribute("id","EPS117-total")

  var td60=document.createElement('td')
  td60.setAttribute("rowspan","3")
  td60.setAttribute("id","EPS117-moyenne")

  var td61=document.createElement('td')
  td61.setAttribute("id","EPS117-rang")

  var td62=document.createElement('td')
  td62.setAttribute("id","EPS117-mention")

  var td63=document.createElement('td')
  td63.setAttribute("id","EPS117-session")

  var td64=document.createElement('td')
  td64.setAttribute("id","EPS117-credits")

  var tr8=document.createElement('tr')
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
  var td45=document.createElement('td')
  td45.setAttribute("id","EPS118-codeue")
  td45.innerHTML=`EPS118`

  var td46=document.createElement('td')
  td46.setAttribute("id","EPS118-matiere")
  td46.innerHTML=`La Physiologie de l’Execice I`

  var td47=document.createElement('td')
  td47.setAttribute("id","EPS118-note")

  var td48=document.createElement('td')
  td48.setAttribute("id","EPS118-coef")

  var td49=document.createElement('td')
  td49.setAttribute("id","EPS118-total")

  var td50=document.createElement('td')
  td50.setAttribute("id","EPS118-rang")

  var td51=document.createElement('td')
  td51.setAttribute("id","EPS118-mention")

  var td52=document.createElement('td')
  td52.setAttribute("id","EPS118-session")

  var td53=document.createElement('td')
  td53.setAttribute("id","EPS118-credits")

  var tr9=document.createElement('tr')
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
  var td45=document.createElement('td')
  td45.setAttribute("id","EPS119-codeue")
  td45.innerHTML=`EPS119`

  var td46=document.createElement('td')
  td46.setAttribute("id","EPS119-matiere")
  td46.innerHTML=`Technique D'Expression Anglaise. Anglaise- Forbi`

  var td47=document.createElement('td')
  td47.setAttribute("id","EPS119-note")

  var td48=document.createElement('td')
  td48.setAttribute("id","EPS119-coef")

  var td49=document.createElement('td')
  td49.setAttribute("id","EPS119-total")

  var td50=document.createElement('td')
  td50.setAttribute("id","EPS119-rang")

  var td51=document.createElement('td')
  td51.setAttribute("id","EPS119-mention")

  var td52=document.createElement('td')
  td52.setAttribute("id","EPS119-session")

  var td53=document.createElement('td')
  td53.setAttribute("id","EPS119-credits")

  var tr10=document.createElement('tr')
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
  var td100=document.createElement('td')
  td100.setAttribute('colspan','4')
  td100.innerHTML=`RESULTATS SEMESTRE 1`

  var td101=document.createElement('td')
  td101.setAttribute("id","resultat-coef")
  
  var td102=document.createElement('td')
  td102.setAttribute("id","resultat-total")
  
  var td103=document.createElement('td')
  td103.setAttribute("id","resultat-moyenne")
  
  var td104=document.createElement('td')
  td104.setAttribute("id","resultat-rang")
  
  var td105=document.createElement('td')
  td105.setAttribute("colspan","2")
  td105.setAttribute("id","resultat")
  td105.innerHTML=`Total Crédits Semestre 1`
  
  var td106=document.createElement('td')
  td106.setAttribute("id","resultat-crédits")

  var tr11=document.createElement('tr')
  tr11.appendChild(td100)
  tr11.appendChild(td101)
  tr11.appendChild(td102)
  tr11.appendChild(td103)
  tr11.appendChild(td104)
  tr11.appendChild(td105)
  tr11.appendChild(td106)

  //tbody
  var tbody=document.createElement('tbody')
  tbody.appendChild(tr2)
  tbody.appendChild(tr3)
  tbody.appendChild(tr4)
  tbody.appendChild(tr5)
  tbody.appendChild(tr6)
  tbody.appendChild(tr7)
  tbody.appendChild(tr8)
  tbody.appendChild(tr9)
  tbody.appendChild(tr10)
  tbody.appendChild(tr11)

  var table1=document.createElement('table')
  table1.setAttribute('class', 'table-1')
  table1.appendChild(thead1)
  table1.appendChild(tbody)

  //table3
  //thead2
  var tr12=document.createElement('tr')
  for(i=0; i<=11; i++){
    var th=document.createElement('th')
    th.setAttribute('scope','col')
    if(i==0){th.innerHTML=`&nbsp;&nbsp;`}
    tr12.appendChild(th)
  }
  var thead2=document.createElement('thead')
  thead2.appendChild(tr12)

  //tbody
  //Line 1
  var tr13=document.createElement('tr')
  for(i=0; i<=8; i++){
    var td=document.createElement('td')
    if(i==1){td.setAttribute('colspan','3'); td.innerHTML=`Moyenne de Classe de l'étudiant :`}
    if(i==2){td.innerHTML=`/ 20`}
    if(i==3){td.setAttribute('colspan','2'); td.innerHTML=`Maximum :`}
    if(i==7){td.innerHTML=`Retard :`}

    tr13.appendChild(td)
  }
  //Line 2
  var tr14=document.createElement('tr')
  for(i=0; i<=8; i++){
    var td=document.createElement('td')
    if(i==1){td.setAttribute('colspan','3'); td.innerHTML=`Moyenne Générale de la classe :`}
    if(i==2){td.innerHTML=`/ 20`}
    if(i==3){td.setAttribute('colspan','2'); td.innerHTML=`Minimum :`}
    if(i==7){td.innerHTML=`Absences:`}

    tr14.appendChild(td)
  }
  //Line 3
  var tr15=document.createElement('tr')
  for(i=0; i<=8; i++){
    var td=document.createElement('td')
    if(i==1){td.setAttribute('colspan','3');}
    if(i==4){td.setAttribute('colspan','2'); td.innerHTML=`Rang :`}
    if(i==5){td.innerHTML=` sur `}

    tr15.appendChild(td)
  }
  //Line 4
  var tbody3=document.createElement('tbody')
  tbody3.setAttribute('id', 'tbody-3')
  tbody3.appendChild(tr13)
  tbody3.appendChild(tr14)
  tbody3.appendChild(tr15)

  var table3=document.createElement('table')
  table3.setAttribute('id','table-3')
  table3.appendChild(thead2)
  table3.appendChild(tbody3)

  //semester Result
  var semestreResult=document.createElement('div')
  semestreResult.setAttribute('id','semester-result')
  semestreResult.appendChild(table1)
  semestreResult.appendChild(table3)

  //Main
  var main=document.createElement('main')
  main.appendChild(bullchecktitle)
  main.appendChild(infostudent)
  main.appendChild(semestreResult)

  //Footer
  var visa=document.createElement('div')
  visa.setAttribute('class','visa')
  visa.innerHTML="VISA CHEF ETABLISSEMENT"

  var footer=document.createElement('footer')
  footer.appendChild(visa)

  //TEST
  containerbull=document.createElement('div')
  containerbull.setAttribute('class','container-bull')
  containerbull.appendChild(header)
  containerbull.appendChild(hr)
  containerbull.appendChild(main)
  containerbull.appendChild(footer)

  //TEST
  return(containerbull)
}
/*DECLARATION S3 STAPS*/
function GenerateBullStaps2Semestre3(){
  //title
  var br = document.createElement('br')
  var slogan=document.createElement('div')
  slogan.innerHTML=`Au-delà de la limite`
  slogan.setAttribute('class','slogan')

  var titleinfo=document.createElement('div')
  titleinfo.innerHTML=`BP : 7403 Yaoundé  Tél : (237) 695 548 821 / 653 764 050 <br> Site Web : www.institutfrançoisembango.com Email : isep_fm@yahoo.com`
  titleinfo.setAttribute('class', 'title-info')
  
  var title=document.createElement('div')
  title.setAttribute("id", "title")
  title.appendChild(slogan)
  title.appendChild(titleinfo)

  //Logo
  var headleft=document.createElement('div')
  headleft.setAttribute('id', 'head-left')
  
  var image=document.createElement('img')
  image.setAttribute("src",`/static/bulletin/image/logo.jpeg`)
  image.setAttribute("alt","logo")

  var logo=document.createElement('div')
  logo.setAttribute("id","logo")
  logo.appendChild(image)

  var headright=document.createElement('div')
  headright.setAttribute('id','head-right')

  var containertitle=document.createElement('div')
  containertitle.appendChild(headleft)
  containertitle.appendChild(logo)
  containertitle.appendChild(headright)

  var logoTitle=document.createElement('div')
  logoTitle.setAttribute('id','logo-title')
  logoTitle.appendChild(containertitle)
  logoTitle.appendChild(title)

  var header=document.createElement('header')
  header.appendChild(logoTitle)
  
  var body = document.getElementsByTagName('body')
  body[0].appendChild(header)

  var hr=document.createElement('hr')

  var bullcheck=document.createElement('div')
  bullcheck.setAttribute('id','bull-check')
  bullcheck.innerHTML=`DAF/SER/DFF/FFFF/FFFF`

  var bulltitle=document.createElement('div')
  bulltitle.setAttribute('id','bull-title')
  bulltitle.innerHTML=`BULLETIN DE NOTES SEMESTRE 3`

  var bullchecktitle=document.createElement('div')
  bullchecktitle.setAttribute('id','bull-check-title')
  bullchecktitle.appendChild(bullcheck)
  bullchecktitle.appendChild(bulltitle)

  //info student
  var info1=document.createElement('div')
  info1.setAttribute('class','info-student-style')
  info1.innerHTML=`Filière &nbsp;&nbsp; : STAPS`
  var info2=document.createElement('div')
  info2.setAttribute('class','info-student-style')
  info2.innerHTML=`Spécialité &nbsp;:  EPS`
  var info3=document.createElement('div')
  info3.setAttribute('class','info-student-style')
  info3.innerHTML=`Nom (s) &nbsp; &nbsp; : `
  var info4=document.createElement('div')
  info4.setAttribute('class','info-student-style')
  info4.innerHTML=`Prénom (s) : `
  var info5=document.createElement('div')
  info5.setAttribute('class','info-student-style')
  info5.innerHTML=`Nationalité : Camerounais(e)`

  var infostudent1=document.createElement('div')
  infostudent1.setAttribute('id','info-student-1')
  infostudent1.appendChild(info1)
  infostudent1.appendChild(info2)
  infostudent1.appendChild(info3)
  infostudent1.appendChild(info4)
  infostudent1.appendChild(info5)
  
  var info11=document.createElement('div')
  info11.setAttribute('class','info-student-style')
  info11.innerHTML=`Grade : BTS  `
  var info22=document.createElement('div')
  info22.setAttribute('class','info-student-style')
  info22.innerHTML=`Matricule : `
  var info33=document.createElement('div')
  info33.setAttribute('class','info-student-style')
  info33.innerHTML=`Date De Naissance : `
  var info44=document.createElement('div')
  info44.setAttribute('class','info-student-style')
  info44.innerHTML=`Lieu De Naissance : `
  var info55=document.createElement('div')
  info55.setAttribute('class','info-student-style')
  info55.innerHTML=`Année Académique : `

  var infostudent2=document.createElement('div')
  infostudent2.setAttribute('id','info-student-2')
  infostudent2.appendChild(info11)
  infostudent2.appendChild(info22)
  infostudent2.appendChild(info33)
  infostudent2.appendChild(info44)
  infostudent2.appendChild(info55)

  var info111=document.createElement('div')
  info111.innerHTML=`Niveau: II`

  var infostudent3=document.createElement('div')
  infostudent3.setAttribute('id','info-student-3')
  infostudent3.appendChild(info111)

  var infostudent=document.createElement('div')
  infostudent.setAttribute('id','info-student')
  infostudent.appendChild(infostudent1)
  infostudent.appendChild(infostudent2)
  infostudent.appendChild(infostudent3)

  //table1
  //thead -Line 1
  var tr1=document.createElement('tr')
  var thvalue=["","Groupe UE","Code UE","Matière","Note","Coef","Total","Moyenne Groupe","Rang","Mention","Session","Crédits Obtenus"]
  for(i=0; i<thvalue.length; i++){
    var th=document.createElement('th')
    th.setAttribute("scope", "col")
    th.innerHTML=thvalue[i]
    tr1.appendChild(th)
  }
  var thead1=document.createElement('thead')
  thead1.appendChild(tr1)
  //tbody
  //Line 2
  var th1 =document.createElement('th')
  th1.setAttribute('id','semestre')
  th1.setAttribute('rowspan','10')
  th1.innerHTML=`SEMESTRE 3`
  var th2=document.createElement('th')
  th2.setAttribute('scope','row')
  th2.setAttribute('rowspan','2')
  th2.innerHTML=`UE Fondamentales`
  var td1=document.createElement('td')
  td1.setAttribute('id','EPS231-codeue')
  td1.innerHTML=`EPS231`
  var td2=document.createElement('td')
  td2.setAttribute('id', 'EPS231-matiere')
  td2.innerHTML=`Education Physique : Loisirs`
  var td3=document.createElement('td')
  td3.setAttribute('id','EPS231-note')
  
  var td4=document.createElement('td')
  td4.setAttribute('id','EPS231-coef')

  var td5=document.createElement('td')
  td5.setAttribute('id','EPS231-total')

  var td6=document.createElement('td')
  td6.setAttribute('id','EPS231-moyenne')
  td6.setAttribute('rowspan','2')

  var td7=document.createElement('td')
  td7.setAttribute('id','EPS231-rang')
  
  var td8=document.createElement('td')
  td8.setAttribute('id','EPS231-mention')

  var td9=document.createElement('td')
  td9.setAttribute('id','EPS231-session')

  var td10=document.createElement('td')
  td10.setAttribute('id','EPS231-credits')

  var tr2=document.createElement('tr')
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
  var td11=document.createElement('td')
  td11.setAttribute('id','EPS231-codeue')
  td11.innerHTML=`EPS232`
  
  var td12=document.createElement('td')
  td12.setAttribute('id','EPS232-matiere')
  td12.innerHTML=`Eléments de Psychopédagogie`

  var td13=document.createElement('td')
  td13.setAttribute('id','EPS232-note')

  var td14=document.createElement('td')
  td14.setAttribute('id','EPS232-coef')

  var td15=document.createElement('td')
  td15.setAttribute('id','EPS232-total')

  var td16=document.createElement('td')
  td16.setAttribute('id','EPS232-rang')

  var td17=document.createElement('td')
  td17.setAttribute('id','EPS232-mention')

  var td18=document.createElement('td')
  td18.setAttribute('id','EPS232-session')

  var td19=document.createElement('td')
  td19.setAttribute('id','EPS232-credits')

  var tr3=document.createElement('tr')
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
  var th2=document.createElement('th')
  th2.setAttribute('scope','row')
  th2.setAttribute('rowspan','4')
  th2.innerHTML=`UE Professionnelles`

  var td20=document.createElement('td')
  td20.setAttribute("id","EPS233-codeue")
  td20.innerHTML=`EPS233`

  var td21=document.createElement('td')
  td21.setAttribute("id","EPS233-matiere")
  td21.innerHTML=`Didactique De l'EPS III`

  var td22=document.createElement('td')
  td22.setAttribute("id","EPS233-note")

  var td222=document.createElement('td')
  td222.setAttribute("id","EPS233-coef")

  var td23=document.createElement('td')
  td23.setAttribute("id","EPS233-total")

  var td24=document.createElement('td')
  td24.setAttribute("rowspan","4")
  td24.setAttribute("id","EPS233-moyenne")

  var td25=document.createElement('td')
  td25.setAttribute("id","EPS233-rang")

  var td26=document.createElement('td')
  td26.setAttribute("id","EPS233-mention")

  var td27=document.createElement('td')
  td27.setAttribute("id","EPS233-session")

  var td28=document.createElement('td')
  td28.setAttribute("id","EPS233-credits")

  var tr4=document.createElement('tr')
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
  var td28=document.createElement('td')
  td28.setAttribute("id","EPS234-codeue")
  td28.innerHTML=`EPS234`

  var td29=document.createElement('td')
  td29.setAttribute("id","EPS234-matiere")
  td29.innerHTML=`La Physiologie de L'Exercice II`

  var td30=document.createElement('td')
  td30.setAttribute("id","EPS234-note")

  var td31=document.createElement('td')
  td31.setAttribute("id","EPS234-coef")

  var td32=document.createElement('td')
  td32.setAttribute("id","EPS234-total")

  var td33=document.createElement('td')
  td33.setAttribute("id","EPS234-rang")

  var td34=document.createElement('td')
  td34.setAttribute("id","EPS234-mention")

  var td35=document.createElement('td')
  td35.setAttribute("id","EPS234-session")

  var td36=document.createElement('td')
  td36.setAttribute("id","EPS234-credits")

  var tr5=document.createElement('tr')
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
  var td377=document.createElement('td')
  td377.setAttribute("id","EPS235-codeue")
  td377.innerHTML=`EPS235`

  var td37=document.createElement('td')
  td37.setAttribute("id","EPS235-matiere")
  td37.innerHTML=`Didactique Des APS (Gymnastique/Athlethisme/Activités Physiques et Sportives Adaptées)`

  var td38=document.createElement('td')
  td38.setAttribute("id","EPS235-note")

  var td39=document.createElement('td')
  td39.setAttribute("id","EPS235-coef")

  var td40=document.createElement('td')
  td40.setAttribute("id","EPS235-total")

  var td41=document.createElement('td')
  td41.setAttribute("id","EPS235-rang")

  var td42=document.createElement('td')
  td42.setAttribute("id","EPS235-mention")

  var td43=document.createElement('td')
  td43.setAttribute("id","EPS235-session")

  var td44=document.createElement('td')
  td44.setAttribute("id","EPS235-credits")

  var tr6=document.createElement('tr')
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
  var td45=document.createElement('td')
  td45.setAttribute("id","EPS236-codeue")
  td45.innerHTML=`EPS236`

  var td46=document.createElement('td')
  td46.setAttribute("id","EPS236-matiere")
  td46.innerHTML=`Pédagogie Pratique II (Sport Co-sport de ombat-Sport Individuel Gymnastique)`

  var td47=document.createElement('td')
  td47.setAttribute("id","EPS236-note")

  var td48=document.createElement('td')
  td48.setAttribute("id","EPS236-coef")

  var td49=document.createElement('td')
  td49.setAttribute("id","EPS236-total")

  var td50=document.createElement('td')
  td50.setAttribute("id","EPS236-rang")

  var td51=document.createElement('td')
  td51.setAttribute("id","EPS236-mention")

  var td52=document.createElement('td')
  td52.setAttribute("id","EPS236-session")

  var td53=document.createElement('td')
  td53.setAttribute("id","EPS236-credits")

  var tr7=document.createElement('tr')
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
  var th3=document.createElement('th')
  th3.setAttribute('scope','row')
  th3.setAttribute('rowspan','3')
  th3.innerHTML=`UE Transversales`

  var td54=document.createElement('td')
  td54.setAttribute("id","EPS237-codeue")
  td54.innerHTML=`EPS237`

  var td56=document.createElement('td')
  td56.setAttribute("id","EPS237-matiere")
  td56.innerHTML=`Formation Bilingue -Anglais appliqué au APS`

  var td57=document.createElement('td')
  td57.setAttribute("id","EPS237-note")

  var td58=document.createElement('td')
  td58.setAttribute("id","EPS237-coef")

  var td59=document.createElement('td')
  td59.setAttribute("id","EPS237-total")

  var td60=document.createElement('td')
  td60.setAttribute("rowspan","3")
  td60.setAttribute("id","EPS237-moyenne")

  var td61=document.createElement('td')
  td61.setAttribute("id","EPS237-rang")

  var td62=document.createElement('td')
  td62.setAttribute("id","EPS237-mention")

  var td63=document.createElement('td')
  td63.setAttribute("id","EPS237-session")

  var td64=document.createElement('td')
  td64.setAttribute("id","EPS237-credits")

  var tr8=document.createElement('tr')
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
  var td45=document.createElement('td')
  td45.setAttribute("id","EPS238-codeue")
  td45.innerHTML=`EPS238`

  var td46=document.createElement('td')
  td46.setAttribute("id","EPS238-matiere")
  td46.innerHTML=`Technique D'Expression Française`

  var td47=document.createElement('td')
  td47.setAttribute("id","EPS238-note")

  var td48=document.createElement('td')
  td48.setAttribute("id","EPS238-coef")

  var td49=document.createElement('td')
  td49.setAttribute("id","EPS238-total")

  var td50=document.createElement('td')
  td50.setAttribute("id","EPS238-rang")

  var td51=document.createElement('td')
  td51.setAttribute("id","EPS238-mention")

  var td52=document.createElement('td')
  td52.setAttribute("id","EPS238-session")

  var td53=document.createElement('td')
  td53.setAttribute("id","EPS238-credits")

  var tr9=document.createElement('tr')
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
  var td45=document.createElement('td')
  td45.setAttribute("id","EPS239-codeue")
  td45.innerHTML=`EPS239`

  var td46=document.createElement('td')
  td46.setAttribute("id","EPS239-matiere")
  td46.innerHTML=`Informatique`

  var td47=document.createElement('td')
  td47.setAttribute("id","EPS239-note")

  var td48=document.createElement('td')
  td48.setAttribute("id","EPS239-coef")

  var td49=document.createElement('td')
  td49.setAttribute("id","EPS239-total")

  var td50=document.createElement('td')
  td50.setAttribute("id","EPS239-rang")

  var td51=document.createElement('td')
  td51.setAttribute("id","EPS239-mention")

  var td52=document.createElement('td')
  td52.setAttribute("id","EPS239-session")

  var td53=document.createElement('td')
  td53.setAttribute("id","EPS239-credits")

  var tr10=document.createElement('tr')
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
  var td100=document.createElement('td')
  td100.setAttribute('colspan','4')
  td100.innerHTML=`RESULTATS SEMESTRE 1`

  var td101=document.createElement('td')
  td101.setAttribute("id","resultat-coef")
  
  var td102=document.createElement('td')
  td102.setAttribute("id","resultat-total")
  
  var td103=document.createElement('td')
  td103.setAttribute("id","resultat-moyenne")
  
  var td104=document.createElement('td')
  td104.setAttribute("id","resultat-rang")
  
  var td105=document.createElement('td')
  td105.setAttribute("colspan","2")
  td105.setAttribute("id","resultat")
  td105.innerHTML=`Total Crédits Semestre 1`
  
  var td106=document.createElement('td')
  td106.setAttribute("id","resultat-crédits")

  var tr11=document.createElement('tr')
  tr11.appendChild(td100)
  tr11.appendChild(td101)
  tr11.appendChild(td102)
  tr11.appendChild(td103)
  tr11.appendChild(td104)
  tr11.appendChild(td105)
  tr11.appendChild(td106)

  //tbody
  var tbody=document.createElement('tbody')
  tbody.appendChild(tr2)
  tbody.appendChild(tr3)
  tbody.appendChild(tr4)
  tbody.appendChild(tr5)
  tbody.appendChild(tr6)
  tbody.appendChild(tr7)
  tbody.appendChild(tr8)
  tbody.appendChild(tr9)
  tbody.appendChild(tr10)
  tbody.appendChild(tr11)

  table1 = document.createElement('table')
  table1.setAttribute('class', 'table-1')
  table1.appendChild(thead1)
  table1.appendChild(tbody)

  //table3
  //thead2
  var tr12=document.createElement('tr')
  for(i=0; i<=11; i++){
    var th=document.createElement('th')
    th.setAttribute('scope','col')
    if(i==0){th.innerHTML=`&nbsp;&nbsp;`}
    tr12.appendChild(th)
  }
  var thead2=document.createElement('thead')
  thead2.appendChild(tr12)

  //tbody
  //Line 1
  var tr13=document.createElement('tr')
  for(i=0; i<=8; i++){
    var td=document.createElement('td')
    if(i==1){td.setAttribute('colspan','3'); td.innerHTML=`Moyenne de Classe de l'étudiant :`}
    if(i==2){td.innerHTML=`/ 20`}
    if(i==3){td.setAttribute('colspan','2'); td.innerHTML=`Maximum :`}
    if(i==7){td.innerHTML=`Retard :`}

    tr13.appendChild(td)
  }
  //Line 2
  var tr14=document.createElement('tr')
  for(i=0; i<=8; i++){
    var td=document.createElement('td')
    if(i==1){td.setAttribute('colspan','3'); td.innerHTML=`Moyenne Générale de la classe :`}
    if(i==2){td.innerHTML=`/ 20`}
    if(i==3){td.setAttribute('colspan','2'); td.innerHTML=`Minimum :`}
    if(i==7){td.innerHTML=`Absences:`}

    tr14.appendChild(td)
  }
  //Line 3
  var tr15=document.createElement('tr')
  for(i=0; i<=8; i++){
    var td=document.createElement('td')
    if(i==1){td.setAttribute('colspan','3'); }
    
    if(i==4){td.setAttribute('colspan','2'); td.innerHTML=`Rang :`}
    //if(i==8){td.innerHTML=`Absences:`}
    if(i==5){td.innerHTML=` sur `}

    tr15.appendChild(td)
  }
  //Line 4


  var tbody3=document.createElement('tbody')
  tbody3.setAttribute('id', 'tbody-3')
  tbody3.appendChild(tr13)
  tbody3.appendChild(tr14)
  tbody3.appendChild(tr15)

  var table3=document.createElement('table')
  table3.setAttribute('id','table-3')
  table3.appendChild(thead2)
  table3.appendChild(tbody3)

  //semester Result
  var semestreResult=document.createElement('div')
  semestreResult.setAttribute('id','semester-result')
  semestreResult.appendChild(table1)
  semestreResult.appendChild(table3)

  //Main
  var main=document.createElement('main')
  main.appendChild(bullchecktitle)
  main.appendChild(infostudent)
  main.appendChild(semestreResult)

  //Footer
  var visa=document.createElement('div')
  visa.setAttribute('class','visa')
  visa.innerHTML="VISA CHEF ETABLISSEMENT"

  var footer=document.createElement('footer')
  footer.appendChild(visa)

  //TEST
  containerbull=document.createElement('div')
  containerbull.setAttribute('class','container-bull')
  containerbull.appendChild(header)
  containerbull.appendChild(hr)
  containerbull.appendChild(main)
  containerbull.appendChild(footer)

  //TEST
  /*body=document.getElementsByTagName('body')
  body[0].appendChild(containerbull)*/
    return (containerbull)
  }
/*DECLARATION SEMESTRE 5 EVE */
function GenerateBullEVEsemestre5(){
  var br = document.createElement('br')
  var slogan=document.createElement('div')
  slogan.innerHTML=`Au-delà de la limite`
  slogan.setAttribute('class','slogan')

  var titleinfo=document.createElement('div')
  titleinfo.innerHTML=`BP : 7403 Yaoundé  Tél : (237) 695 548 821 / 653 764 050 <br> Site Web : www.institutfrançoisembango.com Email : isep_fm@yahoo.com`
  titleinfo.setAttribute('class', 'title-info')
  
  var title=document.createElement('div')
  title.setAttribute("id", "title")
  title.appendChild(slogan)
  title.appendChild(titleinfo)

  //Logo
  var headleft=document.createElement('div')
  headleft.setAttribute('id', 'head-left')
  
  var image=document.createElement('img')
  image.setAttribute("src",`/static/bulletin/image/logo.jpeg`)
  image.setAttribute("alt","logo")

  var logo=document.createElement('div')
  logo.setAttribute("id","logo")
  logo.appendChild(image)

  var headright=document.createElement('div')
  headright.setAttribute('id','head-right')

  var containertitle=document.createElement('div')
  containertitle.appendChild(headleft)
  containertitle.appendChild(logo)
  containertitle.appendChild(headright)

  var logoTitle=document.createElement('div')
  logoTitle.setAttribute('id','logo-title')
  logoTitle.appendChild(containertitle)
  logoTitle.appendChild(title)

  var header=document.createElement('header')
  header.appendChild(logoTitle)
  
  body = document.getElementsByTagName('body')
  body[0].appendChild(header)

  var hr=document.createElement('hr')

  var bullcheck=document.createElement('div')
  bullcheck.setAttribute('id','bull-check')
  bullcheck.innerHTML=`DAF/SER/DFF/FFFF/FFFF`

  var bulltitle=document.createElement('div')
  bulltitle.setAttribute('id','bull-title')
  bulltitle.innerHTML=`BULLETIN DE NOTES SEMESTRE 5`

  var bullchecktitle=document.createElement('div')
  bullchecktitle.setAttribute('id','bull-check-title')
  bullchecktitle.appendChild(bullcheck)
  bullchecktitle.appendChild(bulltitle)

  //info student
  var info1=document.createElement('div')
  info1.setAttribute('class','info-student-style')
  info1.innerHTML=`Filière &nbsp;&nbsp; : MAS`
  var info2=document.createElement('div')
  info2.setAttribute('class','info-student-style')
  info2.innerHTML=`Spécialité &nbsp;:  EVE`
  var info3=document.createElement('div')
  info3.setAttribute('class','info-student-style')
  info3.innerHTML=`Nom (s) &nbsp; &nbsp; : `
  var info4=document.createElement('div')
  info4.setAttribute('class','info-student-style')
  info4.innerHTML=`Prénom (s) : `
  var info5=document.createElement('div')
  info5.setAttribute('class','info-student-style')
  info5.innerHTML=`Nationalité : Camerounais(e)`

  var infostudent1=document.createElement('div')
  infostudent1.setAttribute('id','info-student-1')
  infostudent1.appendChild(info1)
  infostudent1.appendChild(info2)
  infostudent1.appendChild(info3)
  infostudent1.appendChild(info4)
  infostudent1.appendChild(info5)
  
  var info11=document.createElement('div')
  info11.setAttribute('class','info-student-style')
  info11.innerHTML=`Grade : LICENCE `
  var info22=document.createElement('div')
  info22.setAttribute('class','info-student-style')
  info22.innerHTML=`Matricule : `
  var info33=document.createElement('div')
  info33.setAttribute('class','info-student-style')
  info33.innerHTML=`Date De Naissance : `
  var info44=document.createElement('div')
  info44.setAttribute('class','info-student-style')
  info44.innerHTML=`Lieu De Naissance : `
  var info55=document.createElement('div')
  info55.setAttribute('class','info-student-style')
  info55.innerHTML=`Année Académique : `

  var infostudent2=document.createElement('div')
  infostudent2.setAttribute('id','info-student-2')
  infostudent2.appendChild(info11)
  infostudent2.appendChild(info22)
  infostudent2.appendChild(info33)
  infostudent2.appendChild(info44)
  infostudent2.appendChild(info55)

  var info111=document.createElement('div')
  info111.innerHTML=`Niveau: III`

  var infostudent3=document.createElement('div')
  infostudent3.setAttribute('id','info-student-3')
  infostudent3.appendChild(info111)

  var infostudent=document.createElement('div')
  infostudent.setAttribute('id','info-student')
  infostudent.appendChild(infostudent1)
  infostudent.appendChild(infostudent2)
  infostudent.appendChild(infostudent3)

  //table1
  //thead -Line 1
  var tr1=document.createElement('tr')
  var thvalue=["","Groupe UE","Code UE","Matière","Note","Coef","Total","Moyenne Groupe","Rang","Mention","Session","Crédits Obtenus"]
  for(i=0; i<thvalue.length; i++){
    var th=document.createElement('th')
    th.setAttribute("scope", "col")
    th.innerHTML=thvalue[i]
    tr1.appendChild(th)
  }
  var thead1=document.createElement('thead')
  thead1.appendChild(tr1)
  //tbody
  //Line 2
  var th1 =document.createElement('th')
  th1.setAttribute('id','semestre')
  th1.setAttribute('rowspan','7')
  th1.innerHTML=`SEMESTRE 5`
  var th2=document.createElement('th')
  th2.setAttribute('scope','row')
  th2.setAttribute('rowspan','4')
  th2.innerHTML=`UE Fondamentales`
  var td1=document.createElement('td')
  td1.setAttribute('id','MAS315-codeue')
  td1.innerHTML=`MAS315`
  var td2=document.createElement('td')
  td2.setAttribute('id', 'MAS315-matiere')
  td2.innerHTML=`Environnement Institutionnel De la pratique du Sport`
  var td3=document.createElement('td')
  td3.setAttribute('id','MAS315-note')
  
  var td4=document.createElement('td')
  td4.setAttribute('id','MAS315-coef')

  var td5=document.createElement('td')
  td5.setAttribute('id','MAS315-total')

  var td6=document.createElement('td')
  td6.setAttribute('id','MAS315-moyenne')
  td6.setAttribute('rowspan','4')

  var td7=document.createElement('td')
  td7.setAttribute('id','MAS315-rang')
  
  var td8=document.createElement('td')
  td8.setAttribute('id','MAS315-mention')

  var td9=document.createElement('td')
  td9.setAttribute('id','MAS315-session')

  var td10=document.createElement('td')
  td10.setAttribute('id','MAS315-credits')

  var tr2=document.createElement('tr')
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
  var td11=document.createElement('td')
  td11.setAttribute('id','MAS325-codeue')
  td11.innerHTML=`MAS325`
  
  var td12=document.createElement('td')
  td12.setAttribute('id','MAS325-matiere')
  td12.innerHTML=`Montage Des Projets Et Entrepreneuriat Sportif`

  var td13=document.createElement('td')
  td13.setAttribute('id','MAS325-note')

  var td14=document.createElement('td')
  td14.setAttribute('id','MAS325-coef')

  var td15=document.createElement('td')
  td15.setAttribute('id','MAS325-total')

  var td16=document.createElement('td')
  td16.setAttribute('id','MAS325-rang')

  var td17=document.createElement('td')
  td17.setAttribute('id','MAS325-mention')

  var td18=document.createElement('td')
  td18.setAttribute('id','MAS325-session')

  var td19=document.createElement('td')
  td19.setAttribute('id','EPS325-credits')

  var tr3=document.createElement('tr')
  tr3.appendChild(td11)
  tr3.appendChild(td12)
  tr3.appendChild(td13)
  tr3.appendChild(td14)
  tr3.appendChild(td15)
  tr3.appendChild(td16)
  tr3.appendChild(td17)
  tr3.appendChild(td18)
  tr3.appendChild(td19)
  
  var td20=document.createElement('td')
  td20.setAttribute("id","MAS335-codeue")
  td20.innerHTML=`MAS335`

  var td21=document.createElement('td')
  td21.setAttribute("id","MAS335-matiere")
  td21.innerHTML=`Information Et Communication Stratégiques dans le Sport et les Loisirs`

  var td22=document.createElement('td')
  td22.setAttribute("id","MAS335-note")

  var td222=document.createElement('td')
  td222.setAttribute("id","MAS335-coef")

  var td23=document.createElement('td')
  td23.setAttribute("id","MAS335-total")

  var td25=document.createElement('td')
  td25.setAttribute("id","MAS335-rang")

  var td26=document.createElement('td')
  td26.setAttribute("id","MAS335-mention")

  var td27=document.createElement('td')
  td27.setAttribute("id","MAS335-session")

  var td28=document.createElement('td')
  td28.setAttribute("id","MAS335-credits")

  var tr4=document.createElement('tr')
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
  var td28=document.createElement('td')
  td28.setAttribute("id","MAS345-codeue")
  td28.innerHTML=`MAS345`

  var td29=document.createElement('td')
  td29.setAttribute("id","MAS345-matiere")
  td29.innerHTML=`E-sport`

  var td30=document.createElement('td')
  td30.setAttribute("id","MAS345-note")

  var td31=document.createElement('td')
  td31.setAttribute("id","MAS345-coef")

  var td32=document.createElement('td')
  td32.setAttribute("id","MAS345-total")

  var td33=document.createElement('td')
  td33.setAttribute("id","MAS345-rang")

  var td34=document.createElement('td')
  td34.setAttribute("id","MAS345-mention")

  var td35=document.createElement('td')
  td35.setAttribute("id","MAS345-session")

  var td36=document.createElement('td')
  td36.setAttribute("id","MAS345-credits")

  var tr5=document.createElement('tr')
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
  var th3=document.createElement('th')
  th3.setAttribute('scope','row')
  th3.setAttribute('rowspan','2')
  th3.innerHTML=`UE Spécialité`

  var td54=document.createElement('td')
  td54.setAttribute("id","EVE355-codeue")
  td54.innerHTML=`EVE355`

  var td56=document.createElement('td')
  td56.setAttribute("id","EVE355-matiere")
  td56.innerHTML=`Multimédias dans le Développement Du Sport et Des Loisirs`

  var td57=document.createElement('td')
  td57.setAttribute("id","EVE355-note")

  var td58=document.createElement('td')
  td58.setAttribute("id","EVE355-coef")

  var td59=document.createElement('td')
  td59.setAttribute("id","EVE355-total")

  var td60=document.createElement('td')
  td60.setAttribute("rowspan","2")
  td60.setAttribute("id","EVE355-moyenne")

  var td61=document.createElement('td')
  td61.setAttribute("id","EVE355-rang")

  var td62=document.createElement('td')
  td62.setAttribute("id","EVE355-mention")

  var td63=document.createElement('td')
  td63.setAttribute("id","EVE355-session")

  var td64=document.createElement('td')
  td64.setAttribute("id","EVE355-credits")

  var tr8=document.createElement('tr')
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
  var td45=document.createElement('td')
  td45.setAttribute("id","EVE365-codeue")
  td45.innerHTML=`EVE365`

  var td46=document.createElement('td')
  td46.setAttribute("id","EVE365-matiere")
  td46.innerHTML=`Ingénierie De L'Animation Sportive Et Culturelle`

  var td47=document.createElement('td')
  td47.setAttribute("id","EVE365-note")

  var td48=document.createElement('td')
  td48.setAttribute("id","EVE365-coef")

  var td49=document.createElement('td')
  td49.setAttribute("id","EVE365-total")

  var td50=document.createElement('td')
  td50.setAttribute("id","EVE365-rang")

  var td51=document.createElement('td')
  td51.setAttribute("id","EVE365-mention")

  var td52=document.createElement('td')
  td52.setAttribute("id","EVE365-session")

  var td53=document.createElement('td')
  td53.setAttribute("id","EVE365-credits")

  var tr9=document.createElement('tr')
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
  var td100=document.createElement('td')
  td100.setAttribute('colspan','4')
  td100.innerHTML=`RESULTATS SEMESTRE 1`

  var td101=document.createElement('td')
  td101.setAttribute("id","resultat-coef")
  
  var td102=document.createElement('td')
  td102.setAttribute("id","resultat-total")
  
  var td103=document.createElement('td')
  td103.setAttribute("id","resultat-moyenne")
  
  var td104=document.createElement('td')
  td104.setAttribute("id","resultat-rang")
  
  var td105=document.createElement('td')
  td105.setAttribute("colspan","2")
  td105.setAttribute("id","resultat")
  td105.innerHTML=`Total Crédits Semestre 1`
  
  var td106=document.createElement('td')
  td106.setAttribute("id","resultat-crédits")

  var tr11=document.createElement('tr')
  tr11.appendChild(td100)
  tr11.appendChild(td101)
  tr11.appendChild(td102)
  tr11.appendChild(td103)
  tr11.appendChild(td104)
  tr11.appendChild(td105)
  tr11.appendChild(td106)

  //tbody
  var tbody=document.createElement('tbody')
  tbody.setAttribute('id','tbody01')
  tbody.appendChild(tr2)
  tbody.appendChild(tr3)
  tbody.appendChild(tr4)
  tbody.appendChild(tr5)
  tbody.appendChild(tr8)
  tbody.appendChild(tr9)
  tbody.appendChild(tr11)

  var table1=document.createElement('table')
  table1.setAttribute('class', 'table-1')
  table1.appendChild(thead1)
  table1.appendChild(tbody)

  //table3
  //thead2
  var tr12=document.createElement('tr')
  for(i=0; i<=11; i++){
    var th=document.createElement('th')
    th.setAttribute('scope','col')
    if(i==0){th.innerHTML=`&nbsp;&nbsp;`}
    tr12.appendChild(th)
  }
  var thead2=document.createElement('thead')
  thead2.appendChild(tr12)

  //tbody
  //Line 1
  var tr13=document.createElement('tr')
  for(i=0; i<=8; i++){
    var td=document.createElement('td')
    if(i==1){td.setAttribute('colspan','3'); td.innerHTML=`Moyenne de Classe de l'étudiant :`}
    if(i==2){td.innerHTML=`/ 20`}
    if(i==3){td.setAttribute('colspan','2'); td.innerHTML=`Maximum :`}
    if(i==7){td.innerHTML=`Retard :`}

    tr13.appendChild(td)
  }
  //Line 2
  var tr14=document.createElement('tr')
  for(i=0; i<=8; i++){
    var td=document.createElement('td')
    if(i==1){td.setAttribute('colspan','3'); td.innerHTML=`Moyenne Générale de la classe :`}
    if(i==2){td.innerHTML=`/ 20`}
    if(i==3){td.setAttribute('colspan','2'); td.innerHTML=`Minimum :`}
    if(i==7){td.innerHTML=`Absences:`}

    tr14.appendChild(td)
  }
  //Line 3
  var tr15=document.createElement('tr')
  for(i=0; i<=8; i++){
    var td=document.createElement('td')
    if(i==1){td.setAttribute('colspan','3');}
    if(i==4){td.setAttribute('colspan','2'); td.innerHTML=`Rang :`}
    if(i==5){td.innerHTML=` sur `}

    tr15.appendChild(td)
  }
  //Line 4
  var tbody3=document.createElement('tbody')
  tbody3.setAttribute('id', 'tbody-3')
  tbody3.appendChild(tr13)
  tbody3.appendChild(tr14)
  tbody3.appendChild(tr15)

  var table3=document.createElement('table')
  table3.setAttribute('id','table-3')
  table3.appendChild(thead2)
  table3.appendChild(tbody3)

  var semestreResult=document.createElement('div')
  semestreResult.setAttribute('id','semester-result')
  semestreResult.appendChild(table1)
  semestreResult.appendChild(table3)

  var main=document.createElement('main')
  main.appendChild(bullchecktitle)
  main.appendChild(infostudent)
  main.appendChild(semestreResult)

  var visa=document.createElement('div')
  visa.setAttribute('class','visa')
  visa.innerHTML="VISA CHEF ETABLISSEMENT"

  var footer=document.createElement('footer')
  footer.appendChild(visa)

  containerbull=document.createElement('div')
  containerbull.setAttribute('class','container-bull')
  containerbull.appendChild(header)
  containerbull.appendChild(hr)
  containerbull.appendChild(main)
  containerbull.appendChild(footer)

  /*body=document.getElementsByTagName('body')
  body[0].appendChild(containerbull)*/
  return(containerbull)
}
/*DECLARATION GENERATION SEEMESTRE 5 MSO */
function GenerateBullMSOsemestre5(){
  var br = document.createElement('br')
  var slogan=document.createElement('div')
  slogan.innerHTML=`Au-delà de la limite`
  slogan.setAttribute('class','slogan')

  var titleinfo=document.createElement('div')
  titleinfo.innerHTML=`BP : 7403 Yaoundé  Tél : (237) 695 548 821 / 653 764 050 <br> Site Web : www.institutfrançoisembango.com Email : isep_fm@yahoo.com`
  titleinfo.setAttribute('class', 'title-info')
  
  var title=document.createElement('div')
  title.setAttribute("id", "title")
  title.appendChild(slogan)
  title.appendChild(titleinfo)

  //Logo
  var headleft=document.createElement('div')
  headleft.setAttribute('id', 'head-left')
  
  var image=document.createElement('img')
  image.setAttribute("src",`/static/bulletin/image/logo.jpeg`)
  image.setAttribute("alt","logo")

  var logo=document.createElement('div')
  logo.setAttribute("id","logo")
  logo.appendChild(image)

  var headright=document.createElement('div')
  headright.setAttribute('id','head-right')

  var containertitle=document.createElement('div')
  containertitle.appendChild(headleft)
  containertitle.appendChild(logo)
  containertitle.appendChild(headright)

  var logoTitle=document.createElement('div')
  logoTitle.setAttribute('id','logo-title')
  logoTitle.appendChild(containertitle)
  logoTitle.appendChild(title)

  var header=document.createElement('header')
  header.appendChild(logoTitle)
  
  body = document.getElementsByTagName('body')
  body[0].appendChild(header)

  var hr=document.createElement('hr')
  
  var bullcheck=document.createElement('div')
  bullcheck.setAttribute('id','bull-check')
  bullcheck.innerHTML=`DAF/SER/DFF/FFFF/FFFF`

  var bulltitle=document.createElement('div')
  bulltitle.setAttribute('id','bull-title')
  bulltitle.innerHTML=`BULLETIN DE NOTES SEMESTRE 5`

  var bullchecktitle=document.createElement('div')
  bullchecktitle.setAttribute('id','bull-check-title')
  bullchecktitle.appendChild(bullcheck)
  bullchecktitle.appendChild(bulltitle)

  //info student
  var info1=document.createElement('div')
  info1.setAttribute('class','info-student-style')
  info1.innerHTML=`Filière &nbsp;&nbsp; : MAS`
  var info2=document.createElement('div')
  info2.setAttribute('class','info-student-style')
  info2.innerHTML=`Spécialité &nbsp;:  MSO`
  var info3=document.createElement('div')
  info3.setAttribute('class','info-student-style')
  info3.innerHTML=`Nom (s) &nbsp; &nbsp; : `
  var info4=document.createElement('div')
  info4.setAttribute('class','info-student-style')
  info4.innerHTML=`Prénom (s) : `
  var info5=document.createElement('div')
  info5.setAttribute('class','info-student-style')
  info5.innerHTML=`Nationalité : Camerounais(e)`

  var infostudent1=document.createElement('div')
  infostudent1.setAttribute('id','info-student-1')
  infostudent1.appendChild(info1)
  infostudent1.appendChild(info2)
  infostudent1.appendChild(info3)
  infostudent1.appendChild(info4)
  infostudent1.appendChild(info5)
  
  var info11=document.createElement('div')
  info11.setAttribute('class','info-student-style')
  info11.innerHTML=`Grade : LICENCE `
  var info22=document.createElement('div')
  info22.setAttribute('class','info-student-style')
  info22.innerHTML=`Matricule : `
  var info33=document.createElement('div')
  info33.setAttribute('class','info-student-style')
  info33.innerHTML=`Date De Naissance : `
  var info44=document.createElement('div')
  info44.setAttribute('class','info-student-style')
  info44.innerHTML=`Lieu De Naissance : `
  var info55=document.createElement('div')
  info55.setAttribute('class','info-student-style')
  info55.innerHTML=`Année Académique : `

  var infostudent2=document.createElement('div')
  infostudent2.setAttribute('id','info-student-2')
  infostudent2.appendChild(info11)
  infostudent2.appendChild(info22)
  infostudent2.appendChild(info33)
  infostudent2.appendChild(info44)
  infostudent2.appendChild(info55)

  var info111=document.createElement('div')
  info111.innerHTML=`Niveau: III`

  var infostudent3=document.createElement('div')
  infostudent3.setAttribute('id','info-student-3')
  infostudent3.appendChild(info111)

  var infostudent=document.createElement('div')
  infostudent.setAttribute('id','info-student')
  infostudent.appendChild(infostudent1)
  infostudent.appendChild(infostudent2)
  infostudent.appendChild(infostudent3)

  //table1
  //thead -Line 1
  var tr1=document.createElement('tr')
  var thvalue=["","Groupe UE","Code UE","Matière","Note","Coef","Total","Moyenne Groupe","Rang","Mention","Session","Crédits Obtenus"]
  for(i=0; i<thvalue.length; i++){
    var th=document.createElement('th')
    th.setAttribute("scope", "col")
    th.innerHTML=thvalue[i]
    tr1.appendChild(th)
  }
  var thead1=document.createElement('thead')
  thead1.appendChild(tr1)
  //tbody
  //Line 2
  var th1 =document.createElement('th')
  th1.setAttribute('id','semestre')
  th1.setAttribute('rowspan','7')
  th1.innerHTML=`SEMESTRE 5`
  var th2=document.createElement('th')
  th2.setAttribute('scope','row')
  th2.setAttribute('rowspan','4')
  th2.innerHTML=`UE Fondamentales`
  var td1=document.createElement('td')
  td1.setAttribute('id','MAS315-codeue')
  td1.innerHTML=`MAS315`
  var td2=document.createElement('td')
  td2.setAttribute('id', 'MAS315-matiere')
  td2.innerHTML=`Environnement Institutionnel De la pratique du Sport`
  var td3=document.createElement('td')
  td3.setAttribute('id','MAS315-note')
  
  var td4=document.createElement('td')
  td4.setAttribute('id','MAS315-coef')

  var td5=document.createElement('td')
  td5.setAttribute('id','MAS315-total')

  var td6=document.createElement('td')
  td6.setAttribute('id','MAS315-moyenne')
  td6.setAttribute('rowspan','4')

  var td7=document.createElement('td')
  td7.setAttribute('id','MAS315-rang')
  
  var td8=document.createElement('td')
  td8.setAttribute('id','MAS315-mention')

  var td9=document.createElement('td')
  td9.setAttribute('id','MAS315-session')

  var td10=document.createElement('td')
  td10.setAttribute('id','MAS315-credits')

  var tr2=document.createElement('tr')
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
  var td11=document.createElement('td')
  td11.setAttribute('id','MAS325-codeue')
  td11.innerHTML=`MAS325`
  
  var td12=document.createElement('td')
  td12.setAttribute('id','MAS325-matiere')
  td12.innerHTML=`Montage Des Projets Et Entrepreneuriat Sportif`

  var td13=document.createElement('td')
  td13.setAttribute('id','MAS325-note')

  var td14=document.createElement('td')
  td14.setAttribute('id','MAS325-coef')

  var td15=document.createElement('td')
  td15.setAttribute('id','MAS325-total')

  var td16=document.createElement('td')
  td16.setAttribute('id','MAS325-rang')

  var td17=document.createElement('td')
  td17.setAttribute('id','MAS325-mention')

  var td18=document.createElement('td')
  td18.setAttribute('id','MAS325-session')

  var td19=document.createElement('td')
  td19.setAttribute('id','EPS325-credits')

  var tr3=document.createElement('tr')
  tr3.appendChild(td11)
  tr3.appendChild(td12)
  tr3.appendChild(td13)
  tr3.appendChild(td14)
  tr3.appendChild(td15)
  tr3.appendChild(td16)
  tr3.appendChild(td17)
  tr3.appendChild(td18)
  tr3.appendChild(td19)
  
  var td20=document.createElement('td')
  td20.setAttribute("id","MAS335-codeue")
  td20.innerHTML=`MAS335`

  var td21=document.createElement('td')
  td21.setAttribute("id","MAS335-matiere")
  td21.innerHTML=`Information Et Communication Stratégiques dans le Sport et les Loisirs`

  var td22=document.createElement('td')
  td22.setAttribute("id","MAS335-note")

  var td222=document.createElement('td')
  td222.setAttribute("id","MAS335-coef")

  var td23=document.createElement('td')
  td23.setAttribute("id","MAS335-total")

  var td25=document.createElement('td')
  td25.setAttribute("id","MAS335-rang")

  var td26=document.createElement('td')
  td26.setAttribute("id","MAS335-mention")

  var td27=document.createElement('td')
  td27.setAttribute("id","MAS335-session")

  var td28=document.createElement('td')
  td28.setAttribute("id","MAS335-credits")

  var tr4=document.createElement('tr')
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
  var td28=document.createElement('td')
  td28.setAttribute("id","MAS345-codeue")
  td28.innerHTML=`MAS345`

  var td29=document.createElement('td')
  td29.setAttribute("id","MAS345-matiere")
  td29.innerHTML=`E-sport`

  var td30=document.createElement('td')
  td30.setAttribute("id","MAS345-note")

  var td31=document.createElement('td')
  td31.setAttribute("id","MAS345-coef")

  var td32=document.createElement('td')
  td32.setAttribute("id","MAS345-total")

  var td33=document.createElement('td')
  td33.setAttribute("id","MAS345-rang")

  var td34=document.createElement('td')
  td34.setAttribute("id","MAS345-mention")

  var td35=document.createElement('td')
  td35.setAttribute("id","MAS345-session")

  var td36=document.createElement('td')
  td36.setAttribute("id","MAS345-credits")

  var tr5=document.createElement('tr')
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
  var th3=document.createElement('th')
  th3.setAttribute('scope','row')
  th3.setAttribute('rowspan','2')
  th3.innerHTML=`UE Spécialité`

  var td54=document.createElement('td')
  td54.setAttribute("id","MSO355-codeue")
  td54.innerHTML=`MSO355`

  var td56=document.createElement('td')
  td56.setAttribute("id","MSO355-matiere")
  td56.innerHTML=`Ethique Sportive Et Programmes Olympiques`

  var td57=document.createElement('td')
  td57.setAttribute("id","MSO355-note")

  var td58=document.createElement('td')
  td58.setAttribute("id","MSO355-coef")

  var td59=document.createElement('td')
  td59.setAttribute("id","MSO355-total")

  var td60=document.createElement('td')
  td60.setAttribute("rowspan","2")
  td60.setAttribute("id","MSO355-moyenne")

  var td61=document.createElement('td')
  td61.setAttribute("id","MSO355-rang")

  var td62=document.createElement('td')
  td62.setAttribute("id","MSO355-mention")

  var td63=document.createElement('td')
  td63.setAttribute("id","MSO355-session")

  var td64=document.createElement('td')
  td64.setAttribute("id","MSO355-credits")

  var tr8=document.createElement('tr')
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
  var td45=document.createElement('td')
  td45.setAttribute("id","MSO365-codeue")
  td45.innerHTML=`MSO365`

  var td46=document.createElement('td')
  td46.setAttribute("id","MSO365-matiere")
  td46.innerHTML=`Psychologie Du Travail Et des Organisations`

  var td47=document.createElement('td')
  td47.setAttribute("id","MSO365-note")

  var td48=document.createElement('td')
  td48.setAttribute("id","MSO365-coef")

  var td49=document.createElement('td')
  td49.setAttribute("id","MSO365-total")

  var td50=document.createElement('td')
  td50.setAttribute("id","MSO365-rang")

  var td51=document.createElement('td')
  td51.setAttribute("id","MSO365-mention")

  var td52=document.createElement('td')
  td52.setAttribute("id","MSO365-session")

  var td53=document.createElement('td')
  td53.setAttribute("id","MSO365-credits")

  var tr9=document.createElement('tr')
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
  var td100=document.createElement('td')
  td100.setAttribute('colspan','4')
  td100.innerHTML=`RESULTATS SEMESTRE 1`

  var td101=document.createElement('td')
  td101.setAttribute("id","resultat-coef")
  
  var td102=document.createElement('td')
  td102.setAttribute("id","resultat-total")
  
  var td103=document.createElement('td')
  td103.setAttribute("id","resultat-moyenne")
  
  var td104=document.createElement('td')
  td104.setAttribute("id","resultat-rang")
  
  var td105=document.createElement('td')
  td105.setAttribute("colspan","2")
  td105.setAttribute("id","resultat")
  td105.innerHTML=`Total Crédits Semestre 1`
  
  var td106=document.createElement('td')
  td106.setAttribute("id","resultat-crédits")

  var tr11=document.createElement('tr')
  tr11.appendChild(td100)
  tr11.appendChild(td101)
  tr11.appendChild(td102)
  tr11.appendChild(td103)
  tr11.appendChild(td104)
  tr11.appendChild(td105)
  tr11.appendChild(td106)

  //tbody
  var tbody=document.createElement('tbody')
  tbody.setAttribute('id','tbody01')
  tbody.appendChild(tr2)
  tbody.appendChild(tr3)
  tbody.appendChild(tr4)
  tbody.appendChild(tr5)
  tbody.appendChild(tr8)
  tbody.appendChild(tr9)
  tbody.appendChild(tr11)

  var table1=document.createElement('table')
  table1.setAttribute('class', 'table-1')
  table1.appendChild(thead1)
  table1.appendChild(tbody)

  //table3
  //thead2
  var tr12=document.createElement('tr')
  for(i=0; i<=11; i++){
    var th=document.createElement('th')
    th.setAttribute('scope','col')
    if(i==0){th.innerHTML=`&nbsp;&nbsp;`}
    tr12.appendChild(th)
  }
  var thead2=document.createElement('thead')
  thead2.appendChild(tr12)

  //tbody
  //Line 1
  var tr13=document.createElement('tr')
  for(i=0; i<=8; i++){
    var td=document.createElement('td')
    if(i==1){td.setAttribute('colspan','3'); td.innerHTML=`Moyenne de Classe de l'étudiant :`}
    if(i==2){td.innerHTML=`/ 20`}
    if(i==3){td.setAttribute('colspan','2'); td.innerHTML=`Maximum :`}
    if(i==7){td.innerHTML=`Retard :`}

    tr13.appendChild(td)
  }
  //Line 2
  var tr14=document.createElement('tr')
  for(i=0; i<=8; i++){
    var td=document.createElement('td')
    if(i==1){td.setAttribute('colspan','3'); td.innerHTML=`Moyenne Générale de la classe :`}
    if(i==2){td.innerHTML=`/ 20`}
    if(i==3){td.setAttribute('colspan','2'); td.innerHTML=`Minimum :`}
    if(i==7){td.innerHTML=`Absences:`}

    tr14.appendChild(td)
  }
  //Line 3
  var tr15=document.createElement('tr')
  for(i=0; i<=8; i++){
    var td=document.createElement('td')
    if(i==1){td.setAttribute('colspan','3');}
    if(i==4){td.setAttribute('colspan','2'); td.innerHTML=`Rang :`}
    if(i==5){td.innerHTML=` sur `}

    tr15.appendChild(td)
  }
  //Line 4
  var tbody3=document.createElement('tbody')
  tbody3.setAttribute('id', 'tbody-3')
  tbody3.appendChild(tr13)
  tbody3.appendChild(tr14)
  tbody3.appendChild(tr15)

  var table3=document.createElement('table')
  table3.setAttribute('id','table-3')
  table3.appendChild(thead2)
  table3.appendChild(tbody3)

  var semestreResult=document.createElement('div')
  semestreResult.setAttribute('id','semester-result')
  semestreResult.appendChild(table1)
  semestreResult.appendChild(table3)

  var main=document.createElement('main')
  main.appendChild(bullchecktitle)
  main.appendChild(infostudent)
  main.appendChild(semestreResult)

  var visa=document.createElement('div')
  visa.setAttribute('class','visa')
  visa.innerHTML="VISA CHEF ETABLISSEMENT"

  var footer=document.createElement('footer')
  footer.appendChild(visa)

  containerbull=document.createElement('div')
  containerbull.setAttribute('class','container-bull')
  containerbull.appendChild(header)
  containerbull.appendChild(hr)
  containerbull.appendChild(main)
  containerbull.appendChild(footer)

  /*body=document.getElementsByTagName('body')
  body[0].appendChild(containerbull)*/
  return(containerbull)
} 


/**FONCTION BULLETIN MDS */
function BullMDS1(clone){

  //DONNEES RECUPEREES DE LA BD
  var infoEtudiant = mydata[1]
  var coefUe = mydata[2]
  var creditUe = mydata[3]
  var mds111 = mydata[4]
  var mds111b = mydata[5]
  var mds112 = mydata[6]
  var mds113 = mydata[7]
  var mds114 = mydata[8]
  var mds115 = mydata[9]
  var mds116 = mydata[10]
  var mds117 = mydata[11]

  //Info Utilisateur
  var info1 = clone.children[2].children[1].children[0]
  for(j=2; j<=info1.childElementCount-1; j++){
    if(j==2){info1.children[j].innerHTML = info1.children[j].innerHTML +` ${infoEtudiant[i]['nom']}`}
    if(j==3){info1.children[j].innerHTML = info1.children[j].innerHTML +` ${infoEtudiant[i]['prenom']}`}
    //if(j==4){info1.children[j].innerHTML = info1.children[j].innerHTML +' er'}
  }

  var info2 = clone.children[2].children[1].children[1]
  for(j=1; j<=info2.childElementCount-1; j++){
    if(j==1){info2.children[j].innerHTML = info2.children[j].innerHTML +` ${infoEtudiant[i]['matricule']}`}
    if(j==2){info2.children[j].innerHTML = info2.children[j].innerHTML +` ${infoEtudiant[i]['date_naissance']}`}
    if(j==3){info2.children[j].innerHTML = info2.children[j].innerHTML +` ${infoEtudiant[i]['lieu_naissance']}`}
    //if(j==4){info1.children[j].innerHTML = info1.children[j].innerHTML +` ${infoEtudiant[i]['anneeaca']}`} //Année Academique
  }

  //Tableau de notes
  var tbody = clone.children[2].children[2].children[0].children[1]

  //LIGNE MDS11
  var ligneMDS111 = tbody.children[0]
  for(j=0; j<=ligneMDS111.childElementCount-1; j++){
    if(j==4){ligneMDS111.children[j].innerHTML = mds111[i]['note_Examen']}//note math
    if(j==5){ligneMDS111.children[j].innerHTML = coefUe[0]['coefficient']}//coef math
    if(j==6){val = ligneMDS111.children[4].innerHTML*ligneMDS111.children[5].innerHTML; val = val.toFixed(2); val = parseFloat(val) ;ligneMDS111.children[j].innerHTML = val}//total note math * coef
  if(j==7){ligneMDS111.children[j].innerHTML = Moyenne3( ligneMDS111.children[6].innerHTML, mds111b[i]['note_Examen']*coefUe[1]['coefficient'], mds112[i]['note_Examen']*coefUe[2]['coefficient'],((coefUe[0]['coefficient']+coefUe[1]['coefficient']+coefUe[2]['coefficient'])) ) } //moyenne donc (totalmath + totalinfo)/2
    if(j==8){/*ligneMDS111.children[j].innerHTML =  mds1sort.indexof(mds111[i]['note_Examen'])*/}//Rang
    if(j==9){if(ligneMDS111.children[4].innerHTML >= 10){
      ligneMDS111.children[9].innerHTML = "VALIDEE"
    }else{ligneMDS111.children[9].innerHTML = "NON VALIDEE"}}//Mention
    if(j==10){}//Session
    if(j==11){if(mds111[i]["note_Examen"]>= 10 && mds111b[i]['note_Examen']>= 10){ligneMDS111.children[j].innerHTML = creditUe[0]['nombre_credit']}else{ligneMDS111.children[j].innerHTML = 0}}//Crédits
  }

  //LIGNE MDS11b
  var ligneMDS111b = tbody.children[1]
  for(j=0; j<=ligneMDS111b.childElementCount-1; j++){
    if(j==2){ligneMDS111b.children[j].innerHTML = mds111b[i]['note_Examen']}//note info
    if(j==3){ligneMDS111b.children[j].innerHTML = coefUe[1]['coefficient']}//coef info
    if(j==4){val=ligneMDS111b.children[2].innerHTML*ligneMDS111b.children[3].innerHTML; val= val.toFixed(2); val = parseFloat(val); ligneMDS111b.children[j].innerHTML = val}//total note math * coef
    if(j==5){}//Rang
    if(j==6){
      if(ligneMDS111b.children[2].innerHTML >= 10){ligneMDS111b.children[6].innerHTML = "VALIDEE"}else{ligneMDS111b.children[6].innerHTML = "NON VALIDEE"}}
    if(j==7){}//Session
    if(j==8){if(mds111[i]["note_Examen"]>= 10 && mds111b[i]['note_Examen']>= 10){ligneMDS111b.children[j].innerHTML = creditUe[1]['nombre_credit']}else{ligneMDS111b.children[j].innerHTML = 0}}//Crédits
  }

  //LIGNE MDS112
  var ligneMDS112 = tbody.children[2]
  for(j=0; j<=ligneMDS112.childElementCount-1; j++){
    if(j==2){ligneMDS112.children[j].innerHTML = mds112[i]['note_Examen']}//note info
    if(j==3){ligneMDS112.children[j].innerHTML = coefUe[2]['coefficient']}//coef info
    if(j==4){val=ligneMDS112.children[2].innerHTML*ligneMDS112.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val); ligneMDS112.children[j].innerHTML = val}//total note math * coef
    if(j==5){}//Rang
    if(j==6){if(ligneMDS112.children[2].innerHTML >= 10){ligneMDS112.children[j].innerHTML = "VALIDEE"}else{ligneMDS112.children[j].innerHTML ="NON VALIDEE"}}//Mention
    if(j==7){}//Session
    if(j==8){if(ligneMDS112.children[2].innerHTML>=10){ligneMDS112.children[j].innerHTML = creditUe[2]['nombre_credit']}else{ligneMDS112.children[j].innerHTML = 0}} //nombre_crédits
  }

  //LIGNE MDS113
  var ligneMDS113 = tbody.children[3]
  for(j=0; j<=ligneMDS113.childElementCount-1; j++){
    if(j==3){ligneMDS113.children[j].innerHTML = mds113[i]['note_Examen']}//note math
    if(j==4){ligneMDS113.children[j].innerHTML = coefUe[3]['coefficient']}//coef math
    if(j==5){val=ligneMDS113.children[3].innerHTML*ligneMDS113.children[4].innerHTML; val=val.toFixed(2); val=parseFloat(val); ligneMDS113.children[j].innerHTML = val}//total note math * coef
    if(j==6){ligneMDS113.children[j].innerHTML = 
      Moyenne4( 
        ligneMDS113.children[5].innerHTML, 
        mds114[i]['note_Examen']*coefUe[4]['coefficient'], 
        mds115[i]['note_Examen']*coefUe[5]['coefficient'], 
        mds116[i]['note_Examen']*coefUe[6]['coefficient'],
        ( (coefUe[3]['coefficient']+coefUe[4]['coefficient']+ coefUe[5]['coefficient']+coefUe[6]['coefficient']) )
      );} //moyenne donc (totalmath + totalinfo)/2
    if(j==7){}//Rang
    if(j==8){if(ligneMDS113.children[3].innerHTML >= 10){ligneMDS113.children[j].innerHTML = "VALIDEE"}else{ligneMDS113.children[j].innerHTML = "NON VALIDEE"}}//Mention
    if(j==9){}
    if(j==10){if(mds113[i]["note_Examen"]>= 10){ligneMDS113.children[j].innerHTML = creditUe[3]['nombre_credit']}else{ligneMDS113.children[j].innerHTML = 0}}//Crédits
  }

  //LINE MDS114
  var ligneMDS114 = tbody.children[4]
  for(j=0; j<=ligneMDS114.childElementCount-1; j++){
    if(j==2){ligneMDS114.children[j].innerHTML = mds114[i]['note_Examen']}//note info
    if(j==3){ligneMDS114.children[j].innerHTML = coefUe[4]['coefficient']}//coef info
    if(j==4){val=ligneMDS114.children[2].innerHTML*ligneMDS114.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val); ligneMDS114.children[j].innerHTML = val }//total note math * coef
    if(j==5){}//Rang
    if(j==6){if(ligneMDS114.children[2].innerHTML >= 10){ligneMDS114.children[j].innerHTML = "VALIDEE"}else{ligneMDS114.children[j].innerHTML ="NON VALIDEE"}}//Mention
    if(j==7){}//Session
    if(j==8){if(ligneMDS114.children[2].innerHTML>=10){ligneMDS114.children[j].innerHTML = creditUe[4]['nombre_credit']}else{ligneMDS114.children[j].innerHTML = 0}} //nombre_crédits
  }

  //LINE MDS115
  var ligneMDS115 = tbody.children[5]
  for(j=0; j<=ligneMDS115.childElementCount-1; j++){
    if(j==2){ligneMDS115.children[j].innerHTML = mds115[i]['note_Examen']}//note info
    if(j==3){ligneMDS115.children[j].innerHTML = coefUe[5]['coefficient']}//coef info
    if(j==4){val=ligneMDS115.children[2].innerHTML*ligneMDS115.children[3].innerHTML; val=val.toFixed(2);val=parseFloat(val); ligneMDS115.children[j].innerHTML = val}//total note math * coef
    if(j==5){}//Rang
    if(j==6){if(ligneMDS115.children[2].innerHTML >= 10){ligneMDS115.children[j].innerHTML = "VALIDEE"}else{ligneMDS115.children[j].innerHTML ="NON VALIDEE"}}//Mention
    if(j==7){}//Session
    if(j==8){if(ligneMDS115.children[2].innerHTML>=10){ligneMDS115.children[j].innerHTML = creditUe[5]['nombre_credit']}else{ligneMDS115.children[j].innerHTML = 0}} //nombre_crédits
  }

  //LINE MD16
  var ligneMDS116 = tbody.children[6]
  for(j=0; j<=ligneMDS116.childElementCount-1; j++){
    if(j==2){ligneMDS116.children[j].innerHTML = mds116[i]['note_Examen']}//note info
    if(j==3){ligneMDS116.children[j].innerHTML = coefUe[4]['coefficient']}//coef info
    if(j==4){val=ligneMDS116.children[2].innerHTML*ligneMDS116.children[3].innerHTML;val=val.toFixed(2);val=parseFloat(val); ligneMDS116.children[j].innerHTML = val}//total note math * coef
    if(j==5){}//Rang
    if(j==6){if(ligneMDS116.children[2].innerHTML >= 10){ligneMDS116.children[j].innerHTML = "VALIDEE"}else{ligneMDS116.children[j].innerHTML ="NON VALIDEE"}}//Mention
    if(j==7){}//Session
    if(j==8){if(ligneMDS116.children[2].innerHTML>=10){ligneMDS116.children[j].innerHTML = creditUe[6]['nombre_credit']}else{ligneMDS116.children[j].innerHTML = 0}} //nombre_crédits
  }

  //LINE 17
  var ligneMDS117 = tbody.children[7]
  for(j=0; j<=ligneMDS117.childElementCount-1; j++){
    if(j==3){ligneMDS117.children[j].innerHTML = mds117[i]['note_Examen']}//note math
    if(j==4){ligneMDS117.children[j].innerHTML = coefUe[7]['coefficient']}//coef math
    if(j==5){val=ligneMDS117.children[3].innerHTML*ligneMDS117.children[4].innerHTML; val=val.toFixed(2); val=parseFloat(val); ligneMDS117.children[j].innerHTML = val}//total note math * coef
    if(j==6){ligneMDS117.children[j].innerHTML = ligneMDS117.children[3].innerHTML} //moyenne donc (totalmath + totalinfo)/2
    if(j==7){}//Rang
    if(j==8){if(ligneMDS117.children[3].innerHTML >= 10){ligneMDS117.children[j].innerHTML = "VALIDEE"}else{ligneMDS117.children[j].innerHTML = "NON VALIDEE"}}//Mention
    if(j==9){}
    if(j==10){if(mds117[i]["note_Examen"]>= 10){ligneMDS117.children[j].innerHTML = creditUe[7]['nombre_credit']}else{ligneMDS117.children[j].innerHTML = 0}}//Crédits
  }

  //LINE DEs RESULTATS
  var resultat = tbody.children[8]
  for(j=0; j<=resultat.childElementCount-1; j++){
    if(j==1){
      resultat.children[1].innerHTML = sommeInt1(ligneMDS111.children[5].innerHTML, ligneMDS111b.children[3].innerHTML, ligneMDS112.children[3].innerHTML, ligneMDS113.children[4].innerHTML, ligneMDS114.children[3].innerHTML, ligneMDS115.children[3].innerHTML, ligneMDS116.children[3].innerHTML, ligneMDS117.children[4].innerHTML);
    }
    if(j==2){resultat.children[2].innerHTML = sommeFloat(ligneMDS111b.children[4].innerHTML, ligneMDS111.children[6].innerHTML, ligneMDS112.children[4].innerHTML, ligneMDS113.children[5].innerHTML, ligneMDS114.children[4].innerHTML, ligneMDS115.children[4].innerHTML,ligneMDS116.children[4].innerHTML, ligneMDS117.children[5].innerHTML) }
    if(j==3){ val = resultat.children[2].innerHTML / resultat.children[1].innerHTML; val=val.toFixed(2); val=parseFloat(val); resultat.children[j].innerHTML= val}
    if(j==6){ resultat.children[6].innerHTML =  sommeInt(ligneMDS111.children[11].innerHTML ,ligneMDS112.children[8].innerHTML,ligneMDS113.children[10].innerHTML, ligneMDS114.children[8].innerHTML,ligneMDS115.children[8].innerHTML, ligneMDS116.children[8].innerHTML, ligneMDS117.children[10].innerHTML) }
  }


  return(clone)
}




//FONCTIONS
function Moyenne3(a,b,c, coef){ 
  a = parseFloat(a); 
  b = parseFloat(b); 
  c = parseFloat(c);
  result= (a + b + c)/coef; result = result.toFixed(2); 
  result = parseFloat(result);
  return(result)
}
function Moyenne4(a,b,c,d, coef){ 
  a = parseFloat(a); 
  b = parseFloat(b); 
  c = parseFloat(c);
  d = parseFloat(d);
  result= (a + b + c + d)/coef; 
  result = result.toFixed(2); 
  result = parseFloat(result);
  return(result)
}
function sommeInt(a,b,c,d,e,f,g){
  a = parseInt(a)
  b = parseInt(b); 
  c = parseInt(c);
  d = parseInt(d);
  e = parseInt(e);
  f = parseInt(f);
  g = parseInt(g);

  result = a + b + c + d + e + f + g

  return(result)
}
function sommeInt1(a,b,c,d,e,f,g,h){
  a = parseInt(a)
  b = parseInt(b); 
  c = parseInt(c);
  d = parseInt(d);
  e = parseInt(e);
  f = parseInt(f);
  g = parseInt(g);
  h = parseInt(h);

  result = a + b + c + d + e + f + g + h
  return(result)
}
function sommeFloat(a,b,c,d,e,f,g,h){
  a = parseFloat(a)
  b = parseFloat(b); 
  c = parseFloat(c);
  d = parseFloat(d);
  e = parseFloat(e);
  f = parseFloat(f);
  g = parseFloat(g);
  h = parseFloat(h);

  result = a + b + c + d + e + f + g + h
  result = result.toFixed(2)
  result = parseFloat(result)

  return(result)
}
function triCroissant(b){
  for(i=0; i<=b.length; i++){
    
    for(j=i+1; j<=b.length; j++){
      if(b[i] >= b[j]){
        tmp = b[i]
        b[i] = b[j]
        b[j] = tmp
      }
    }
  }

  return (b)
}

function formatAsArray(b){
  ar=[];
  for(var i = 0; i<=b.length; i++){
    console.log(b[i]['note_Examen']);
  }
  return(ar)
}