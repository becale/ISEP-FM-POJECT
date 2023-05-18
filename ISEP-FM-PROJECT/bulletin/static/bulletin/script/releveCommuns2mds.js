window.addEventListener('load',()=>{
    //Recuperation de la variable des données
     mydata = JSON.parse(document.getElementById('semestre1MDS').textContent);
     console.log(mydata) 

    
     function Page1(){ 
        listStudent = mydata[1]

        //console.log(listStudent);

        bigtab = document.getElementById('table1')

        //page2.children[1].children[1].children[1]
        page = document.getElementById("page2")
        bigtab1 = page.children[1].children[1]


        //Tableau Sur lequel on ajoute les nouvelles lignes
        worktab = bigtab.children[1]
        worktab1 = bigtab1.children[1]
        //Ligne des 4 tableaux
        
        
        for(i=0; i<=mydata[1].length-1; i++){

            temp = worktab.children[3].cloneNode(true)

            //temp1 = worktab1.children[3].cloneNode(true)

            //tab0
            tab0 = temp.children[0]
            tab01 = tab0.children.nested4
            tab02 = tab01.children
            tab03 = tab02['0']
            tab04 = tab03.children
            tab05 = tab04[0] //good  
            ////
            /*tab00 = temp1.children[0]
            tab001 = tab00.children.nested4
            tab002 = tab001.children
            tab003 = tab002['0']
            tab004 =tab003.children
            tab005 = tab004[0]//good*/

            for(j=0; j<=tab05.childElementCount-1; j++){
                if(j==0){
                    tab05.cells[j].innerHTML = i+1;
                    //tab005.cells[j].innerHTML = i+1;
                }
                if(j==1){
                    tab05.cells[j].innerHTML = listStudent[i][0]['nom']; 
                }
                if(j==2){
                    tab05.cells[j].innerHTML = listStudent[i][0]['prenom'];
                }
                if(j==3){
                    tab05.cells[j].innerHTML = listStudent[i][0]['matricule'];
                }
            }

            //tab0 Page2

            //tab1
            tab1 = temp.children[1]
            tab11 = tab1.children.nested11
            tab12 = tab11.children
            tab13 = tab12['0']
            tab14 = tab13.children
            tab15 = tab14[0] //good line
            //
            /*tab111 = temp1.children[1]
            tab112 = tab111.children.nested11
            tab113 = tab112.children
            tab114 = tab113['0']
            tab115 = tab114.children
            tab116 = tab115['0'] //good line*/

            for(j=0; j<=tab15.childElementCount-1; j++){
                if(j==0){
                    tab15.cells[j].innerHTML= listStudent[i][1][0];
                };
                    
                if(j==1){
                    tab15.cells[j].innerHTML= listStudent[i][2][0]
                }
                if(j==2){
                    tab15.cells[j].innerHTML=listStudent[i][3][0]
                }
                if(j==3){
                    tab15.cells[j].innerHTML= listStudent[i][4][0]
                }
                if(j==4){
                    tab15.cells[j].innerHTML= listStudent[i][1][3];
                }
                if(j==5){
                    if(listStudent[i][1][3]>=10){tab15.cells[j].innerHTML="V"}else{tab15.cells[j].innerHTML="NV"}
                    
                }
            }

            //tab2
            tab2 = temp.children[2]
            tab21 = tab2.children.nested22
            tab22 = tab21.children['0']
            tab23 = tab22.children['0']
            for(j=0; j<=tab23.childElementCount-1; j++){
                if(j==0){tab23.cells[j].innerHTML = listStudent[i][5][0]};
                if(j==1){tab23.cells[j].innerHTML = listStudent[i][6][0]};
                if(j==2){tab23.cells[j].innerHTML = listStudent[i][7][0]};
                if(j==3){tab23.cells[j].innerHTML = listStudent[i][8][0]};

                if(j==4){tab23.cells[j].innerHTML = listStudent[i][5][3]};
                if(j==5){if(listStudent[i][5][3]>=10){tab23.cells[j].innerHTML ='V'}else{tab23.cells[j].innerHTML ='NV'}};//{ {if(listStudent[i][7][5]){tab23.cells[j].innerHTML ='V'}else{tab23.cells[j].innerHTML ='NV'}};};

            }

            //tab3
            tab3 = temp.children[3]
            tab31 = tab3.children.nested33
            tab32 = tab31.children['0']
            tab33 = tab32.children['0']

            for(j=0; j<=tab33.childElementCount-1; j++){
                if(j==0){tab33.cells[j].innerHTML = listStudent[i][9][0]};
                if(j==1){tab33.cells[j].innerHTML = listStudent[i][10][0]};;
        
                if(j==2){tab33.cells[j].innerHTML = listStudent[i][9][3]};
                if(j==3){if (listStudent[i][9][3]  >= 10){ tab33.cells[j].innerHTML ='V' }else{ tab33.cells[j].innerHTML ='NV'};}
            }
            
            //tab4
            tab4 = temp.children[4]
            tab41 = tab4.children.nested333
            tab42 = tab41.children['0']
            tab43 = tab42.children['0']
            for(j=0; j<=tab43.childElementCount-1; j++){
                if(j==0){tab43.cells[j].innerHTML = listStudent[i][11][1]};
                if(j==1){tab43.cells[j].innerHTML = listStudent[i][11][2]};;
                if(j==2){tab43.cells[j].innerHTML = mydata[2].indexOf(listStudent[i][11][2])+1}
                if(j==3){tab43.cells[j].innerHTML = listStudent[i][2][7]+listStudent[i][4][7]+listStudent[i][5][7]+listStudent[i][6][7]+listStudent[i][7][7]+listStudent[i][8][7]+listStudent[i][9][7]+listStudent[i][10][7]};
                if(j==4){tab43.cells[j].innerHTML = '/'};
            }

            //Ajoute de la ligne au grand tableau
            worktab.appendChild(temp)
            //worktab1.appendChild(temp1)
   }}
    Page1()

    /**FUNCTION MULTI_PAGE FOR PROCES VERBAL */
    function ListProcess(){

        body = document.getElementById('body')

        page = document.getElementById('page2')

        listProces = document.createElement('div');
        
        for(i=0; i<=9; i++){
            clone = page.cloneNode(true)
            clone.style.display = 'block'
            clone = fullfill(clone, i)

            listProces.appendChild(clone)
        }

        //Fixation de ListProcess sur le body de la page
        body.appendChild(listProces)
     }
    
    /**FONCTION DE REMPLISSAGE DU CLONE */
    function fullfill(clone, i){
        //Pagination
        pagination=clone.children[3]


        //Line 1

        //Line 2
        line2 = clone.children[1].children[1].children[0]
        line2.children[2].innerHTML = ' MANAGEMENT DU SPORT'
        line2.children[5].innerHTML = '2022/2023'

        //Third Line
        line3 = clone.children[1].children[2].children[0]

        if(i == 0){ 
            line3.children[1].innerHTML = "MDS111"; 
            line3.children[2].innerHTML = "MATHEMATIQUES I";
            line3.children[4].innerHTML = mydata[5][0]
            line3.children[6].innerHTML = '1'

            pagination.innerText= `Page ${i+1} / ${mydata[5].length}`
        }
        if(i == 1){ 
            line3.children[1].innerHTML = "MDS111";
            line3.children[2].innerHTML = "INFORMATIQUE I";
            line3.children[4].innerHTML = mydata[5][1]
            line3.children[6].innerHTML = '1'

            pagination.innerText= `Page ${i+1} / ${mydata[5].length}`
        }
        if(i == 2){ 
            line3.children[1].innerHTML = "MDS112";
            line3.children[2].innerHTML = "MATHEMATIQUES FINANCIERES";
            line3.children[4].innerHTML = mydata[5][2]
            line3.children[6].innerHTML = '1'

            pagination.innerText= `Page ${i+1} / ${mydata[5].length}`
        }
        if(i == 3){ 
            line3.children[1].innerHTML = "MDS112";
            line3.children[2].innerHTML = "STATISTIQUES DESCRIPTIVES";
            line3.children[4].innerHTML = mydata[5][3]
            line3.children[6].innerHTML = '1'

            pagination.innerText= `Page ${i+1} / ${mydata[5].length}`
        }
        if(i == 4){ 
            line3.children[1].innerHTML = "MDS113";
            line3.children[2].innerHTML = "ENVIRONNEMENT JURIDIQUE ET COMPTABLE I";
            line3.children[4].innerHTML = mydata[5][4]
            line3.children[6].innerHTML = '1'

            pagination.innerText= `Page ${i+1} / ${mydata[5].length}`
        }
        if(i == 5){ 
            line3.children[1].innerHTML = "MDS114";
            line3.children[2].innerHTML = "MARKETING";
            line3.children[4].innerHTML = mydata[5][5]
            line3.children[6].innerHTML = '1'

            pagination.innerText= `Page ${i+1} / ${mydata[5].length}`
        }
        if(i == 6){ 
            line3.children[1].innerHTML = "MDS115";
            line3.children[2].innerHTML = "OUTILS DE GESTION DU SPORT I";
            line3.children[4].innerHTML = mydata[5][6]
            line3.children[6].innerHTML = '1'

            pagination.innerText= `Page ${i+1} / ${mydata[5].length}`
        }
        if(i == 7){ 
            line3.children[1].innerHTML = "MDS116";
            line3.children[2].innerHTML = "GESTION DES STRUCTURES ET ORGANISATIONS SPORTIVES I";
            line3.children[4].innerHTML = mydata[5][7]
            line3.children[6].innerHTML = '1'

            pagination.innerText= `Page ${i+1} / ${mydata[5].length}`
        }
        if(i == 8){ 
            line3.children[1].innerHTML = "MDS117";
            line3.children[2].innerHTML = "TECHNIQUE D'EXPRESSION ANGLAISE";
            line3.children[4].innerHTML = mydata[5][8]
            line3.children[6].innerHTML = '1'

            pagination.innerText= `Page ${i+1} / ${mydata[5].length}`
        }
        if(i == 9){ 
            line3.children[1].innerHTML = "MDS117";
            line3.children[2].innerHTML = "TECHNIQUE D'EXPRESSION FRANCAISE";
            line3.children[4].innerHTML = mydata[5][9]
            line3.children[6].innerHTML = '1'

            pagination.innerText= `Page ${i+1} / ${mydata[5].length}`
        }

        //Tableau des students
        tab = clone.children[2].children[0]

        listStudent = mydata[1]

        tableContainer = document.getElementById('tableContainer')

        /**STATS */
        for(j=0; j<=mydata[1].length-1; j++){
          

            line = document.createElement('tr')

            for(k=0; k<=8; k++){
                td = document.createElement('td')
                if(k==0){
                    td.innerHTML=`${j+1}`;
                    td.setAttribute('class','numero')
                }
                if(k==1){
                    td.innerHTML=`${listStudent[j][0]['matricule']}`
                    td.setAttribute('class','matricule')
                }
                if(k==2){
                    td.innerHTML=`${listStudent[j][0]['nom']}`+` ${listStudent[j][0]['prenom']}`;
                    td.setAttribute('class', 'nomprenon')

                }
                if(k==3){
                    if(i==0){td.innerHTML=`${listStudent[j][1][8]}`}
                    if(i==1){td.innerHTML=`${listStudent[j][2][8]}`}
                    if(i==2){td.innerHTML=`${listStudent[j][3][8]}`}
                    if(i==3){td.innerHTML=`${listStudent[j][4][8]}`}
                    if(i==4){td.innerHTML=`${listStudent[j][5][8]}`}
                    if(i==5){td.innerHTML=`${listStudent[j][6][8]}`}
                    
                    if(i==6){td.innerHTML=`${listStudent[j][7][8]}`}
                    if(i==7){td.innerHTML=`${listStudent[j][8][8]}`}
                    if(i==8){td.innerHTML=`${listStudent[j][9][8]}`}
                    if(i==9){td.innerHTML=`${listStudent[j][10][8]}`}
                    td.setAttribute('class','cc')
                }
                if(k==4){
                    if(i==0){td.innerHTML=`${listStudent[j][1][9]}`}
                    if(i==1){td.innerHTML=`${listStudent[j][2][9]}`}
                    if(i==2){td.innerHTML=`${listStudent[j][3][9]}`}
                    if(i==3){td.innerHTML=`${listStudent[j][4][9]}`}
                    if(i==4){td.innerHTML=`${listStudent[j][5][9]}`}
                    if(i==5){td.innerHTML=`${listStudent[j][6][9]}`}
                    if(i==6){td.innerHTML=`${listStudent[j][7][9]}`}
                    if(i==7){td.innerHTML=`${listStudent[j][8][9]}`}
                    if(i==8){td.innerHTML=`${listStudent[j][9][9]}`}
                    if(i==9){td.innerHTML=`${listStudent[j][10][9]}`}
                }
                if(k==5){
                    if(i==0){td.innerHTML=`${listStudent[j][1][0]}`; 
                    td.setAttribute('class', 'moyenne'); 
                }
                    if(i==1){td.innerHTML=`${listStudent[j][2][0]}`}
                    if(i==2){td.innerHTML=`${listStudent[j][3][0]}`}
                    if(i==3){td.innerHTML=`${listStudent[j][4][0]}`}
                    if(i==4){td.innerHTML=`${listStudent[j][5][0]}`}
                    if(i==5){td.innerHTML=`${listStudent[j][6][0]}`}

                    if(i==6){td.innerHTML=`${listStudent[j][7][0]}`}
                    if(i==7){td.innerHTML=`${listStudent[j][8][0]}`}
                    if(i==8){td.innerHTML=`${listStudent[j][9][0]}`}
                    if(i==9){td.innerHTML=`${listStudent[j][10][0]}`}
                }
                if(k==6){
                    if(i==0){
                        if(listStudent[j][1][5]){td.innerHTML=`${listStudent[j][1][6]}`}else{td.innerHTML=0}
                    }
                    if(i==1){
                        if(listStudent[j][2][5]){td.innerHTML=`${listStudent[j][2][6]}`}else{td.innerHTML=0}
                    }
                    if(i==2){
                        if(listStudent[j][3][5]){td.innerHTML=`${listStudent[j][3][6]}`}else{td.innerHTML=0}
                    }
                    if(i==3){
                        if(listStudent[j][4][5]){td.innerHTML=`${listStudent[j][4][6]}`}else{td.innerHTML=0}
                    }
                    if(i==4){
                        if(listStudent[j][5][5]){td.innerHTML=`${listStudent[j][5][6]}`}else{td.innerHTML=0}
                    }
                    if(i==5){
                        if(listStudent[j][6][5]){td.innerHTML=`${listStudent[j][6][6]}`}else{td.innerHTML=0}
                    }

                    if(i==6){
                        if(listStudent[j][7][5]){td.innerHTML=`${listStudent[j][7][6]}`}else{td.innerHTML=0}
                    }
                    if(i==7){
                        if(listStudent[j][8][5]){td.innerHTML=`${listStudent[j][8][6]}`}else{td.innerHTML=0}
                    }
                    if(i==8){
                        if(listStudent[j][9][5]){td.innerHTML=`${listStudent[j][9][6]}`}else{td.innerHTML=0}
                    }
                    if(i==9){
                        if(listStudent[j][10][5]){td.innerHTML=`${listStudent[j][10][6]}`}else{td.innerHTML=0}
                    }
                }
                if(k==7){
                    if(i==0){ if(listStudent[j][1][5]){td.innerHTML='Validée'}else{td.innerHTML='Non Validée'} }
                    if(i==1){ if(listStudent[j][2][5]){td.innerHTML='Validée'}else{td.innerHTML='Non Validée'} }
                    if(i==2){ if(listStudent[j][3][5]){td.innerHTML='Validée'}else{td.innerHTML='Non Validée'} }
                    if(i==3){ if(listStudent[j][4][5]){td.innerHTML='Validée'}else{td.innerHTML='Non Validée'} }
                    if(i==4){ if(listStudent[j][5][5]){td.innerHTML='Validée'}else{td.innerHTML='Non Validée'} }
                    if(i==5){ if(listStudent[j][6][5]){td.innerHTML='Validée'}else{td.innerHTML='Non Validée'} }
                    
                    if(i==6){ if(listStudent[j][7][5]){td.innerHTML='Validée'}else{td.innerHTML='Non Validée'} }
                    if(i==7){ if(listStudent[j][8][5]){td.innerHTML='Validée'}else{td.innerHTML='Non Validée'} }
                    if(i==8){ if(listStudent[j][9][5]){td.innerHTML='Validée'}else{td.innerHTML='Non Validée'} }
                    if(i==9){ if(listStudent[j][10][5]){td.innerHTML='Validée'}else{td.innerHTML='Non Validée'} }
                }
                if(k==8){
                    if(i==0){ 
                        if(listStudent[j][1][0] >= 16){
                            td.innerHTML='A'; 
                        }else if(listStudent[j][1][0] >= 15 && listStudent[j][1][0] < 16){
                            td.innerHTML='A-'
                        }else if(listStudent[j][1][0] >= 14 && listStudent[j][1][0] < 15){
                            td.innerHTML='B+'
                        }else if(listStudent[j][1][0] >= 13 && listStudent[j][1][0] < 14){
                            td.innerHTML='B'
                        }else if(listStudent[j][1][0] >= 12 && listStudent[j][1][0] < 13){
                            td.innerHTML='B-'
                        }else if(listStudent[j][1][0] >= 11 && listStudent[j][1][0] < 12){
                            td.innerHTML='C+'
                        }else if(listStudent[j][1][0] >= 10 && listStudent[j][1][0] < 11){
                            td.innerHTML='C'
                        }else if(listStudent[j][1][0] >= 9 && listStudent[j][1][0] < 10){
                            td.innerHTML='C-'
                        }else if(listStudent[j][1][0] >= 8 && listStudent[j][1][0] < 9){
                            td.innerHTML='D+'
                        }else if(listStudent[j][1][0] >= 7 && listStudent[j][1][0] < 8){
                            td.innerHTML='D'
                        }else if(listStudent[j][1][0] >= 6 && listStudent[j][1][0] < 7){
                            td.innerHTML='E'
                        }else if(listStudent[j][1][0] >= 0 && listStudent[j][1][0] < 6){
                            td.innerHTML='F'
                        }
                    }

                    if(i==1){
                        if(listStudent[j][2][0] >= 16){
                            td.innerHTML='A'
                        }else if(listStudent[j][2][0] >= 15 && listStudent[j][2][0] < 16){
                            td.innerHTML='A-'
                        }else if(listStudent[j][2][0] >= 14 && listStudent[j][2][0] < 15){
                            td.innerHTML='B+'
                        }else if(listStudent[j][2][0] >= 13 && listStudent[j][2][0] < 14){
                            td.innerHTML='B'
                        }else if(listStudent[j][2][0] >= 12 && listStudent[j][2][0] < 13){
                            td.innerHTML='B-'
                        }else if(listStudent[j][2][0] >= 11 && listStudent[j][2][0] < 12){
                            td.innerHTML='C+'
                        }else if(listStudent[j][2][0] >= 10 && listStudent[j][2][0] < 11){
                            td.innerHTML='C'
                        }else if(listStudent[j][2][0] >= 9 && listStudent[j][2][0] < 10){
                            td.innerHTML='C-'
                        }else if(listStudent[j][2][0] >= 8 && listStudent[j][2][0] < 9){
                            td.innerHTML='D+'
                        }else if(listStudent[j][2][0] >= 7 && listStudent[j][2][0] < 8){
                            td.innerHTML='D'
                        }else if(listStudent[j][2][0] >= 6 && listStudent[j][2][0] < 7){
                            td.innerHTML='E'
                        }else if(listStudent[j][2][0] >= 0 && listStudent[j][2][0] < 6){
                            td.innerHTML='F'
                        }
                    }

                    if(i==2){
                        if(listStudent[j][3][0] >= 16){
                            td.innerHTML='A'
                        }else if(listStudent[j][3][0] >= 15 && listStudent[j][3][0] < 16){
                            td.innerHTML='A-'
                        }else if(listStudent[j][3][0] >= 14 && listStudent[j][3][0] < 15){
                            td.innerHTML='B+'
                        }else if(listStudent[j][3][0] >= 13 && listStudent[j][3][0] < 14){
                            td.innerHTML='B'
                        }else if(listStudent[j][3][0] >= 12 && listStudent[j][3][0] < 13){
                            td.innerHTML='B-'
                        }else if(listStudent[j][3][0] >= 11 && listStudent[j][3][0] < 12){
                            td.innerHTML='C+'
                        }else if(listStudent[j][3][0] >= 10 && listStudent[j][3][0] < 11){
                            td.innerHTML='C'
                        }else if(listStudent[j][3][0] >= 9 && listStudent[j][3][0] < 10){
                            td.innerHTML='C-'
                        }else if(listStudent[j][3][0] >= 8 && listStudent[j][3][0] < 9){
                            td.innerHTML='D+'
                        }else if(listStudent[j][3][0] >= 7 && listStudent[j][3][0] < 8){
                            td.innerHTML='D'
                        }else if(listStudent[j][3][0] >= 6 && listStudent[j][3][0] < 7){
                            td.innerHTML='E'
                        }else if(listStudent[j][3][0] >= 0 && listStudent[j][3][0] < 6){
                            td.innerHTML='F'
                        }
                    }

                    if(i==3){
                        if(listStudent[j][4][0] >= 16){
                            td.innerHTML='A'
                        }else if(listStudent[j][4][0] >= 15 && listStudent[j][4][0] < 16){
                            td.innerHTML='A-'
                        }else if(listStudent[j][4][0] >= 14 && listStudent[j][4][0] < 15){
                            td.innerHTML='B+'
                        }else if(listStudent[j][4][0] >= 13 && listStudent[j][4][0] < 14){
                            td.innerHTML='B'
                        }else if(listStudent[j][4][0] >= 12 && listStudent[j][4][0] < 13){
                            td.innerHTML='B-'
                        }else if(listStudent[j][4][0] >= 11 && listStudent[j][4][0] < 12){
                            td.innerHTML='C+'
                        }else if(listStudent[j][4][0] >= 10 && listStudent[j][4][0] < 11){
                            td.innerHTML='C'
                        }else if(listStudent[j][4][0] >= 9 && listStudent[j][4][0] < 10){
                            td.innerHTML='C-'
                        }else if(listStudent[j][4][0] >= 8 && listStudent[j][4][0] < 9){
                            td.innerHTML='D+'
                        }else if(listStudent[j][4][0] >= 7 && listStudent[j][4][0] < 8){
                            td.innerHTML='D'
                        }else if(listStudent[j][4][0] >= 6 && listStudent[j][4][0] < 7){
                            td.innerHTML='E'
                        }else if(listStudent[j][4][0] >= 0 && listStudent[j][4][0] < 6){
                            td.innerHTML='F'
                        }
                    }

                    if(i==4){
                        if(listStudent[j][5][0] >= 16){
                            td.innerHTML='A'
                        }else if(listStudent[j][5][0] >= 15 && listStudent[j][5][0] < 16){
                            td.innerHTML='A-'
                        }else if(listStudent[j][5][0] >= 14 && listStudent[j][5][0] < 15){
                            td.innerHTML='B+'
                        }else if(listStudent[j][5][0] >= 13 && listStudent[j][5][0] < 14){
                            td.innerHTML='B'
                        }else if(listStudent[j][5][0] >= 12 && listStudent[j][5][0] < 13){
                            td.innerHTML='B-'
                        }else if(listStudent[j][5][0] >= 11 && listStudent[j][5][0] < 12){
                            td.innerHTML='C+'
                        }else if(listStudent[j][5][0] >= 10 && listStudent[j][5][0] < 11){
                            td.innerHTML='C'
                        }else if(listStudent[j][5][0] >= 9 && listStudent[j][5][0] < 10){
                            td.innerHTML='C-'
                        }else if(listStudent[j][5][0] >= 8 && listStudent[j][5][0] < 9){
                            td.innerHTML='D+'
                        }else if(listStudent[j][5][0] >= 7 && listStudent[j][5][0] < 8){
                            td.innerHTML='D'
                        }else if(listStudent[j][5][0] >= 6 && listStudent[j][5][0] < 7){
                            td.innerHTML='E'
                        }else if(listStudent[j][5][0] >= 0 && listStudent[j][5][0] < 6){
                            td.innerHTML='F'
                        }
                    }

                    if(i==5){
                        if(listStudent[j][6][0] >= 16){
                            td.innerHTML='A'
                        }else if(listStudent[j][6][0] >= 15 && listStudent[j][6][0] < 16){
                            td.innerHTML='A-'
                        }else if(listStudent[j][6][0] >= 14 && listStudent[j][6][0] < 15){
                            td.innerHTML='B+'
                        }else if(listStudent[j][6][0] >= 13 && listStudent[j][6][0] < 14){
                            td.innerHTML='B'
                        }else if(listStudent[j][6][0] >= 12 && listStudent[j][6][0] < 13){
                            td.innerHTML='B-'
                        }else if(listStudent[j][6][0] >= 11 && listStudent[j][6][0] < 12){
                            td.innerHTML='C+'
                        }else if(listStudent[j][6][0] >= 10 && listStudent[j][6][0] < 11){
                            td.innerHTML='C'
                        }else if(listStudent[j][6][0] >= 9 && listStudent[j][6][0] < 10){
                            td.innerHTML='C-'
                        }else if(listStudent[j][6][0] >= 8 && listStudent[j][6][0] < 9){
                            td.innerHTML='D+'
                        }else if(listStudent[j][6][0] >= 7 && listStudent[j][6][0] < 8){
                            td.innerHTML='D'
                        }else if(listStudent[j][6][0] >= 6 && listStudent[j][6][0] < 7){
                            td.innerHTML='E'
                        }else if(listStudent[j][6][0] >= 0 && listStudent[j][6][0] < 6){
                            td.innerHTML='F'
                        }
                    }

                    if(i==6){
                        if(listStudent[j][7][0] >= 16){
                            td.innerHTML='A'
                        }else if(listStudent[j][7][0] >= 15 && listStudent[j][7][0] < 16){
                            td.innerHTML='A-'
                        }else if(listStudent[j][7][0] >= 14 && listStudent[j][7][0] < 15){
                            td.innerHTML='B+'
                        }else if(listStudent[j][7][0] >= 13 && listStudent[j][7][0] < 14){
                            td.innerHTML='B'
                        }else if(listStudent[j][7][0] >= 12 && listStudent[j][7][0] < 13){
                            td.innerHTML='B-'
                        }else if(listStudent[j][7][0] >= 11 && listStudent[j][7][0] < 12){
                            td.innerHTML='C+'
                        }else if(listStudent[j][7][0] >= 10 && listStudent[j][7][0] < 11){
                            td.innerHTML='C'
                        }else if(listStudent[j][7][0] >= 9 && listStudent[j][7][0] < 10){
                            td.innerHTML='C-'
                        }else if(listStudent[j][7][0] >= 8 && listStudent[j][7][0] < 9){
                            td.innerHTML='D+'
                        }else if(listStudent[j][7][0] >= 7 && listStudent[j][7][0] < 8){
                            td.innerHTML='D'
                        }else if(listStudent[j][7][0] >= 6 && listStudent[j][7][0] < 7){
                            td.innerHTML='E'
                        }else if(listStudent[j][7][0] >= 0 && listStudent[j][7][0] < 6){
                            td.innerHTML='F'
                        }
                    }

                    if(i==7){
                        if(listStudent[j][8][0] >= 16){
                            td.innerHTML='A'
                        }else if(listStudent[j][8][0] >= 15 && listStudent[j][8][0] < 16){
                            td.innerHTML='A-'
                        }else if(listStudent[j][8][0] >= 14 && listStudent[j][8][0] < 15){
                            td.innerHTML='B+'
                        }else if(listStudent[j][8][0] >= 13 && listStudent[j][8][0] < 14){
                            td.innerHTML='B'
                        }else if(listStudent[j][8][0] >= 12 && listStudent[j][8][0] < 13){
                            td.innerHTML='B-'
                        }else if(listStudent[j][8][0] >= 11 && listStudent[j][8][0] < 12){
                            td.innerHTML='C+'
                        }else if(listStudent[j][8][0] >= 10 && listStudent[j][8][0] < 11){
                            td.innerHTML='C'
                        }else if(listStudent[j][8][0] >= 9 && listStudent[j][8][0] < 10){
                            td.innerHTML='C-'
                        }else if(listStudent[j][8][0] >= 8 && listStudent[j][8][0] < 9){
                            td.innerHTML='D+'
                        }else if(listStudent[j][8][0] >= 7 && listStudent[j][8][0] < 8){
                            td.innerHTML='D'
                        }else if(listStudent[j][8][0] >= 6 && listStudent[j][8][0] < 7){
                            td.innerHTML='E'
                        }else if(listStudent[j][8][0] >= 0 && listStudent[j][8][0] < 6){
                            td.innerHTML='F'
                        }
                    }

                    if(i==8){
                        if(listStudent[j][9][0] >= 16){
                            td.innerHTML='A'
                        }else if(listStudent[j][9][0] >= 15 && listStudent[j][9][0] < 16){
                            td.innerHTML='A-'
                        }else if(listStudent[j][9][0] >= 14 && listStudent[j][9][0] < 15){
                            td.innerHTML='B+'
                        }else if(listStudent[j][9][0] >= 13 && listStudent[j][9][0] < 14){
                            td.innerHTML='B'
                        }else if(listStudent[j][9][0] >= 12 && listStudent[j][9][0] < 13){
                            td.innerHTML='B-'
                        }else if(listStudent[j][9][0] >= 11 && listStudent[j][9][0] < 12){
                            td.innerHTML='C+'
                        }else if(listStudent[j][9][0] >= 10 && listStudent[j][9][0] < 11){
                            td.innerHTML='C'
                        }else if(listStudent[j][9][0] >= 9 && listStudent[j][9][0] < 10){
                            td.innerHTML='C-'
                        }else if(listStudent[j][9][0] >= 8 && listStudent[j][9][0] < 9){
                            td.innerHTML='D+'
                        }else if(listStudent[j][9][0] >= 7 && listStudent[j][9][0] < 8){
                            td.innerHTML='D'
                        }else if(listStudent[j][9][0] >= 6 && listStudent[j][9][0] < 7){
                            td.innerHTML='E'
                        }else if(listStudent[j][9][0] >= 0 && listStudent[j][9][0] < 6){
                            td.innerHTML='F'
                        }
                    }

                    if(i==9){
                        if(listStudent[j][10][0]>= 16){
                            td.innerHTML='A'
                        }else if(listStudent[j][10][0]>= 15 && listStudent[j][10][0]< 16){
                            td.innerHTML='A-'
                        }else if(listStudent[j][10][0]>= 14 && listStudent[j][10][0]< 15){
                            td.innerHTML='B+'
                        }else if(listStudent[j][10][0]>= 13 && listStudent[j][10][0]< 14){
                            td.innerHTML='B'
                        }else if(listStudent[j][10][0]>= 12 && listStudent[j][10][0]< 13){
                            td.innerHTML='B-'
                        }else if(listStudent[j][10][0]>= 11 && listStudent[j][10][0]< 12){
                            td.innerHTML='C+'
                        }else if(listStudent[j][10][0]>= 10 && listStudent[j][10][0]< 11){
                            td.innerHTML='C'
                        }else if(listStudent[j][10][0]>= 9 && listStudent[j][10][0]< 10){
                            td.innerHTML='C-'
                        }else if(listStudent[j][10][0]>= 8 && listStudent[j][10][0]< 9){
                            td.innerHTML='D+'
                        }else if(listStudent[j][10][0]>= 7 && listStudent[j][10][0]< 8){
                            td.innerHTML='D'
                        }else if(listStudent[j][10][0]>= 6 && listStudent[j][10][0]< 7){
                            td.innerHTML='E'
                        }else if(listStudent[j][10][0]>= 0 && listStudent[j][10][0] < 6){
                            td.innerHTML='F'
                        }
                    }
                }

                line.appendChild(td)
            }
            tab.children[1].appendChild(line)

        }

        //Tableau des stats
        tabstat = clone.children[2].children[1]

        ligneStat1 = tabstat.children[0].children[1].children[0]
        ligneStat1.children[1]
        ligneStat1.children[2]
        ligneStat1.children[3]
        ligneStat1.children[4]

        ligneStat2 = tabstat.children[0].children[1].children[1]

        ligneStat3 = tabstat.children[0].children[1].children[2]

        ligneStat4 = tabstat.children[0].children[1].children[3]

        if(1==0){
            //Ligne 1
            ligneStat1.children[1].innerHTML=mydata[1].length
            ligneStat1.children[4].innerHTML=mydata[7][0]['Passable']
            ligneStat1.children[5].innerHTML=`${(mydata[7][0]['pourcentageP'])} %`
            //Ligne2
            ligneStat2.children[1].innerHTML=mydata[6][0]['nombre']
            ligneStat2.children[2].innerHTML= `${(mydata[6][0]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML=mydata[7][0]['Assez Bien']
            ligneStat2.children[5].innerHTML=`${(mydata[7][0]['pourcentageAB'])} %`
            //Ligne3
            ligneStat3.children[1].innerHTML=mydata[1].length-mydata[6][0]['nombre']
            ligneStat3.children[2].innerHTML=`${ floatfix(mydata[6][0]['pourcentage']) } %`

            ligneStat3.children[4].innerHTML=mydata[7][0]['Bien']
            ligneStat3.children[5].innerHTML=`${(mydata[7][0]['pourcentageB'])} %`
            //Ligne4
            ligneStat4.children[4].innerHTML=mydata[7][0]['Très Bien']
            ligneStat4.children[5].innerHTML=`${(mydata[7][0]['pourcentageTB'])} %`
        }
        if(i==1){
            //Ligne 1
            ligneStat1.children[1].innerHTML=mydata[1].length
            ligneStat1.children[4].innerHTML=mydata[7][1]['Passable']
            ligneStat1.children[5].innerHTML=`${(mydata[7][1]['pourcentageP'])} %`
            //Ligne2
            ligneStat2.children[1].innerHTML=mydata[6][1]['nombre']
            ligneStat2.children[2].innerHTML= `${(mydata[6][1]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML=mydata[7][1]['Assez Bien']
            ligneStat2.children[5].innerHTML=`${(mydata[7][1]['pourcentageAB'])} %`
            //Ligne3
            ligneStat3.children[1].innerHTML=mydata[1].length-mydata[6][1]['nombre']
            ligneStat3.children[2].innerHTML=`${ floatfix(mydata[6][1]['pourcentage'])/*(100-(mydata[6][1]['pourcentage']))*/ } %`

            ligneStat3.children[4].innerHTML=mydata[7][1]['Bien']
            ligneStat3.children[5].innerHTML=`${(mydata[7][1]['pourcentageB'])} %`
            //Ligne4
            ligneStat4.children[4].innerHTML=mydata[7][1]['Très Bien']
            ligneStat4.children[5].innerHTML=`${(mydata[7][1]['pourcentageTB'])} %`
        }
        if(i==2){
            //Ligne 1
            ligneStat1.children[1].innerHTML=mydata[1].length
            ligneStat1.children[4].innerHTML=mydata[7][2]['Passable']
            ligneStat1.children[5].innerHTML=`${(mydata[7][2]['pourcentageP'])} %`
            //Ligne2
            ligneStat2.children[1].innerHTML=mydata[6][2]['nombre']
            ligneStat2.children[2].innerHTML= `${(mydata[6][2]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML=mydata[7][2]['Assez Bien']
            ligneStat2.children[5].innerHTML=`${(mydata[7][2]['pourcentageAB'])} %`
            //Ligne3
            ligneStat3.children[1].innerHTML=mydata[1].length-mydata[6][2]['nombre']
            ligneStat3.children[2].innerHTML=`${ floatfix(mydata[6][2]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML=mydata[7][2]['Bien']
            ligneStat3.children[5].innerHTML=`${(mydata[7][2]['pourcentageB'])} %`
            //Ligne4
            ligneStat4.children[4].innerHTML=mydata[7][2]['Très Bien']
            ligneStat4.children[5].innerHTML=`${(mydata[7][2]['pourcentageTB'])} %`
        }
        if(i==3){
            //Ligne 1
            ligneStat1.children[1].innerHTML=mydata[1].length
            ligneStat1.children[4].innerHTML=mydata[7][3]['Passable']
            ligneStat1.children[5].innerHTML=`${(mydata[7][3]['pourcentageP'])} %`
            //Ligne2
            ligneStat2.children[1].innerHTML=mydata[6][3]['nombre']
            ligneStat2.children[2].innerHTML= `${(mydata[6][3]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML=mydata[7][3]['Assez Bien']
            ligneStat2.children[5].innerHTML=`${(mydata[7][3]['pourcentageAB'])} %`
            //Ligne3
            ligneStat3.children[1].innerHTML=mydata[1].length-mydata[6][3]['nombre']
            ligneStat3.children[2].innerHTML=`${floatfix(mydata[6][3]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML=mydata[7][3]['Bien']
            ligneStat3.children[5].innerHTML=`${(mydata[7][3]['pourcentageB'])} %`
            //Ligne4
            ligneStat4.children[4].innerHTML=mydata[7][3]['Très Bien']
            ligneStat4.children[5].innerHTML=`${(mydata[7][3]['pourcentageTB'])} %`
        }
        if(i==4){
            //Ligne 1
            ligneStat1.children[1].innerHTML=mydata[1].length
            ligneStat1.children[4].innerHTML=mydata[7][4]['Passable']
            ligneStat1.children[5].innerHTML=`${(mydata[7][4]['pourcentageP'])} %`
            //Ligne2
            ligneStat2.children[1].innerHTML=mydata[6][4]['nombre']
            ligneStat2.children[2].innerHTML= `${(mydata[6][4]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML=mydata[7][4]['Assez Bien']
            ligneStat2.children[5].innerHTML=`${(mydata[7][4]['pourcentageAB'])} %`
            //Ligne3
            ligneStat3.children[1].innerHTML=mydata[1].length-mydata[6][4]['nombre']
            ligneStat3.children[2].innerHTML=`${floatfix(mydata[6][4]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML=mydata[7][4]['Bien']
            ligneStat3.children[5].innerHTML=`${(mydata[7][4]['pourcentageB'])} %`
            //Ligne4
            ligneStat4.children[4].innerHTML=mydata[7][4]['Très Bien']
            ligneStat4.children[5].innerHTML=`${(mydata[7][4]['pourcentageTB'])} %`
        }
        if(i==5){
            //Ligne 1
            ligneStat1.children[1].innerHTML=mydata[1].length
            ligneStat1.children[4].innerHTML=mydata[7][5]['Passable']
            ligneStat1.children[5].innerHTML=`${(mydata[7][5]['pourcentageP'])} %`
            //Ligne2
            ligneStat2.children[1].innerHTML=mydata[6][5]['nombre']
            ligneStat2.children[2].innerHTML= `${(mydata[6][5]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML=mydata[7][5]['Assez Bien']
            ligneStat2.children[5].innerHTML=`${(mydata[7][5]['pourcentageAB'])} %`
            //Ligne3
            ligneStat3.children[1].innerHTML=mydata[1].length-mydata[6][5]['nombre']
            ligneStat3.children[2].innerHTML=`${floatfix(mydata[6][5]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML=mydata[7][5]['Bien']
            ligneStat3.children[5].innerHTML=`${(mydata[7][5]['pourcentageB'])} %`
            //Ligne4
            ligneStat4.children[4].innerHTML=mydata[7][5]['Très Bien']
            ligneStat4.children[5].innerHTML=`${(mydata[7][5]['pourcentageTB'])} %`
        }
        if(i==6){
            //Ligne 1
            ligneStat1.children[1].innerHTML=mydata[1].length
            ligneStat1.children[4].innerHTML=mydata[7][6]['Passable']
            ligneStat1.children[5].innerHTML=`${(mydata[7][6]['pourcentageP'])} %`
            //Ligne2
            ligneStat2.children[1].innerHTML=mydata[6][6]['nombre']
            ligneStat2.children[2].innerHTML= `${(mydata[6][6]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML=mydata[7][6]['Assez Bien']
            ligneStat2.children[5].innerHTML=`${(mydata[7][6]['pourcentageAB'])} %`
            //Ligne3
            ligneStat3.children[1].innerHTML=mydata[1].length-mydata[6][6]['nombre']
            ligneStat3.children[2].innerHTML=`${floatfix(mydata[6][6]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML=mydata[7][6]['Bien']
            ligneStat3.children[5].innerHTML=`${(mydata[7][6]['pourcentageB'])} %`
            //Ligne4
            ligneStat4.children[4].innerHTML=mydata[7][6]['Très Bien']
            ligneStat4.children[5].innerHTML=`${(mydata[7][6]['pourcentageTB'])} %`
        }
        if(i==7){
            //Ligne 1
            ligneStat1.children[1].innerHTML=mydata[1].length
            ligneStat1.children[4].innerHTML=mydata[7][7]['Passable']
            ligneStat1.children[5].innerHTML=`${(mydata[7][7]['pourcentageP'])} %`
            //Ligne2
            ligneStat2.children[1].innerHTML=mydata[6][7]['nombre']
            ligneStat2.children[2].innerHTML= `${(mydata[6][7]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML=mydata[7][7]['Assez Bien']
            ligneStat2.children[5].innerHTML=`${(mydata[7][7]['pourcentageAB'])} %`
            //Ligne3
            ligneStat3.children[1].innerHTML=mydata[1].length-mydata[6][7]['nombre']
            ligneStat3.children[2].innerHTML=`${floatfix(mydata[6][7]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML=mydata[7][7]['Bien']
            ligneStat3.children[5].innerHTML=`${(mydata[7][7]['pourcentageB'])} %`
            //Ligne4
            ligneStat4.children[4].innerHTML=mydata[7][7]['Très Bien']
            ligneStat4.children[5].innerHTML=`${(mydata[7][7]['pourcentageTB'])} %`
        }
        if(i==8){
            //Ligne 1
            ligneStat1.children[1].innerHTML=mydata[1].length
            ligneStat1.children[4].innerHTML=mydata[7][8]['Passable']
            ligneStat1.children[5].innerHTML=`${(mydata[7][8]['pourcentageP'])} %`
            //Ligne2
            ligneStat2.children[1].innerHTML=mydata[6][8]['nombre']
            ligneStat2.children[2].innerHTML= `${(mydata[6][8]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML=mydata[7][8]['Assez Bien']
            ligneStat2.children[5].innerHTML=`${(mydata[7][8]['pourcentageAB'])} %`
            //Ligne3
            ligneStat3.children[1].innerHTML=mydata[1].length-mydata[6][8]['nombre']
            ligneStat3.children[2].innerHTML=`${floatfix(mydata[6][8]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML=mydata[7][8]['Bien']
            ligneStat3.children[5].innerHTML=`${(mydata[7][8]['pourcentageB'])} %`
            //Ligne4
            ligneStat4.children[4].innerHTML=mydata[7][8]['Très Bien']
            ligneStat4.children[5].innerHTML=`${(mydata[7][8]['pourcentageTB'])} %`
        }
        if(i==9){
            //Ligne 1
            ligneStat1.children[1].innerHTML=mydata[1].length
            ligneStat1.children[4].innerHTML=mydata[7][9]['Passable']
            ligneStat1.children[5].innerHTML=`${(mydata[7][9]['pourcentageP'])} %`
            //Ligne2
            ligneStat2.children[1].innerHTML=mydata[6][9]['nombre']
            ligneStat2.children[2].innerHTML= `${(mydata[6][9]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML=mydata[7][9]['Assez Bien']
            ligneStat2.children[5].innerHTML=`${(mydata[7][9]['pourcentageAB'])} %`
            //Ligne3
            ligneStat3.children[1].innerHTML=mydata[1].length-mydata[6][9]['nombre']
            ligneStat3.children[2].innerHTML=`${floatfix(mydata[6][9]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML=mydata[7][9]['Bien']
            ligneStat3.children[5].innerHTML=`${(mydata[7][9]['pourcentageB'])} %`
            //Ligne4
            ligneStat4.children[4].innerHTML=mydata[7][9]['Très Bien']
            ligneStat4.children[5].innerHTML=`${(mydata[7][9]['pourcentageTB'])} %`
        }

        return (clone)
    }

    ListProcess()
})


function floatfix(a){
    return (100 - a).toFixed(2)
} 