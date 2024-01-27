window.addEventListener('load', () => {
    //Recuperation de la variable des données
    mydata = JSON.parse(document.getElementById('semestre1MDS').textContent);
    console.log(mydata)

    function Page1_2() {
        listStudent = mydata[1]

        page0 = document.getElementById('page')
        page0 = page0.cloneNode(true)

        bigtab = page0.children[0].children[2].children[1]

        page = document.getElementById("part2")
        page = page.cloneNode(true)

        bigtab1 = page.children[0].children[1].children[1]

        //Tableau Sur lequel on ajoute les nouvelles lignes
        worktab = bigtab.children[1]
        worktab1 = bigtab1.children[1]
            //Ligne des 4 tableaux

        for (i = 0; i <= mydata[1].length - 1; i++) {

            temp = worktab.children[3].cloneNode(true)
            temp1 = worktab1.children[3].cloneNode(true)

            //tab0
            tab0 = temp.children[0]
            tab01 = tab0.children.nested4
            tab02 = tab01.children
            tab03 = tab02['0']
            tab04 = tab03.children
            tab05 = tab04[0] //good  
                ////
            tab00 = temp1.children[0]
            tab001 = tab00.children.nested4
            tab002 = tab001.children
            tab003 = tab002['0']
            tab004 = tab003.children
            tab005 = tab004[0] //good*/

            for (j = 0; j <= tab05.childElementCount - 1; j++) {
                if (j == 0) {
                    tab05.cells[j].innerHTML = i + 1;

                    tab005.cells[j].innerHTML = i + 1;
                }
                if (j == 1) {
                    tab05.cells[j].innerHTML = listStudent[i][0]['nom'];
                    tab005.cells[j].innerHTML = listStudent[i][0]['nom'];
                }
                if (j == 2) {
                    tab05.cells[j].innerHTML = listStudent[i][0]['prenom'];
                    tab005.cells[j].innerHTML = listStudent[i][0]['prenom']
                }
                if (j == 3) {
                    tab05.cells[j].innerHTML = listStudent[i][0]['matricule'];
                    tab005.cells[j].innerHTML = listStudent[i][0]['matricule']
                        //tab005.cells[j].innerHTML = listStudent[i][0]['date_naissance']
                }
            }

            //tab0 Page2


            //tab1 UE FONDAMENTALES
            tab1 = temp.children[1]
            tab11 = tab1.children.nested11
            tab12 = tab11.children
            tab13 = tab12['0']
            tab14 = tab13.children
            tab15 = tab14[0] //good line
                //
            tab111 = temp1.children[1]
            tab112 = tab111.children.nested11
            tab113 = tab112.children
            tab114 = tab113['0']
            tab115 = tab114.children
            tab116 = tab115['0'] //good line*/

            

            for (j = 0; j <= tab15.childElementCount - 1; j++) {
                if (j == 0) {
                    tab15.cells[j].innerHTML = listStudent[i][1][0];
                }
                if (j == 1) {
                    tab15.cells[j].innerHTML = listStudent[i][2][0];
                }
                if (j == 2) {

                    var uef1cr = listStudent[i][1][7]
                    //if (listStudent[i][1][0] < 10) { uef1cr = 0 } //else { uef1cr = ] }

                    var uef2cr = listStudent[i][2][7]
                    //if (listStudent[i][2][0] < 10) { uef2cr = 0 } //else { uef2cr = listStudent[i][2][7] }

                    moyuef = listStudent[i][1][3]

                    if (moyuef >= 10 && (listStudent[i][1][0] >= 7 && listStudent[i][2][0] >= 7)) {
                        //console.log('OK');
                        moyuefcr = uef1cr + uef2cr//listStudent[i][1][6] + listStudent[i][2][6]
                    } else {
                        moyuef = '--'
                        moyuefcr = uef1cr + uef2cr
                    }
                    tab15.cells[j].innerHTML = moyuef //listStudent[i][1][3];


                    tab116.cells[j].innerHTML = listStudent[i][1][7] + listStudent[i][2][7] + listStudent[i][3][7] + listStudent[i][4][7] + listStudent[i][5][7] + listStudent[i][9][7] + listStudent[i][10][7] + listStudent[i][11][7] + listStudent[i][12][7] //Crédits
                        //tab116.cells[j].innerHTML = ""
                }
                if (j == 3) {
                    tab15.cells[j].innerHTML = moyuefcr


                    //tab116.cells[j].innerHTML = mydata[2].indexOf(listStudent[i][13][2]) + 1 //rang
                }

                //tab116.cells[4].innerHTML = "--" //tab 116 renvoit au tableau des résultats
            }



            //tab2 UE PROFESSIONNELLES
            tab2 = temp.children[2]
            tab21 = tab2.children.nested22
            tab22 = tab21.children['0']
            tab23 = tab22.children['0']

            for (j = 0; j <= tab23.childElementCount - 1; j++) {
                if (j == 0) { tab23.cells[j].innerHTML = listStudent[i][3][0] };
                if (j == 1) { tab23.cells[j].innerHTML = listStudent[i][4][0] }; //{if(listStudent[i][3][5]){tab23.cells[j].innerHTML ='V'}else{tab23.cells[j].innerHTML ='NV'}};
                if (j == 2) { tab23.cells[j].innerHTML = listStudent[i][5][0] };
                if (j == 3) { tab23.cells[j].innerHTML = listStudent[i][6][0] }; //{{if(listStudent[i][4][5]){tab23.cells[j].innerHTML ='V'}else{tab23.cells[j].innerHTML ='NV'}};};
                if (j == 4) { tab23.cells[j].innerHTML = listStudent[i][7][0] };
                if (j == 5) { tab23.cells[j].innerHTML = listStudent[i][8][0] };
                if (j == 6) { tab23.cells[j].innerHTML = listStudent[i][9][0] };

                if (j == 7) {
                    eps125Somme = (listStudent[i][5][0] + listStudent[i][6][0] + listStudent[i][7][0] + listStudent[i][8][0]) / (4)

                    var uef3cr = listStudent[i][3][6]
                    if (listStudent[i][3][0] < 10) { uef3cr = 0 }

                    var uef4cr = listStudent[i][4][6]
                    if (listStudent[i][4][0] < 10) { uef4cr = 0 }

                    var uef5cr = listStudent[i][5][6]
                    if (listStudent[i][5][5] == false) { uef5cr = 0 }

                    var uef9cr = listStudent[i][9][6]
                    if (listStudent[i][9][0] < 10) { uef9cr = 0 }

                    moyuep = listStudent[i][3][3]
                    moyuepcr = 0

                    if (moyuep >= 10 && (listStudent[i][3][0] >= 7 && listStudent[i][4][0] >= 7 && eps125Somme >= 7 && listStudent[i][9][0] >= 7)) {
                        console.log('OK');
                        moyuepcr = listStudent[i][3][6] + listStudent[i][4][6] + listStudent[i][5][7] + listStudent[i][9][6]
                    } else {
                        moyuep = '--'
                        moyuepcr = uef3cr + uef4cr + uef5cr + uef9cr
                    }


                    tab23.cells[j].innerHTML = moyuep //listStudent[i][3][3]
                };
                if (j == 8) { tab23.cells[j].innerHTML = moyuepcr /*if (listStudent[i][3][3] >= 10) { tab23.cells[j].innerHTML = 'V' } else { tab23.cells[j].innerHTML = 'NV' }*/ };

            }

            //tab3 UE TRANSVERSALES
            tab3 = temp.children[3]
            tab31 = tab3.children.nested33
            tab32 = tab31.children['0']
            tab33 = tab32.children['0']

            for (j = 0; j <= tab33.childElementCount - 1; j++) {
                if (j == 0) { tab33.cells[j].innerHTML = listStudent[i][10][0] };
                if (j == 1) { tab33.cells[j].innerHTML = listStudent[i][11][0] };
                if (j == 2) { tab33.cells[j].innerHTML = listStudent[i][12][0] };

                if (j == 3) {

                    var uef10cr = listStudent[i][10][6]
                    if (listStudent[i][10][0] < 10) { uef10cr = 0 }

                    var uef11cr = listStudent[i][11][6]
                    if (listStudent[i][11][0] < 10) { uef11cr = 0 }

                    var uef12cr = listStudent[i][12][6]
                    if (listStudent[i][12][0] < 10) { uef12cr = 0 }

                    moyuet = listStudent[i][10][3]

                    if (moyuet >= 10 && (listStudent[i][10][0] >= 7 && listStudent[i][11][0] >= 7 && listStudent[i][12][0] >= 7)) {
                        //console.log('OK');
                        moyuetcr = listStudent[i][10][6] + listStudent[i][11][6] + listStudent[i][12][6]
                    } else {
                        moyuet = '--'
                        moyuetcr = uef10cr + uef11cr + uef12cr
                    }

                    tab33.cells[j].innerHTML = moyuet
                };

                if (j == 4) {
                    tab33.cells[j].innerHTML = moyuetcr
                }

                //Ajoute de la ligne au grand tableau
                /* worktab.appendChild(temp)
                 worktab1.appendChild(temp1)*/
            }

            //RESULTATS
            for (j = 0; j <= tab116.childElementCount - 1; j++) {
                if (j == 0) { tab116.cells[j].innerHTML = listStudent[i][13][1]; } //total }
                if (j == 1) { tab116.cells[j].innerHTML = listStudent[i][13][2]; } //moyenne }
                if (j == 2) { tab116.cells[j].innerHTML = moyuefcr + moyuepcr + moyuetcr } //moyuefcr + moyuepcr + moyuetcr
                if (j == 3) { tab116.cells[j].innerHTML = mydata[2].indexOf(listStudent[i][13][2]) + 1 } //rang }
                if (j == 4) { tab116.cells[j].innerHTML = "--" }
            }


            //Ajoute de la ligne au grand tableau
            worktab.appendChild(temp)
            worktab1.appendChild(temp1)

            body.appendChild(page0)
            body.appendChild(page)
        }

    }
    Page1_2()


    function PageRattrapage() {
        listStudent = mydata[1]

        page2 = document.getElementById('page')
        page2 = page2.cloneNode(true)
            //Changement Title
        page2.children[0].children[2].children[0].innerHTML = "PROCES VERBAL MODULAIRE RATTRAPAGE 2<sup>eme</sup> SEMESTRE EPS1  2022-2023"

        bigtab2 = page2.children[0].children[2].children[1]

        page3 = document.getElementById("part2")
        page3 = page3.cloneNode(true)
            //Changement Title
        page3.children[0].children[1].children[0].innerHTML = "PROCES VERBAL MODULAIRE RATTRAPAGE 2<sup>eme</sup> SEMESTRE EPS1  2022-2023"

        bigtab3 = page3.children[0].children[1].children[1]

        //Tableau Sur lequel on ajoute les nouvelles lignes
        worktab2 = bigtab2.children[1]
        worktab3 = bigtab3.children[1]

        for (i = 0; i <= mydata[1].length - 1; i++) {

            temp2 = worktab2.children[3].cloneNode(true)
            temp3 = worktab3.children[3].cloneNode(true)

            //tab0 NOMS ET INFOS ETUDIANTS
            tab0 = temp2.children[0]
            tab01 = tab0.children.nested4
            tab02 = tab01.children
            tab03 = tab02['0']
            tab04 = tab03.children
            tab05 = tab04[0] //good  
                ////
            tab00 = temp3.children[0]
            tab001 = tab00.children.nested4
            tab002 = tab001.children
            tab003 = tab002['0']
            tab004 = tab003.children
            tab005 = tab004[0] //good*/

            for (j = 0; j <= tab05.childElementCount - 1; j++) {
                if (j == 0) {
                    tab05.cells[j].innerHTML = i + 1;

                    tab005.cells[j].innerHTML = i + 1;
                }
                if (j == 1) {
                    tab05.cells[j].innerHTML = listStudent[i][0]['nom'];
                    tab005.cells[j].innerHTML = listStudent[i][0]['nom'];
                }
                if (j == 2) {
                    tab05.cells[j].innerHTML = listStudent[i][0]['prenom'];
                    tab005.cells[j].innerHTML = listStudent[i][0]['prenom']
                }
                if (j == 3) {
                    tab05.cells[j].innerHTML = listStudent[i][0]['matricule'];
                    tab005.cells[j].innerHTML = listStudent[i][0]['matricule']
                        //tab005.cells[j].innerHTML = listStudent[i][0]['date_naissance']
                }
            }


            //tab1 UE FONDAMENTALES
            tab1 = temp2.children[1]
            tab11 = tab1.children.nested11
            tab12 = tab11.children
            tab13 = tab12['0']
            tab14 = tab13.children
            tab15 = tab14[0] //good line
                ///
            tab111 = temp3.children[1]
            tab112 = tab111.children.nested11
            tab113 = tab112.children
            tab114 = tab113['0']
            tab115 = tab114.children
            tab116 = tab115['0'] //good line*/

            for (j = 0; j <= tab15.childElementCount - 1; j++) {
                if (j == 0) {
                    tab15.cells[j].innerHTML = '--' //listStudent[i][1][0];
                }
                if (j == 1) {
                    tab15.cells[j].innerHTML = '--' //listStudent[i][2][0];
                }
                if (j == 2) {

                    /*var uef1cr = listStudent[i][1][6]
                    if (listStudent[i][1][0] < 10) { uef1cr = 0 } 

                    var uef2cr = listStudent[i][2][6]
                    if (listStudent[i][2][0] < 10) { uef2cr = 0 } 

                    moyuef = listStudent[i][1][3]

                    if (moyuef >= 10 && (listStudent[i][1][0] >= 7 && listStudent[i][2][0] >= 7)) {
                        moyuefcr = listStudent[i][1][6] + listStudent[i][2][6]
                    } else {
                        moyuef = '--'
                        moyuefcr = uef1cr + uef2cr
                    }*/
                    tab15.cells[j].innerHTML = '--' /*moyuef */


                    tab116.cells[j].innerHTML = '--' //Crédits
                }
                if (j == 3) {
                    tab15.cells[j].innerHTML = moyuefcr


                    tab116.cells[j].innerHTML = '--' //mydata[2].indexOf(listStudent[i][13][2]) + 1 //rang
                }

                tab116.cells[4].innerHTML = "--" //tab 116 renvoit au tableau des résultats
            }

            //tab2 UE PROFESSIONNELLES
            tab2 = temp2.children[2]
            tab21 = tab2.children.nested22
            tab22 = tab21.children['0']
            tab23 = tab22.children['0']

            for (j = 0; j <= tab23.childElementCount - 1; j++) {
                if (j == 0) { tab23.cells[j].innerHTML = '--' /*listStudent[i][3][0]*/ };
                if (j == 1) { tab23.cells[j].innerHTML = '--' /*listStudent[i][4][0]*/ }; //{if(listStudent[i][3][5]){tab23.cells[j].innerHTML ='V'}else{tab23.cells[j].innerHTML ='NV'}};
                if (j == 2) { tab23.cells[j].innerHTML = '--' /*listStudent[i][5][0]*/ };
                if (j == 3) { tab23.cells[j].innerHTML = '--' /*listStudent[i][6][0]*/ }; //{{if(listStudent[i][4][5]){tab23.cells[j].innerHTML ='V'}else{tab23.cells[j].innerHTML ='NV'}};};
                if (j == 4) { tab23.cells[j].innerHTML = '--' /*listStudent[i][7][0]*/ };
                if (j == 5) { tab23.cells[j].innerHTML = '--' /*listStudent[i][8][0]*/ };
                if (j == 6) { tab23.cells[j].innerHTML = '--' /*listStudent[i][9][0]*/ };

                if (j == 7) {
                    /*eps125Somme = (listStudent[i][5][0] + listStudent[i][6][0] + listStudent[i][7][0] + listStudent[i][8][0]) / (4)

                    var uef3cr = listStudent[i][3][6]
                    if (listStudent[i][3][0] < 10) { uef3cr = 0 }

                    var uef4cr = listStudent[i][4][6]
                    if (listStudent[i][4][0] < 10) { uef4cr = 0 }

                    var uef5cr = listStudent[i][5][6]
                    if (listStudent[i][5][5] == false) { uef5cr = 0 }

                    var uef9cr = listStudent[i][9][6]
                    if (listStudent[i][9][0] < 10) { uef9cr = 0 }

                    moyuep = listStudent[i][3][3]
                    moyuepcr = 

                    if (moyuep >= 10 && (listStudent[i][3][0] >= 7 && listStudent[i][4][0] >= 7 && eps125Somme >= 7 && listStudent[i][9][0] >= 7)) {
                        console.log('OK');
                        moyuepcr = listStudent[i][3][6] + listStudent[i][4][6] + listStudent[i][5][7] + listStudent[i][9][6]
                    } else {
                        moyuep = '--'
                        moyuepcr = uef3cr + uef4cr + uef5cr + uef9cr
                    }*/


                    tab23.cells[j].innerHTML = '--' //moyuep //listStudent[i][3][3]
                };
                if (j == 8) { tab23.cells[j].innerHTML = '--' } //moyuepcr /*if (listStudent[i][3][3] >= 10) { tab23.cells[j].innerHTML = 'V' } else { tab23.cells[j].innerHTML = 'NV' }*/ };

            }



            //Ajoute de la ligne au grand tableau
            worktab2.appendChild(temp2)
            worktab3.appendChild(temp3)

            body.appendChild(page2)
            body.appendChild(page3)
        }
    }
    PageRattrapage()


    function PageSynthese() {
        synthese = mydata[10][0]

        page4 = document.getElementById('page')
        page4 = page4.cloneNode(true)
            //Changement Title
        page4.children[0].children[2].children[0].innerHTML = "PROCES VERBAL MODULAIRE SYNTHESE 2<sup>eme</sup> SEMESTRE EPS1  2022-2023"

        bigtab4 = page4.children[0].children[2].children[1]

        page5 = document.getElementById("part2")
        page5 = page5.cloneNode(true)
            //Changement Title
        page5.children[0].children[1].children[0].innerHTML = "PROCES VERBAL MODULAIRE SYNTHESE 2<sup>eme</sup> SEMESTRE EPS1  2022-2023"

        bigtab5 = page5.children[0].children[1].children[1]

        //Tableau Sur lequel on ajoute les nouvelles lignes
        worktab2 = bigtab4.children[1]
        worktab3 = bigtab5.children[1]

        for (i = 0; i <= mydata[1].length - 1; i++) {

            temp4 = worktab2.children[3].cloneNode(true)
            temp5 = worktab3.children[3].cloneNode(true)

            //tab0 NOMS ET INFOS ETUDIANTS
            tab0 = temp4.children[0]
            tab01 = tab0.children.nested4
            tab02 = tab01.children
            tab03 = tab02['0']
            tab04 = tab03.children
            tab05 = tab04[0] //good  
                ////
            tab00 = temp5.children[0]
            tab001 = tab00.children.nested4
            tab002 = tab001.children
            tab003 = tab002['0']
            tab004 = tab003.children
            tab005 = tab004[0] //good*/

            for (j = 0; j <= tab05.childElementCount - 1; j++) {
                if (j == 0) {
                    tab05.cells[j].innerHTML = i + 1;

                    tab005.cells[j].innerHTML = i + 1;
                }
                if (j == 1) {
                    tab05.cells[j].innerHTML = synthese[i][0]['nom'];
                    tab005.cells[j].innerHTML = synthese[i][0]['nom'];
                }
                if (j == 2) {
                    tab05.cells[j].innerHTML = synthese[i][0]['prenom'];
                    tab005.cells[j].innerHTML = synthese[i][0]['prenom']
                }
                if (j == 3) {
                    tab05.cells[j].innerHTML = synthese[i][0]['matricule'];
                    tab005.cells[j].innerHTML = synthese[i][0]['matricule']
                        //tab005.cells[j].innerHTML = listStudent[i][0]['date_naissance']
                }
            }

            //tab1 UE FONDAMENTALES
            tab1 = temp4.children[1]
            tab11 = tab1.children.nested11
            tab12 = tab11.children
            tab13 = tab12['0']
            tab14 = tab13.children
            tab15 = tab14[0] //good line

            tab111 = temp5.children[1]
            tab112 = tab111.children.nested11
            tab113 = tab112.children
            tab114 = tab113['0']
            tab115 = tab114.children
            tab116 = tab115['0'] //good line*/

            for (j = 0; j <= tab15.childElementCount - 1; j++) {
                if (j == 0) {
                    tab15.cells[j].innerHTML = synthese[i][1][0];
                }
                if (j == 1) {
                    tab15.cells[j].innerHTML = synthese[i][2][0];
                }
                if (j == 2) {

                    var uef1cr = synthese[i][1][7]
                    //if (synthese[i][1][0] < 10) { uef1cr = 0 } //else { uef1cr = ] }

                    var uef2cr = synthese[i][2][7]
                    //if (synthese[i][2][0] < 10) { uef2cr = 0 } //else { uef2cr = synthese[i][2][7] }

                    moyuef = synthese[i][1][3]

                    if (moyuef >= 10 && (synthese[i][1][0] >= 7 && synthese[i][2][0] >= 7)) {
                        //console.log('OK');
                        //moyuefcr = synthese[i][1][6] + synthese[i][2][6]
                        moyuefcr = uef1cr + uef2cr
                    } else {
                        moyuef = '--'
                        moyuefcr = uef1cr + uef2cr
                    }
                    tab15.cells[j].innerHTML = moyuef //synthese[i][1][3];


                    tab116.cells[j].innerHTML = synthese[i][1][7] + synthese[i][2][7] + synthese[i][3][7] + synthese[i][4][7] + synthese[i][5][7] + synthese[i][9][7] + synthese[i][10][7] + synthese[i][11][7] + synthese[i][12][7] //Crédits
                        //tab116.cells[j].innerHTML = ""
                }
                if (j == 3) {
                    tab15.cells[j].innerHTML = moyuefcr


                    //tab116.cells[j].innerHTML = mydata[2].indexOf(synthese[i][13][2]) + 1 //rang
                }

                //tab116.cells[4].innerHTML = "--" //tab 116 renvoit au tableau des résultats
            }

            //tab2 UE PROFESSIONNELLES
            tab2 = temp4.children[2]
            tab21 = tab2.children.nested22
            tab22 = tab21.children['0']
            tab23 = tab22.children['0']

            for (j = 0; j <= tab23.childElementCount - 1; j++) {
                if (j == 0) { tab23.cells[j].innerHTML = synthese[i][3][0] };
                if (j == 1) { tab23.cells[j].innerHTML = synthese[i][4][0] }; //{if(synthese[i][3][5]){tab23.cells[j].innerHTML ='V'}else{tab23.cells[j].innerHTML ='NV'}};
                if (j == 2) { tab23.cells[j].innerHTML = synthese[i][5][0] };
                if (j == 3) { tab23.cells[j].innerHTML = synthese[i][6][0] }; //{{if(synthese[i][4][5]){tab23.cells[j].innerHTML ='V'}else{tab23.cells[j].innerHTML ='NV'}};};
                if (j == 4) { tab23.cells[j].innerHTML = synthese[i][7][0] };
                if (j == 5) { tab23.cells[j].innerHTML = synthese[i][8][0] };
                if (j == 6) { tab23.cells[j].innerHTML = synthese[i][9][0] };

                if (j == 7) {
                    eps125Somme = (synthese[i][5][0] + synthese[i][6][0] + synthese[i][7][0] + synthese[i][8][0]) / (4)

                    var uef3cr = synthese[i][3][7]
                    //if (synthese[i][3][0] < 10) { uef3cr = 0 }

                    var uef4cr = synthese[i][4][7]
                    //if (synthese[i][4][0] < 10) { uef4cr = 0 }

                    var uef5cr = synthese[i][5][7]
                    //if (synthese[i][5][5] == false) { uef5cr = 0 }

                    var uef9cr = synthese[i][9][7]
                    //if (synthese[i][9][0] < 10) { uef9cr = 0 }

                    moyuep = synthese[i][3][3]
                    moyuepcr = 0

                    if (moyuep >= 10 && (synthese[i][3][0] >= 7 && synthese[i][4][0] >= 7 && synthese[i][5][0] >= 7 && synthese[i][6][0] >= 7 &&  synthese[i][7][0] >= 7 &&  synthese[i][8][0] >= 7 && /*eps125Somme >= 7 &&*/ synthese[i][9][0] >= 7)) {
                        //console.log('OK');
                        moyuepcr = uef3cr + uef4cr + uef5cr + uef9cr//synthese[i][3][6] + synthese[i][4][6] + synthese[i][5][7] + synthese[i][9][6]
                    } else {
                        moyuep = '--'
                        moyuepcr = uef3cr + uef4cr + uef5cr + uef9cr
                    }


                    tab23.cells[j].innerHTML = moyuep //synthese[i][3][3]
                };
                if (j == 8) { tab23.cells[j].innerHTML = moyuepcr /*if (synthese[i][3][3] >= 10) { tab23.cells[j].innerHTML = 'V' } else { tab23.cells[j].innerHTML = 'NV' }*/ };

            }

            //tab3 UE TRANSVERSALES
            tab3 = temp4.children[3]
            tab31 = tab3.children.nested33
            tab32 = tab31.children['0']
            tab33 = tab32.children['0']

            for (j = 0; j <= tab33.childElementCount - 1; j++) {
                if (j == 0) { tab33.cells[j].innerHTML = synthese[i][10][0] };
                if (j == 1) { tab33.cells[j].innerHTML = synthese[i][11][0] };
                if (j == 2) { tab33.cells[j].innerHTML = synthese[i][12][0] };

                if (j == 3) {

                    var uef10cr = synthese[i][10][7]
                    //if (synthese[i][10][0] < 10) { uef10cr = 0 }

                    var uef11cr = synthese[i][11][7]
                    //if (synthese[i][11][0] < 10) { uef11cr = 0 }

                    var uef12cr = synthese[i][12][7]
                    //if (synthese[i][12][0] < 10) { uef12cr = 0 }

                    moyuet = synthese[i][10][3]

                    if (moyuet >= 10 && (synthese[i][10][0] >= 7 && synthese[i][11][0] >= 7 && synthese[i][12][0] >= 7)) {
                        //console.log('OK');
                        moyuetcr = synthese[i][10][7] + synthese[i][11][7] + synthese[i][12][7]
                    } else {
                        moyuet = '--'
                        moyuetcr = synthese[i][10][7] + synthese[i][11][7] + synthese[i][12][7]//uef10cr + uef11cr + uef12cr
                    }

                    tab33.cells[j].innerHTML = moyuet
                };

                if (j == 4) {
                    tab33.cells[j].innerHTML = moyuetcr
                }

                //Ajoute de la ligne au grand tableau
                /* worktab.appendChild(temp)
                 worktab1.appendChild(temp1)*/
            }

            //RESULTATS
            for (j = 0; j <= tab116.childElementCount - 1; j++) {
                if (j == 0) { tab116.cells[j].innerHTML = synthese[i][13][1]; } //total }
                if (j == 1) { tab116.cells[j].innerHTML = synthese[i][13][2]; } //moyenne }
                if (j == 2) { tab116.cells[j].innerHTML = synthese[i][13][3]/*moyuefcr + moyuepcr + moyuetcr*/ } //moyuefcr + moyuepcr + moyuetcr
                if (j == 3) { tab116.cells[j].innerHTML = mydata[2].indexOf(synthese[i][13][2]) + 1; } //rang }
                if (j == 4) { tab116.cells[j].innerHTML = "--" }
            }

            //Ajoute de la ligne au grand tableau
            worktab2.appendChild(temp4)
            worktab3.appendChild(temp5)

            body.appendChild(page4)
            body.appendChild(page5)
        }


    }
    PageSynthese()



    /**FUNCTION MULTI_PAGE FOR PROCES VERBAL */
    function ListProcess() {

        body = document.getElementById('body')

        page = document.getElementById('page2')

        listProces = document.createElement('div');

        for (i = 0; i <= 11; i++) {
            clone = page.cloneNode(true)
            clone.style.display = 'block'
            clone = fullfill(clone, i)

            listProces.appendChild(clone)
        }

        //Fixation de ListProcess sur le body de la page
        body.appendChild(listProces)
    }

    function fullfill(clone, i) {
        //Pagination

        pagination = clone.children[3]

        //Line 1

        //Line 2
        line2 = clone.children[1].children[1].children[0]
        line2.children[2].innerHTML = ' EDUCATION PHYSIQUE ET SPORTIVE'
        line2.children[5].innerHTML = '2022/2023'

        //Line 3
        line3 = clone.children[1].children[2].children[0]

        if (i == 0) {
            line3.children[1].innerHTML = mydata[8][0]['code_UE']
            line3.children[2].innerHTML = mydata[8][0]['intitule_UE']
            line3.children[4].innerHTML = mydata[5][0]
            line3.children[6].innerHTML = mydata[8][0]['semestre_id']

            pagination.innerText = `Page ${i+1} / ${mydata[5].length-2}`
        }
        if (i == 1) {
            line3.children[1].innerHTML = mydata[8][1]['code_UE']
            line3.children[2].innerHTML = mydata[8][1]['intitule_UE']
            line3.children[4].innerHTML = mydata[5][1]
            line3.children[6].innerHTML = mydata[8][1]['semestre_id']

            pagination.innerText = `Page ${i+1} / ${mydata[5].length-2}`
        }
        if (i == 2) {
            line3.children[1].innerHTML = mydata[8][2]['code_UE']
            line3.children[2].innerHTML = mydata[8][2]['intitule_UE']
            line3.children[4].innerHTML = mydata[5][2]
            line3.children[6].innerHTML = mydata[8][2]['semestre_id']

            pagination.innerText = `Page ${i+1} / ${mydata[5].length-2}`
        }
        if (i == 3) {
            line3.children[1].innerHTML = mydata[8][3]['code_UE']
            line3.children[2].innerHTML = mydata[8][3]['intitule_UE']
            line3.children[4].innerHTML = mydata[5][3]
            line3.children[6].innerHTML = mydata[8][3]['semestre_id']

            pagination.innerText = `Page ${i+1} / ${mydata[5].length-2}`
        }
        if (i == 4) {
            line3.children[1].innerHTML = mydata[8][4]['code_UE']
            line3.children[2].innerHTML = mydata[8][4]['intitule_UE']
            line3.children[4].innerHTML = mydata[5][4]
            line3.children[6].innerHTML = mydata[8][4]['semestre_id']

            pagination.innerText = `Page ${i+1} / ${mydata[5].length-2}`
        }
        /*if (i == 5) {
            line3.children[1].innerHTML = "EPS125b";
            line3.children[2].innerHTML = "DIDACTIQUE DES APS : BASKET BALL";
            line3.children[4].innerHTML = mydata[5][5]
            line3.children[6].innerHTML = '1'

            pagination.innerText = `Page ${i+1} / ${mydata[5].length}`
        }*/
        if (i == 5) {
            line3.children[1].innerHTML = mydata[8][13]['code_UE']
            line3.children[2].innerHTML = mydata[8][13]['intitule_UE']
            line3.children[4].innerHTML = mydata[5][5]
            line3.children[6].innerHTML = mydata[8][13]['semestre_id']

            pagination.innerText = `Page ${i+1} / ${mydata[5].length-2}`
        }
        if (i == 6) {
            line3.children[1].innerHTML = mydata[8][i]['code_UE']
            line3.children[2].innerHTML = mydata[8][i]['intitule_UE']
            line3.children[4].innerHTML = mydata[5][6]
            line3.children[6].innerHTML = mydata[8][i]['semestre_id']

            pagination.innerText = `Page ${i+1} / ${mydata[5].length-2}`
        }
        /*if (i == 7) {
            line3.children[1].innerHTML = "EPS125l";
            line3.children[2].innerHTML = "DIDACTIQUE DES APS : LUTTE";
            line3.children[4].innerHTML = mydata[5][7]
            line3.children[6].innerHTML = '1'

            pagination.innerText = `Page ${i+1} / ${mydata[5].length}`
        }*/
        if (i == 7) {
            line3.children[1].innerHTML = mydata[8][8]['code_UE']
            line3.children[2].innerHTML = mydata[8][8]['intitule_UE']
            line3.children[4].innerHTML = mydata[5][7]
            line3.children[6].innerHTML = mydata[8][8]['semestre_id']

            pagination.innerText = `Page ${i+1} / ${mydata[5].length-2}`
        }
        if (i == 8) {
            line3.children[1].innerHTML = mydata[8][9]['code_UE']
            line3.children[2].innerHTML = mydata[8][9]['intitule_UE']
            line3.children[4].innerHTML = mydata[5][8]
            line3.children[6].innerHTML = mydata[8][9]['semestre_id']

            pagination.innerText = `Page ${i+1} / ${mydata[5].length-2}`
        }
        if (i == 9) {
            line3.children[1].innerHTML = mydata[8][10]['code_UE']
            line3.children[2].innerHTML = mydata[8][10]['intitule_UE']
            line3.children[4].innerHTML = mydata[5][9]
            line3.children[6].innerHTML = mydata[8][10]['semestre_id']

            pagination.innerText = `Page ${i+1} / ${mydata[5].length-2}`
        }
        if (i == 10) {
            line3.children[1].innerHTML = mydata[8][11]['code_UE']
            line3.children[2].innerHTML = mydata[8][11]['intitule_UE']
            line3.children[4].innerHTML = mydata[5][10]
            line3.children[6].innerHTML = mydata[8][11]['semestre_id']

            pagination.innerText = `Page ${i+1} / ${mydata[5].length-2}`
        }
        if (i == 11) {
            line3.children[1].innerHTML = mydata[8][12]['code_UE']
            line3.children[2].innerHTML = mydata[8][12]['intitule_UE']
            line3.children[4].innerHTML = mydata[5][11]
            line3.children[6].innerHTML = mydata[8][12]['semestre_id']

            pagination.innerText = `Page ${i+1} / ${mydata[5].length-2}`
        }

        //Tableau des students
        tab = clone.children[2].children[0]

        listStudent = mydata[1]

        tableContainer = document.getElementById('tableContainer')


        /**STATS */
        for (j = 0; j <= mydata[1].length - 1; j++) {

            line = document.createElement('tr')

            for (k = 0; k <= 8; k++) {
                td = document.createElement('td')
                if (k == 0) {
                    td.innerHTML = `${j+1}`;
                    td.setAttribute('class', 'numero')
                }
                if (k == 1) {
                    td.innerHTML = `${listStudent[j][0]['matricule']}`
                    td.setAttribute('class', 'matricule')
                }
                if (k == 2) {
                    td.innerHTML = `${listStudent[j][0]['nom']}` + ` ${listStudent[j][0]['prenom']}`;
                    td.setAttribute('class', 'nomprenon')

                }
                if (k == 3) {
                    if (i == 0) { td.innerHTML = `${listStudent[j][1][8]}` }
                    if (i == 1) { td.innerHTML = `${listStudent[j][2][8]}` }
                    if (i == 2) { td.innerHTML = `${listStudent[j][3][8]}` }
                    if (i == 3) { td.innerHTML = `${listStudent[j][4][8]}` }
                    if (i == 4) { td.innerHTML = `${listStudent[j][5][8]}` }
                    if (i == 5) { td.innerHTML = `${listStudent[j][6][8]}` }

                    if (i == 6) { td.innerHTML = `${listStudent[j][7][8]}` }
                    if (i == 7) { td.innerHTML = `${listStudent[j][8][8]}` }
                    if (i == 8) { td.innerHTML = `${listStudent[j][9][8]}` }
                    if (i == 9) { td.innerHTML = `${listStudent[j][10][8]}` }

                    if (i == 10) { td.innerHTML = `${listStudent[j][11][8]}` }
                    if (i == 11) { td.innerHTML = `${listStudent[j][12][8]}` }
                    td.setAttribute('class', 'cc')
                }
                if (k == 4) {
                    if (i == 0) { td.innerHTML = `${listStudent[j][1][9]}` }
                    if (i == 1) { td.innerHTML = `${listStudent[j][2][9]}` }
                    if (i == 2) { td.innerHTML = `${listStudent[j][3][9]}` }
                    if (i == 3) { td.innerHTML = `${listStudent[j][4][9]}` }
                    if (i == 4) { td.innerHTML = `${listStudent[j][5][9]}` }
                    if (i == 5) { td.innerHTML = `${listStudent[j][6][9]}` }
                    if (i == 6) { td.innerHTML = `${listStudent[j][7][9]}` }
                    if (i == 7) { td.innerHTML = `${listStudent[j][8][9]}` }
                    if (i == 8) { td.innerHTML = `${listStudent[j][9][9]}` }
                    if (i == 9) { td.innerHTML = `${listStudent[j][10][9]}` }

                    if (i == 10) { td.innerHTML = `${listStudent[j][11][9]}` }
                    if (i == 11) { td.innerHTML = `${listStudent[j][12][9]}` }
                }
                if (k == 5) {
                    if (i == 0) {
                        td.innerHTML = `${listStudent[j][1][0]}`;
                        td.setAttribute('class', 'moyenne');
                    }
                    if (i == 1) { td.innerHTML = `${listStudent[j][2][0]}` }
                    if (i == 2) { td.innerHTML = `${listStudent[j][3][0]}` }
                    if (i == 3) { td.innerHTML = `${listStudent[j][4][0]}` }
                    if (i == 4) { td.innerHTML = `${listStudent[j][5][0]}` }
                    if (i == 5) { td.innerHTML = `${listStudent[j][6][0]}` }

                    if (i == 6) { td.innerHTML = `${listStudent[j][7][0]}` }
                    if (i == 7) { td.innerHTML = `${listStudent[j][8][0]}` }
                    if (i == 8) { td.innerHTML = `${listStudent[j][9][0]}` }
                    if (i == 9) { td.innerHTML = `${listStudent[j][10][0]}` }

                    if (i == 10) { td.innerHTML = `${listStudent[j][11][0]}` }
                    if (i == 11) { td.innerHTML = `${listStudent[j][12][0]}` }
                }
                if (k == 6) {
                    if (i == 0) {
                        if (listStudent[j][1][5]) { td.innerHTML = `${listStudent[j][1][6]}` } else { td.innerHTML = 0 }
                    }
                    if (i == 1) {
                        if (listStudent[j][2][5]) { td.innerHTML = `${listStudent[j][2][6]}` } else { td.innerHTML = 0 }
                    }
                    if (i == 2) {
                        if (listStudent[j][3][5]) { td.innerHTML = `${listStudent[j][3][6]}` } else { td.innerHTML = 0 }
                    }
                    if (i == 3) {
                        if (listStudent[j][4][5]) { td.innerHTML = `${listStudent[j][4][6]}` } else { td.innerHTML = 0 }
                    }
                    if (i == 4) {
                        if (listStudent[j][5][5]) { td.innerHTML = `${listStudent[j][5][6]}` } else { td.innerHTML = 0 }
                    }
                    if (i == 5) {
                        if (listStudent[j][6][5]) { td.innerHTML = `${listStudent[j][6][6]}` } else { td.innerHTML = 0 }
                    }

                    if (i == 6) {
                        if (listStudent[j][7][5]) { td.innerHTML = `${listStudent[j][7][6]}` } else { td.innerHTML = 0 }
                    }
                    if (i == 7) {
                        if (listStudent[j][8][5]) { td.innerHTML = `${listStudent[j][8][6]}` } else { td.innerHTML = 0 }
                    }
                    if (i == 8) {
                        if (listStudent[j][9][5]) { td.innerHTML = `${listStudent[j][9][6]}` } else { td.innerHTML = 0 }
                    }
                    if (i == 9) {
                        if (listStudent[j][10][5]) { td.innerHTML = `${listStudent[j][10][6]}` } else { td.innerHTML = 0 }
                    }

                    if (i == 10) {
                        if (listStudent[j][11][5]) { td.innerHTML = `${listStudent[j][11][6]}` } else { td.innerHTML = 0 }
                    }
                    if (i == 11) {
                        if (listStudent[j][12][5]) { td.innerHTML = `${listStudent[j][12][6]}` } else { td.innerHTML = 0 }
                    }
                }
                if (k == 7) {
                    if (i == 0) { if (listStudent[j][1][5]) { td.innerHTML = 'Validée' } else { td.innerHTML = 'Non Validée' } }
                    if (i == 1) { if (listStudent[j][2][5]) { td.innerHTML = 'Validée' } else { td.innerHTML = 'Non Validée' } }
                    if (i == 2) { if (listStudent[j][3][5]) { td.innerHTML = 'Validée' } else { td.innerHTML = 'Non Validée' } }
                    if (i == 3) { if (listStudent[j][4][5]) { td.innerHTML = 'Validée' } else { td.innerHTML = 'Non Validée' } }
                    if (i == 4) { if (listStudent[j][5][5]) { td.innerHTML = 'Validée' } else { td.innerHTML = 'Non Validée' } }
                    if (i == 5) { if (listStudent[j][6][5]) { td.innerHTML = 'Validée' } else { td.innerHTML = 'Non Validée' } }

                    if (i == 6) { if (listStudent[j][7][5]) { td.innerHTML = 'Validée' } else { td.innerHTML = 'Non Validée' } }
                    if (i == 7) { if (listStudent[j][8][5]) { td.innerHTML = 'Validée' } else { td.innerHTML = 'Non Validée' } }
                    if (i == 8) { if (listStudent[j][9][5]) { td.innerHTML = 'Validée' } else { td.innerHTML = 'Non Validée' } }
                    if (i == 9) { if (listStudent[j][10][5]) { td.innerHTML = 'Validée' } else { td.innerHTML = 'Non Validée' } }

                    if (i == 10) { if (listStudent[j][11][5]) { td.innerHTML = 'Validée' } else { td.innerHTML = 'Non Validée' } }
                    if (i == 11) { if (listStudent[j][12][5]) { td.innerHTML = 'Validée' } else { td.innerHTML = 'Non Validée' } }
                }
                if (k == 8) {
                    if (i == 0) {
                        if (listStudent[j][1][0] >= 16) {
                            td.innerHTML = 'A';
                        } else if (listStudent[j][1][0] >= 15 && listStudent[j][1][0] < 16) {
                            td.innerHTML = 'A-'
                        } else if (listStudent[j][1][0] >= 14 && listStudent[j][1][0] < 15) {
                            td.innerHTML = 'B+'
                        } else if (listStudent[j][1][0] >= 13 && listStudent[j][1][0] < 14) {
                            td.innerHTML = 'B'
                        } else if (listStudent[j][1][0] >= 12 && listStudent[j][1][0] < 13) {
                            td.innerHTML = 'B-'
                        } else if (listStudent[j][1][0] >= 11 && listStudent[j][1][0] < 12) {
                            td.innerHTML = 'C+'
                        } else if (listStudent[j][1][0] >= 10 && listStudent[j][1][0] < 11) {
                            td.innerHTML = 'C'
                        } else if (listStudent[j][1][0] >= 9 && listStudent[j][1][0] < 10) {
                            td.innerHTML = 'C-'
                        } else if (listStudent[j][1][0] >= 8 && listStudent[j][1][0] < 9) {
                            td.innerHTML = 'D+'
                        } else if (listStudent[j][1][0] >= 7 && listStudent[j][1][0] < 8) {
                            td.innerHTML = 'D'
                        } else if (listStudent[j][1][0] >= 6 && listStudent[j][1][0] < 7) {
                            td.innerHTML = 'E'
                        } else if (listStudent[j][1][0] >= 0 && listStudent[j][1][0] < 6) {
                            td.innerHTML = 'F'
                        }
                    }

                    if (i == 1) {
                        if (listStudent[j][2][0] >= 16) {
                            td.innerHTML = 'A'
                        } else if (listStudent[j][2][0] >= 15 && listStudent[j][2][0] < 16) {
                            td.innerHTML = 'A-'
                        } else if (listStudent[j][2][0] >= 14 && listStudent[j][2][0] < 15) {
                            td.innerHTML = 'B+'
                        } else if (listStudent[j][2][0] >= 13 && listStudent[j][2][0] < 14) {
                            td.innerHTML = 'B'
                        } else if (listStudent[j][2][0] >= 12 && listStudent[j][2][0] < 13) {
                            td.innerHTML = 'B-'
                        } else if (listStudent[j][2][0] >= 11 && listStudent[j][2][0] < 12) {
                            td.innerHTML = 'C+'
                        } else if (listStudent[j][2][0] >= 10 && listStudent[j][2][0] < 11) {
                            td.innerHTML = 'C'
                        } else if (listStudent[j][2][0] >= 9 && listStudent[j][2][0] < 10) {
                            td.innerHTML = 'C-'
                        } else if (listStudent[j][2][0] >= 8 && listStudent[j][2][0] < 9) {
                            td.innerHTML = 'D+'
                        } else if (listStudent[j][2][0] >= 7 && listStudent[j][2][0] < 8) {
                            td.innerHTML = 'D'
                        } else if (listStudent[j][2][0] >= 6 && listStudent[j][2][0] < 7) {
                            td.innerHTML = 'E'
                        } else if (listStudent[j][2][0] >= 0 && listStudent[j][2][0] < 6) {
                            td.innerHTML = 'F'
                        }
                    }

                    if (i == 2) {
                        if (listStudent[j][3][0] >= 16) {
                            td.innerHTML = 'A'
                        } else if (listStudent[j][3][0] >= 15 && listStudent[j][3][0] < 16) {
                            td.innerHTML = 'A-'
                        } else if (listStudent[j][3][0] >= 14 && listStudent[j][3][0] < 15) {
                            td.innerHTML = 'B+'
                        } else if (listStudent[j][3][0] >= 13 && listStudent[j][3][0] < 14) {
                            td.innerHTML = 'B'
                        } else if (listStudent[j][3][0] >= 12 && listStudent[j][3][0] < 13) {
                            td.innerHTML = 'B-'
                        } else if (listStudent[j][3][0] >= 11 && listStudent[j][3][0] < 12) {
                            td.innerHTML = 'C+'
                        } else if (listStudent[j][3][0] >= 10 && listStudent[j][3][0] < 11) {
                            td.innerHTML = 'C'
                        } else if (listStudent[j][3][0] >= 9 && listStudent[j][3][0] < 10) {
                            td.innerHTML = 'C-'
                        } else if (listStudent[j][3][0] >= 8 && listStudent[j][3][0] < 9) {
                            td.innerHTML = 'D+'
                        } else if (listStudent[j][3][0] >= 7 && listStudent[j][3][0] < 8) {
                            td.innerHTML = 'D'
                        } else if (listStudent[j][3][0] >= 6 && listStudent[j][3][0] < 7) {
                            td.innerHTML = 'E'
                        } else if (listStudent[j][3][0] >= 0 && listStudent[j][3][0] < 6) {
                            td.innerHTML = 'F'
                        }
                    }

                    if (i == 3) {
                        if (listStudent[j][4][0] >= 16) {
                            td.innerHTML = 'A'
                        } else if (listStudent[j][4][0] >= 15 && listStudent[j][4][0] < 16) {
                            td.innerHTML = 'A-'
                        } else if (listStudent[j][4][0] >= 14 && listStudent[j][4][0] < 15) {
                            td.innerHTML = 'B+'
                        } else if (listStudent[j][4][0] >= 13 && listStudent[j][4][0] < 14) {
                            td.innerHTML = 'B'
                        } else if (listStudent[j][4][0] >= 12 && listStudent[j][4][0] < 13) {
                            td.innerHTML = 'B-'
                        } else if (listStudent[j][4][0] >= 11 && listStudent[j][4][0] < 12) {
                            td.innerHTML = 'C+'
                        } else if (listStudent[j][4][0] >= 10 && listStudent[j][4][0] < 11) {
                            td.innerHTML = 'C'
                        } else if (listStudent[j][4][0] >= 9 && listStudent[j][4][0] < 10) {
                            td.innerHTML = 'C-'
                        } else if (listStudent[j][4][0] >= 8 && listStudent[j][4][0] < 9) {
                            td.innerHTML = 'D+'
                        } else if (listStudent[j][4][0] >= 7 && listStudent[j][4][0] < 8) {
                            td.innerHTML = 'D'
                        } else if (listStudent[j][4][0] >= 6 && listStudent[j][4][0] < 7) {
                            td.innerHTML = 'E'
                        } else if (listStudent[j][4][0] >= 0 && listStudent[j][4][0] < 6) {
                            td.innerHTML = 'F'
                        }
                    }

                    if (i == 4) {
                        if (listStudent[j][5][0] >= 16) {
                            td.innerHTML = 'A'
                        } else if (listStudent[j][5][0] >= 15 && listStudent[j][5][0] < 16) {
                            td.innerHTML = 'A-'
                        } else if (listStudent[j][5][0] >= 14 && listStudent[j][5][0] < 15) {
                            td.innerHTML = 'B+'
                        } else if (listStudent[j][5][0] >= 13 && listStudent[j][5][0] < 14) {
                            td.innerHTML = 'B'
                        } else if (listStudent[j][5][0] >= 12 && listStudent[j][5][0] < 13) {
                            td.innerHTML = 'B-'
                        } else if (listStudent[j][5][0] >= 11 && listStudent[j][5][0] < 12) {
                            td.innerHTML = 'C+'
                        } else if (listStudent[j][5][0] >= 10 && listStudent[j][5][0] < 11) {
                            td.innerHTML = 'C'
                        } else if (listStudent[j][5][0] >= 9 && listStudent[j][5][0] < 10) {
                            td.innerHTML = 'C-'
                        } else if (listStudent[j][5][0] >= 8 && listStudent[j][5][0] < 9) {
                            td.innerHTML = 'D+'
                        } else if (listStudent[j][5][0] >= 7 && listStudent[j][5][0] < 8) {
                            td.innerHTML = 'D'
                        } else if (listStudent[j][5][0] >= 6 && listStudent[j][5][0] < 7) {
                            td.innerHTML = 'E'
                        } else if (listStudent[j][5][0] >= 0 && listStudent[j][5][0] < 6) {
                            td.innerHTML = 'F'
                        }
                    }

                    if (i == 5) {
                        if (listStudent[j][6][0] >= 16) {
                            td.innerHTML = 'A'
                        } else if (listStudent[j][6][0] >= 15 && listStudent[j][6][0] < 16) {
                            td.innerHTML = 'A-'
                        } else if (listStudent[j][6][0] >= 14 && listStudent[j][6][0] < 15) {
                            td.innerHTML = 'B+'
                        } else if (listStudent[j][6][0] >= 13 && listStudent[j][6][0] < 14) {
                            td.innerHTML = 'B'
                        } else if (listStudent[j][6][0] >= 12 && listStudent[j][6][0] < 13) {
                            td.innerHTML = 'B-'
                        } else if (listStudent[j][6][0] >= 11 && listStudent[j][6][0] < 12) {
                            td.innerHTML = 'C+'
                        } else if (listStudent[j][6][0] >= 10 && listStudent[j][6][0] < 11) {
                            td.innerHTML = 'C'
                        } else if (listStudent[j][6][0] >= 9 && listStudent[j][6][0] < 10) {
                            td.innerHTML = 'C-'
                        } else if (listStudent[j][6][0] >= 8 && listStudent[j][6][0] < 9) {
                            td.innerHTML = 'D+'
                        } else if (listStudent[j][6][0] >= 7 && listStudent[j][6][0] < 8) {
                            td.innerHTML = 'D'
                        } else if (listStudent[j][6][0] >= 6 && listStudent[j][6][0] < 7) {
                            td.innerHTML = 'E'
                        } else if (listStudent[j][6][0] >= 0 && listStudent[j][6][0] < 6) {
                            td.innerHTML = 'F'
                        }
                    }

                    if (i == 6) {
                        if (listStudent[j][7][0] >= 16) {
                            td.innerHTML = 'A'
                        } else if (listStudent[j][7][0] >= 15 && listStudent[j][7][0] < 16) {
                            td.innerHTML = 'A-'
                        } else if (listStudent[j][7][0] >= 14 && listStudent[j][7][0] < 15) {
                            td.innerHTML = 'B+'
                        } else if (listStudent[j][7][0] >= 13 && listStudent[j][7][0] < 14) {
                            td.innerHTML = 'B'
                        } else if (listStudent[j][7][0] >= 12 && listStudent[j][7][0] < 13) {
                            td.innerHTML = 'B-'
                        } else if (listStudent[j][7][0] >= 11 && listStudent[j][7][0] < 12) {
                            td.innerHTML = 'C+'
                        } else if (listStudent[j][7][0] >= 10 && listStudent[j][7][0] < 11) {
                            td.innerHTML = 'C'
                        } else if (listStudent[j][7][0] >= 9 && listStudent[j][7][0] < 10) {
                            td.innerHTML = 'C-'
                        } else if (listStudent[j][7][0] >= 8 && listStudent[j][7][0] < 9) {
                            td.innerHTML = 'D+'
                        } else if (listStudent[j][7][0] >= 7 && listStudent[j][7][0] < 8) {
                            td.innerHTML = 'D'
                        } else if (listStudent[j][7][0] >= 6 && listStudent[j][7][0] < 7) {
                            td.innerHTML = 'E'
                        } else if (listStudent[j][7][0] >= 0 && listStudent[j][7][0] < 6) {
                            td.innerHTML = 'F'
                        }
                    }

                    if (i == 7) {
                        if (listStudent[j][8][0] >= 16) {
                            td.innerHTML = 'A'
                        } else if (listStudent[j][8][0] >= 15 && listStudent[j][8][0] < 16) {
                            td.innerHTML = 'A-'
                        } else if (listStudent[j][8][0] >= 14 && listStudent[j][8][0] < 15) {
                            td.innerHTML = 'B+'
                        } else if (listStudent[j][8][0] >= 13 && listStudent[j][8][0] < 14) {
                            td.innerHTML = 'B'
                        } else if (listStudent[j][8][0] >= 12 && listStudent[j][8][0] < 13) {
                            td.innerHTML = 'B-'
                        } else if (listStudent[j][8][0] >= 11 && listStudent[j][8][0] < 12) {
                            td.innerHTML = 'C+'
                        } else if (listStudent[j][8][0] >= 10 && listStudent[j][8][0] < 11) {
                            td.innerHTML = 'C'
                        } else if (listStudent[j][8][0] >= 9 && listStudent[j][8][0] < 10) {
                            td.innerHTML = 'C-'
                        } else if (listStudent[j][8][0] >= 8 && listStudent[j][8][0] < 9) {
                            td.innerHTML = 'D+'
                        } else if (listStudent[j][8][0] >= 7 && listStudent[j][8][0] < 8) {
                            td.innerHTML = 'D'
                        } else if (listStudent[j][8][0] >= 6 && listStudent[j][8][0] < 7) {
                            td.innerHTML = 'E'
                        } else if (listStudent[j][8][0] >= 0 && listStudent[j][8][0] < 6) {
                            td.innerHTML = 'F'
                        }
                    }

                    if (i == 8) {
                        if (listStudent[j][9][0] >= 16) {
                            td.innerHTML = 'A'
                        } else if (listStudent[j][9][0] >= 15 && listStudent[j][9][0] < 16) {
                            td.innerHTML = 'A-'
                        } else if (listStudent[j][9][0] >= 14 && listStudent[j][9][0] < 15) {
                            td.innerHTML = 'B+'
                        } else if (listStudent[j][9][0] >= 13 && listStudent[j][9][0] < 14) {
                            td.innerHTML = 'B'
                        } else if (listStudent[j][9][0] >= 12 && listStudent[j][9][0] < 13) {
                            td.innerHTML = 'B-'
                        } else if (listStudent[j][9][0] >= 11 && listStudent[j][9][0] < 12) {
                            td.innerHTML = 'C+'
                        } else if (listStudent[j][9][0] >= 10 && listStudent[j][9][0] < 11) {
                            td.innerHTML = 'C'
                        } else if (listStudent[j][9][0] >= 9 && listStudent[j][9][0] < 10) {
                            td.innerHTML = 'C-'
                        } else if (listStudent[j][9][0] >= 8 && listStudent[j][9][0] < 9) {
                            td.innerHTML = 'D+'
                        } else if (listStudent[j][9][0] >= 7 && listStudent[j][9][0] < 8) {
                            td.innerHTML = 'D'
                        } else if (listStudent[j][9][0] >= 6 && listStudent[j][9][0] < 7) {
                            td.innerHTML = 'E'
                        } else if (listStudent[j][9][0] >= 0 && listStudent[j][9][0] < 6) {
                            td.innerHTML = 'F'
                        }
                    }

                    if (i == 9) {
                        if (listStudent[j][10][0] >= 16) {
                            td.innerHTML = 'A'
                        } else if (listStudent[j][10][0] >= 15 && listStudent[j][10][0] < 16) {
                            td.innerHTML = 'A-'
                        } else if (listStudent[j][10][0] >= 14 && listStudent[j][10][0] < 15) {
                            td.innerHTML = 'B+'
                        } else if (listStudent[j][10][0] >= 13 && listStudent[j][10][0] < 14) {
                            td.innerHTML = 'B'
                        } else if (listStudent[j][10][0] >= 12 && listStudent[j][10][0] < 13) {
                            td.innerHTML = 'B-'
                        } else if (listStudent[j][10][0] >= 11 && listStudent[j][10][0] < 12) {
                            td.innerHTML = 'C+'
                        } else if (listStudent[j][10][0] >= 10 && listStudent[j][10][0] < 11) {
                            td.innerHTML = 'C'
                        } else if (listStudent[j][10][0] >= 9 && listStudent[j][10][0] < 10) {
                            td.innerHTML = 'C-'
                        } else if (listStudent[j][10][0] >= 8 && listStudent[j][10][0] < 9) {
                            td.innerHTML = 'D+'
                        } else if (listStudent[j][10][0] >= 7 && listStudent[j][10][0] < 8) {
                            td.innerHTML = 'D'
                        } else if (listStudent[j][10][0] >= 6 && listStudent[j][10][0] < 7) {
                            td.innerHTML = 'E'
                        } else if (listStudent[j][10][0] >= 0 && listStudent[j][10][0] < 6) {
                            td.innerHTML = 'F'
                        }
                    }

                    if (i == 10) {
                        if (listStudent[j][11][0] >= 16) {
                            td.innerHTML = 'A'
                        } else if (listStudent[j][11][0] >= 15 && listStudent[j][11][0] < 16) {
                            td.innerHTML = 'A-'
                        } else if (listStudent[j][11][0] >= 14 && listStudent[j][11][0] < 15) {
                            td.innerHTML = 'B+'
                        } else if (listStudent[j][11][0] >= 13 && listStudent[j][11][0] < 14) {
                            td.innerHTML = 'B'
                        } else if (listStudent[j][11][0] >= 12 && listStudent[j][11][0] < 13) {
                            td.innerHTML = 'B-'
                        } else if (listStudent[j][11][0] >= 11 && listStudent[j][11][0] < 12) {
                            td.innerHTML = 'C+'
                        } else if (listStudent[j][11][0] >= 10 && listStudent[j][11][0] < 11) {
                            td.innerHTML = 'C'
                        } else if (listStudent[j][11][0] >= 9 && listStudent[j][11][0] < 10) {
                            td.innerHTML = 'C-'
                        } else if (listStudent[j][11][0] >= 8 && listStudent[j][11][0] < 9) {
                            td.innerHTML = 'D+'
                        } else if (listStudent[j][11][0] >= 7 && listStudent[j][11][0] < 8) {
                            td.innerHTML = 'D'
                        } else if (listStudent[j][11][0] >= 6 && listStudent[j][11][0] < 7) {
                            td.innerHTML = 'E'
                        } else if (listStudent[j][11][0] >= 0 && listStudent[j][11][0] < 6) {
                            td.innerHTML = 'F'
                        }
                    }

                    if (i == 11) {
                        if (listStudent[j][12][0] >= 16) {
                            td.innerHTML = 'A'
                        } else if (listStudent[j][12][0] >= 15 && listStudent[j][12][0] < 16) {
                            td.innerHTML = 'A-'
                        } else if (listStudent[j][12][0] >= 14 && listStudent[j][12][0] < 15) {
                            td.innerHTML = 'B+'
                        } else if (listStudent[j][12][0] >= 13 && listStudent[j][12][0] < 14) {
                            td.innerHTML = 'B'
                        } else if (listStudent[j][12][0] >= 12 && listStudent[j][12][0] < 13) {
                            td.innerHTML = 'B-'
                        } else if (listStudent[j][12][0] >= 11 && listStudent[j][12][0] < 12) {
                            td.innerHTML = 'C+'
                        } else if (listStudent[j][12][0] >= 10 && listStudent[j][12][0] < 11) {
                            td.innerHTML = 'C'
                        } else if (listStudent[j][12][0] >= 9 && listStudent[j][12][0] < 10) {
                            td.innerHTML = 'C-'
                        } else if (listStudent[j][12][0] >= 8 && listStudent[j][12][0] < 9) {
                            td.innerHTML = 'D+'
                        } else if (listStudent[j][12][0] >= 7 && listStudent[j][12][0] < 8) {
                            td.innerHTML = 'D'
                        } else if (listStudent[j][12][0] >= 6 && listStudent[j][12][0] < 7) {
                            td.innerHTML = 'E'
                        } else if (listStudent[j][12][0] >= 0 && listStudent[j][12][0] < 6) {
                            td.innerHTML = 'F'
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

        if (i == 0) {
            //Ligne 1
            ligneStat1.children[1].innerHTML = mydata[1].length
            ligneStat1.children[4].innerHTML = mydata[7][0]['Passable']
            ligneStat1.children[5].innerHTML = `${(mydata[7][0]['pourcentageP'])} %`
                //Ligne2
            ligneStat2.children[1].innerHTML = mydata[6][0]['nombre']
            ligneStat2.children[2].innerHTML = `${(mydata[6][0]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML = mydata[7][0]['Assez Bien']
            ligneStat2.children[5].innerHTML = `${(mydata[7][0]['pourcentageAB'])} %`
                //Ligne3
            ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][0]['nombre']
            ligneStat3.children[2].innerHTML = `${ floatfix(mydata[6][0]['pourcentage']) } %`

            ligneStat3.children[4].innerHTML = mydata[7][0]['Bien']
            ligneStat3.children[5].innerHTML = `${(mydata[7][0]['pourcentageB'])} %`
                //Ligne4
            ligneStat4.children[4].innerHTML = mydata[7][0]['Très Bien']
            ligneStat4.children[5].innerHTML = `${(mydata[7][0]['pourcentageTB'])} %`
        }
        if (i == 1) {
            //Ligne 1
            ligneStat1.children[1].innerHTML = mydata[1].length
            ligneStat1.children[4].innerHTML = mydata[7][1]['Passable']
            ligneStat1.children[5].innerHTML = `${(mydata[7][1]['pourcentageP'])} %`
                //Ligne2
            ligneStat2.children[1].innerHTML = mydata[6][1]['nombre']
            ligneStat2.children[2].innerHTML = `${(mydata[6][1]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML = mydata[7][1]['Assez Bien']
            ligneStat2.children[5].innerHTML = `${(mydata[7][1]['pourcentageAB'])} %`
                //Ligne3
            ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][1]['nombre']
            ligneStat3.children[2].innerHTML = `${ floatfix(mydata[6][1]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML = mydata[7][1]['Bien']
            ligneStat3.children[5].innerHTML = `${(mydata[7][1]['pourcentageB'])} %`
                //Ligne4
            ligneStat4.children[4].innerHTML = mydata[7][1]['Très Bien']
            ligneStat4.children[5].innerHTML = `${(mydata[7][1]['pourcentageTB'])} %`
        }
        if (i == 2) {
            //Ligne 1
            ligneStat1.children[1].innerHTML = mydata[1].length
            ligneStat1.children[4].innerHTML = mydata[7][2]['Passable']
            ligneStat1.children[5].innerHTML = `${(mydata[7][2]['pourcentageP'])} %`
                //Ligne2
            ligneStat2.children[1].innerHTML = mydata[6][2]['nombre']
            ligneStat2.children[2].innerHTML = `${(mydata[6][2]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML = mydata[7][2]['Assez Bien']
            ligneStat2.children[5].innerHTML = `${(mydata[7][2]['pourcentageAB'])} %`
                //Ligne3
            ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][2]['nombre']
            ligneStat3.children[2].innerHTML = `${ floatfix(mydata[6][2]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML = mydata[7][2]['Bien']
            ligneStat3.children[5].innerHTML = `${(mydata[7][2]['pourcentageB'])} %`
                //Ligne4
            ligneStat4.children[4].innerHTML = mydata[7][2]['Très Bien']
            ligneStat4.children[5].innerHTML = `${(mydata[7][2]['pourcentageTB'])} %`
        }
        if (i == 3) {
            //Ligne 1
            ligneStat1.children[1].innerHTML = mydata[1].length
            ligneStat1.children[4].innerHTML = mydata[7][3]['Passable']
            ligneStat1.children[5].innerHTML = `${(mydata[7][3]['pourcentageP'])} %`
                //Ligne2
            ligneStat2.children[1].innerHTML = mydata[6][3]['nombre']
            ligneStat2.children[2].innerHTML = `${(mydata[6][3]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML = mydata[7][3]['Assez Bien']
            ligneStat2.children[5].innerHTML = `${(mydata[7][3]['pourcentageAB'])} %`
                //Ligne3
            ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][3]['nombre']
            ligneStat3.children[2].innerHTML = `${floatfix(mydata[6][3]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML = mydata[7][3]['Bien']
            ligneStat3.children[5].innerHTML = `${(mydata[7][3]['pourcentageB'])} %`
                //Ligne4
            ligneStat4.children[4].innerHTML = mydata[7][3]['Très Bien']
            ligneStat4.children[5].innerHTML = `${(mydata[7][3]['pourcentageTB'])} %`
        }
        if (i == 4) {
            //Ligne 1
            ligneStat1.children[1].innerHTML = mydata[1].length
            ligneStat1.children[4].innerHTML = mydata[7][4]['Passable']
            ligneStat1.children[5].innerHTML = `${(mydata[7][4]['pourcentageP'])} %`
                //Ligne2
            ligneStat2.children[1].innerHTML = mydata[6][4]['nombre']
            ligneStat2.children[2].innerHTML = `${(mydata[6][4]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML = mydata[7][4]['Assez Bien']
            ligneStat2.children[5].innerHTML = `${(mydata[7][4]['pourcentageAB'])} %`
                //Ligne3
            ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][4]['nombre']
            ligneStat3.children[2].innerHTML = `${floatfix(mydata[6][4]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML = mydata[7][4]['Bien']
            ligneStat3.children[5].innerHTML = `${(mydata[7][4]['pourcentageB'])} %`
                //Ligne4
            ligneStat4.children[4].innerHTML = mydata[7][4]['Très Bien']
            ligneStat4.children[5].innerHTML = `${(mydata[7][4]['pourcentageTB'])} %`
        }
        if (i == 5) {
            //Ligne 1
            ligneStat1.children[1].innerHTML = mydata[1].length
            ligneStat1.children[4].innerHTML = mydata[7][5]['Passable']
            ligneStat1.children[5].innerHTML = `${(mydata[7][5]['pourcentageP'])} %`
                //Ligne2
            ligneStat2.children[1].innerHTML = mydata[6][5]['nombre']
            ligneStat2.children[2].innerHTML = `${(mydata[6][5]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML = mydata[7][5]['Assez Bien']
            ligneStat2.children[5].innerHTML = `${(mydata[7][5]['pourcentageAB'])} %`
                //Ligne3
            ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][5]['nombre']
            ligneStat3.children[2].innerHTML = `${floatfix(mydata[6][5]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML = mydata[7][5]['Bien']
            ligneStat3.children[5].innerHTML = `${(mydata[7][5]['pourcentageB'])} %`
                //Ligne4
            ligneStat4.children[4].innerHTML = mydata[7][5]['Très Bien']
            ligneStat4.children[5].innerHTML = `${(mydata[7][5]['pourcentageTB'])} %`
        }
        if (i == 6) {
            //Ligne 1
            ligneStat1.children[1].innerHTML = mydata[1].length
            ligneStat1.children[4].innerHTML = mydata[7][6]['Passable']
            ligneStat1.children[5].innerHTML = `${(mydata[7][6]['pourcentageP'])} %`
                //Ligne2
            ligneStat2.children[1].innerHTML = mydata[6][6]['nombre']
            ligneStat2.children[2].innerHTML = `${(mydata[6][6]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML = mydata[7][6]['Assez Bien']
            ligneStat2.children[5].innerHTML = `${(mydata[7][6]['pourcentageAB'])} %`
                //Ligne3
            ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][6]['nombre']
            ligneStat3.children[2].innerHTML = `${floatfix(mydata[6][6]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML = mydata[7][6]['Bien']
            ligneStat3.children[5].innerHTML = `${(mydata[7][6]['pourcentageB'])} %`
                //Ligne4
            ligneStat4.children[4].innerHTML = mydata[7][6]['Très Bien']
            ligneStat4.children[5].innerHTML = `${(mydata[7][6]['pourcentageTB'])} %`
        }
        if (i == 7) {
            //Ligne 1
            ligneStat1.children[1].innerHTML = mydata[1].length
            ligneStat1.children[4].innerHTML = mydata[7][7]['Passable']
            ligneStat1.children[5].innerHTML = `${(mydata[7][7]['pourcentageP'])} %`
                //Ligne2
            ligneStat2.children[1].innerHTML = mydata[6][7]['nombre']
            ligneStat2.children[2].innerHTML = `${(mydata[6][7]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML = mydata[7][7]['Assez Bien']
            ligneStat2.children[5].innerHTML = `${(mydata[7][7]['pourcentageAB'])} %`
                //Ligne3
            ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][7]['nombre']
            ligneStat3.children[2].innerHTML = `${floatfix(mydata[6][7]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML = mydata[7][7]['Bien']
            ligneStat3.children[5].innerHTML = `${(mydata[7][7]['pourcentageB'])} %`
                //Ligne4
            ligneStat4.children[4].innerHTML = mydata[7][7]['Très Bien']
            ligneStat4.children[5].innerHTML = `${(mydata[7][7]['pourcentageTB'])} %`
        }
        if (i == 8) {
            //Ligne 1
            ligneStat1.children[1].innerHTML = mydata[1].length
            ligneStat1.children[4].innerHTML = mydata[7][8]['Passable']
            ligneStat1.children[5].innerHTML = `${(mydata[7][8]['pourcentageP'])} %`
                //Ligne2
            ligneStat2.children[1].innerHTML = mydata[6][8]['nombre']
            ligneStat2.children[2].innerHTML = `${(mydata[6][8]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML = mydata[7][8]['Assez Bien']
            ligneStat2.children[5].innerHTML = `${(mydata[7][8]['pourcentageAB'])} %`
                //Ligne3
            ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][8]['nombre']
            ligneStat3.children[2].innerHTML = `${floatfix(mydata[6][8]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML = mydata[7][8]['Bien']
            ligneStat3.children[5].innerHTML = `${(mydata[7][8]['pourcentageB'])} %`
                //Ligne4
            ligneStat4.children[4].innerHTML = mydata[7][8]['Très Bien']
            ligneStat4.children[5].innerHTML = `${(mydata[7][8]['pourcentageTB'])} %`
        }
        if (i == 9) {
            //Ligne 1
            ligneStat1.children[1].innerHTML = mydata[1].length
            ligneStat1.children[4].innerHTML = mydata[7][9]['Passable']
            ligneStat1.children[5].innerHTML = `${(mydata[7][9]['pourcentageP'])} %`
                //Ligne2
            ligneStat2.children[1].innerHTML = mydata[6][9]['nombre']
            ligneStat2.children[2].innerHTML = `${(mydata[6][9]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML = mydata[7][9]['Assez Bien']
            ligneStat2.children[5].innerHTML = `${(mydata[7][9]['pourcentageAB'])} %`
                //Ligne3
            ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][9]['nombre']
            ligneStat3.children[2].innerHTML = `${floatfix(mydata[6][9]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML = mydata[7][9]['Bien']
            ligneStat3.children[5].innerHTML = `${(mydata[7][9]['pourcentageB'])} %`
                //Ligne4
            ligneStat4.children[4].innerHTML = mydata[7][9]['Très Bien']
            ligneStat4.children[5].innerHTML = `${(mydata[7][9]['pourcentageTB'])} %`
        }
        if (i == 10) {
            //Ligne 1
            ligneStat1.children[1].innerHTML = mydata[1].length
            ligneStat1.children[4].innerHTML = mydata[7][10]['Passable']
            ligneStat1.children[5].innerHTML = `${(mydata[7][10]['pourcentageP'])} %`
                //Ligne2
            ligneStat2.children[1].innerHTML = mydata[6][10]['nombre']
            ligneStat2.children[2].innerHTML = `${(mydata[6][10]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML = mydata[7][10]['Assez Bien']
            ligneStat2.children[5].innerHTML = `${(mydata[7][10]['pourcentageAB'])} %`
                //Ligne3
            ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][10]['nombre']
            ligneStat3.children[2].innerHTML = `${floatfix(mydata[6][10]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML = mydata[7][10]['Bien']
            ligneStat3.children[5].innerHTML = `${(mydata[7][10]['pourcentageB'])} %`
                //Ligne4
            ligneStat4.children[4].innerHTML = mydata[7][10]['Très Bien']
            ligneStat4.children[5].innerHTML = `${(mydata[7][10]['pourcentageTB'])} %`
        }
        if (i == 11) {
            //Ligne 1
            ligneStat1.children[1].innerHTML = mydata[1].length
            ligneStat1.children[4].innerHTML = mydata[7][11]['Passable']
            ligneStat1.children[5].innerHTML = `${(mydata[7][11]['pourcentageP'])} %`
                //Ligne2
            ligneStat2.children[1].innerHTML = mydata[6][11]['nombre']
            ligneStat2.children[2].innerHTML = `${(mydata[6][11]['pourcentage'])} %`

            ligneStat2.children[4].innerHTML = mydata[7][11]['Assez Bien']
            ligneStat2.children[5].innerHTML = `${(mydata[7][11]['pourcentageAB'])} %`
                //Ligne3
            ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][11]['nombre']
            ligneStat3.children[2].innerHTML = `${floatfix(mydata[6][11]['pourcentage'])} %`

            ligneStat3.children[4].innerHTML = mydata[7][11]['Bien']
            ligneStat3.children[5].innerHTML = `${(mydata[7][11]['pourcentageB'])} %`
                //Ligne4
            ligneStat4.children[4].innerHTML = mydata[7][11]['Très Bien']
            ligneStat4.children[5].innerHTML = `${(mydata[7][11]['pourcentageTB'])} %`
        }


        return (clone)
    }


    ListProcess()
})

function floatfix(a) {
    return (100 - a).toFixed(2)
}