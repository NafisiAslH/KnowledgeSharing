async  function run() {
    if (detectDayOrMonth() == true)
        [clp_wrts, emp_wrts] = await extractWriteupsInDay();
    else
        [clp_wrts, emp_wrts] = await extractWriteupsInMonth();

    //OpenLinks(clp_wrts);
    PrintResults(emp_wrts);
}


// true for day
function detectDayOrMonth() {
    link = window.location.href;
    return link.split("/")[link.split("/").length-3].startsWith("202")
}


async  function extractWriteupsInDay() {
    clp_wrts = [];
    emp_wrts = [];
    base_wrt_xpath = "/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[NUMNUM]"

    while (true) {
        wrt_num = 0;
        
        while (true) {
            wrt_num++;
            wrt_xpath = base_wrt_xpath.replace("NUMNUM",wrt_num);
            clap_num = getClapNumber(wrt_xpath);
            if (clap_num == -1)
                break;
            if (clap_num > 50)
                clp_wrts.push(getWriteupInfo(wrt_xpath));
            else
                emp_wrts.push(getWriteupInfo(wrt_xpath));
        }
        
        finish = redirectToNextDay()
        await new Promise(r => setTimeout(r, 3000));
        if (finish == false)
            break;
    }

    return [clp_wrts, emp_wrts];
}


async  function extractWriteupsInMonth() {
    clp_wrts = [];
    emp_wrts = [];
    base_wrt_xpath = "/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[NUMNUM]"
    
    await sortLatest();
    await scrollDown();

    wrt_num=0;
    while (true) {
        wrt_num++;
        wrt_xpath = base_wrt_xpath.replace("NUMNUM",wrt_num);
        clap_num = getClapNumber(wrt_xpath);
        if (clap_num == -1)
            break;
        if (clap_num > 50)
            clp_wrts.push(getWriteupInfo(wrt_xpath));
        else
            emp_wrts.push(getWriteupInfo(wrt_xpath));
    }

    return [clp_wrts, emp_wrts];
}


function PrintResults(wrts) {
    window.document.write("<!DOCTYPE html> <html> <head>")
    window.document.write("<style> table {font-family: arial, sans-serif; border-collapse: collapse;}  td, th {border: 1px solid #dddddd; text-align: left; padding: 8px;}  tr:nth-child(even) {background-color: #dddddd;} </style>")
    window.document.write("</head> <body>")
    window.document.write("<script>function OpenLinks() {")
    wrts.forEach(function(wrt) {window.document.write("window.open('" + wrt.link + "', '_blank');")});
    window.document.write("}</script>")
    window.document.write("<center><h1> Write-up with more than 50 claps</h1><button onclick=OpenLinks()>Open Links</button>")
    window.document.write("<center><h1> Write-up with less than 50 claps</h1><table><tr><th style=\"text-align:center\">Date</th><th style=\"text-align:center\">Name</th></tr>")
    wrts.forEach(function(wrt) {window.document.write("<tr>" + "<td>" + wrt.date + "</td><td><a href=" + wrt.link + ">" + wrt.name + "</a></td>" + "</tr>");});
    window.document.write("</table><br><br><br><h3>Author: NafisiAslH </h3> <a href=https://twitter.com/MeAsHacker_HNA>Twitter</a> <a href=https://github.com/NafisiAslH/KnowledgeSharing>Github</a></center>")
}


function OpenLinks(wrts) {
    wrts.forEach( wrt => {
        window.open(wrt.link, '_blank')
    })
    
}


function getClapNumber(wrt_xpath) {
    wrt = getElementByXpath(wrt_xpath);
    if (wrt == null)
        return -1;
    
    btn_xpath = wrt_xpath + "/div/div/div[4]/div[1]/div/span/button";
    btn = getElementByXpath(btn_xpath);
    
    if (btn == null)
        return 0;
    return btn.textContent;
}


function getWriteupInfo(wrt_xpath) {
    name_xpath1 = wrt_xpath + "/div/div/div[2]/a/div/section/div[2]/div/h3";
    name_xpath2 = wrt_xpath + "/div/div/div[2]/div/section/div/div/a/h3";
    name_xpath3 = wrt_xpath + "/div/div/div[2]/a/div/section/div[2]/div/p[1]/strong"
    name_xpath4 = wrt_xpath + "/div/div/div[2]/div/section/div/div/h3/a"
    name_xpath5 = wrt_xpath + "/div/div/div[2]/a/div/section/div[2]/div/p[1]"
    name_xpath6 = wrt_xpath + "/div/div/div[2]/div/section/div/div/a/p[1]"
    a_xpath = wrt_xpath + "/div/div/div[2]/a";
    date_xpath = wrt_xpath + "/div/div/div[1]/div/div/div[2]/div/a"
    
    name_el = getElementByXpath(name_xpath1)
    if (name_el == null)
        name_el = getElementByXpath(name_xpath2)
    if (name_el == null)
        name_el = getElementByXpath(name_xpath3)
    if (name_el == null)
        name_el = getElementByXpath(name_xpath4)
    if (name_el == null)
        name_el = getElementByXpath(name_xpath5)
    if (name_el == null)
        name_el = getElementByXpath(name_xpath6)
    
    name = name_el.textContent;
    link = getElementByXpath(a_xpath).href.split("?")[0];
    date = getElementByXpath(date_xpath).text

    return {name:name, date:date, link:link};
}



function redirectToNextDay() {
    url = location.href;
    
    next_day_btn_xpath1 = "/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/div[3]/div[2]/a"
    next_day_btn_xpath2 = "/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/div[3]/div/a"
    
    if (url.substring(url.length-2) == "01")
        next_day_btn = getElementByXpath(next_day_btn_xpath2)
    else
        next_day_btn = getElementByXpath(next_day_btn_xpath1);
                                     
    if (next_day_btn == null)
        return false;
    next_day_btn.click()
    return true;
}


async function sortLatest() {
    btn1_xpath1="/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[5]/button"
    btn1_xpath2="/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[4]/button"
    btn2_xpath1="/html/body/div[1]/div[2]/div/div[4]/div[1]/ul/li[3]/button"
    
    btn1_el = getElementByXpath(btn1_xpath1)
    if (btn1_el == null)
        btn1_el = getElementByXpath(btn1_xpath2)
    btn1_el.click()
    await new Promise(r => setTimeout(r, 1000));
    
    btn2_el = getElementByXpath(btn2_xpath1)
    btn2_el.click()
    await new Promise(r => setTimeout(r, 1000));

}


async function scrollDown() {
    for (let i=0; i<10; i++) {
        window.scrollTo(0, document.body.scrollHeight);
        await new Promise(r => setTimeout(r, 3000));
    }
}


function getElementByXpath(path) {
      return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}

run()
