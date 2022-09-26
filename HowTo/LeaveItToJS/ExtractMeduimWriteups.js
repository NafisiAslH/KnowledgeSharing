processingJS = 'async function Processing() {    if (DetectDailyOrMonthly() == "daily")        await DayProcessing();    else        await MonthlyTagProcessing();}async function DayProcessing() {    console.log("DayProcessing is started");    clp_wrts = [];    emp_wrts = [];    wrt_num = 0;    base_wrt_xpath = "/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[NUMNUM]";    while (true) {        wrt_num++;        wrt_xpath = base_wrt_xpath.replace("NUMNUM",wrt_num);        clap_num = GetClapNumber(wrt_xpath);        if (clap_num == -1)            break;        if (clap_num > 50)            clp_wrts.push(GetWriteupInfo(wrt_xpath));        else            emp_wrts.push(GetWriteupInfo(wrt_xpath));    }    console.log("writeups is procssed.");    UpdateLocalStroageItem("clp_wrts", clp_wrts);    UpdateLocalStroageItem("emp_wrts", emp_wrts);    localStorage.setItem("DayLock", "RELEAS");    console.log("localstorage is upated");    window.close(``, `_parent`, ``);}async  function MonthlyTagProcessing() {    console.log("MonthlyTagProcessing is started");    clp_wrts = [];    emp_wrts = [];    base_wrt_xpath = "/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[NUMNUM]";        await SortLatest();    await ScrollDown();    wrt_num=0;    while (true) {        wrt_num++;        wrt_xpath = base_wrt_xpath.replace("NUMNUM",wrt_num);        clap_num = GetClapNumber(wrt_xpath);        if (clap_num == -1)            break;        if (clap_num > 50)            clp_wrts.push(GetWriteupInfo(wrt_xpath));        else            emp_wrts.push(GetWriteupInfo(wrt_xpath));    }    console.log("writeups is procssed.");    UpdateLocalStroageItem("clp_wrts", clp_wrts);    UpdateLocalStroageItem("emp_wrts", emp_wrts);    localStorage.setItem("TagLock", "RELEAS");    console.log("localstorage is upated");    window.close(``, `_parent`, ``);}function DetectDailyOrMonthly() {    link = window.location.href;    if (link.split("/")[link.split("/").length-3].startsWith("202"))        return "daily";    else        return "monthly";}function GetClapNumber(wrt_xpath) {    wrt = GetElementByXpath(wrt_xpath);    if (wrt == null)        return -1;        btn_xpath = wrt_xpath + "/div/div/div[4]/div[1]/div/span/button";    btn = GetElementByXpath(btn_xpath);        if (btn == null)        return 0;    return btn.textContent;}function GetWriteupInfo(wrt_xpath) {    name_xpath1 = wrt_xpath + "/div/div/div[2]/a/div/section/div[2]/div/h3";    name_xpath2 = wrt_xpath + "/div/div/div[2]/div/section/div/div/a/h3";    name_xpath3 = wrt_xpath + "/div/div/div[2]/a/div/section/div[2]/div/p[1]/strong";    name_xpath4 = wrt_xpath + "/div/div/div[2]/div/section/div/div/h3/a";    name_xpath5 = wrt_xpath + "/div/div/div[2]/a/div/section/div[2]/div/p[1]";    name_xpath6 = wrt_xpath + "/div/div/div[2]/div/section/div/div/a/p[1]";    a_xpath = wrt_xpath + "/div/div/div[2]/a";    date_xpath = wrt_xpath + "/div/div/div[1]/div/div/div[2]/div/a";        name_el = GetElementByXpath(name_xpath1);    if (name_el == null)        name_el = GetElementByXpath(name_xpath2);    if (name_el == null)        name_el = GetElementByXpath(name_xpath3);    if (name_el == null)        name_el = GetElementByXpath(name_xpath4);    if (name_el == null)        name_el = GetElementByXpath(name_xpath5);    if (name_el == null)        name_el = GetElementByXpath(name_xpath6);        name = name_el.textContent;    link = GetElementByXpath(a_xpath).href.split("?")[0];    date = GetElementByXpath(date_xpath).text;    return {name:name, date:date, link:link};}function GetElementByXpath(path) {    return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}function UpdateLocalStroageItem(name , writeups) {    value_from_storage = GetLocalStroageItem(name);    writeups.forEach(function(writeup) {value_from_storage.push(writeup)});    output = SortUniqArray(value_from_storage);    localStorage.setItem(name, JSON.stringify(output));}function GetLocalStroageItem(name) {    ans = [];    value = localStorage.getItem(name);    if (value == null || value == "")        return ans;    return JSON.parse(value);}function SortUniqArray(array) {    array.sort(function(a, b) {        return ("" + a.link).localeCompare(b.link);    });    for (let i=0; i<array.length-1; i++)        if (array[i].link == array[i+1].link) {            array.splice(i+1,1);            i--;        }    array.sort(function(a, b) {        t = parseInt(a.date.split(" ")[1]);        s = parseInt(b.date.split(" ")[1]);        return s-t;    });    return array;}async function SortLatest() {    btn1_xpath1="/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[5]/button";    btn1_xpath2="/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[4]/button";    btn2_xpath1="/html/body/div[1]/div[2]/div/div[4]/div[1]/ul/li[3]/button";        btn1_el = GetElementByXpath(btn1_xpath1);    if (btn1_el == null)        btn1_el = GetElementByXpath(btn1_xpath2);    btn1_el.click();    await new Promise(r => setTimeout(r, 1000));        btn2_el = GetElementByXpath(btn2_xpath1);    btn2_el.click();    await new Promise(r => setTimeout(r, 1000));}async function ScrollDown() {    for (let i=0; i<10; i++) {        window.scrollTo(0, document.body.scrollHeight);        await new Promise(r => setTimeout(r, 3000));    }}Processing()';

async function ExtractMeduimWriteups(last_day, end_day=31){ 
    daily_tags = [
        "https://medium.com/tag/bug-bounty/archive/",
        "https://medium.com/tag/xss-attack/archive/",
        "https://medium.com/tag/hacking/archive/"
    ];
    monthly_tags = [
        "https://medium.com/tag/bug-bounty-writeup/archive/",
        "https://medium.com/tag/bugcrowd/archive/",
        "https://medium.com/tag/hackerone/archive/"
    ];

    localStorage.setItem("clp_wrts","");
    localStorage.setItem("emp_wrts","");
    ReleaseIt("tag");

    for (let i = 0; i < daily_tags.length; i++) {
        tag_name = daily_tags[i].split("/")[4];
        console.log("#### Processing Writeups with tag: " + tag_name);
        
        await WaitForPreviuosProcessing("tag");
        
        url = daily_tags[i] + last_day;
        await DailyTagProcessing(url,end_day);
    };

    for (let i = 0; i < monthly_tags.length; i++) {
        tag_name = monthly_tags[i].split("/")[4];
        console.log("#### Processing Writeups with tag: " + tag_name);

        await WaitForPreviuosProcessing("tag");
        
        url = monthly_tags[i] + last_day;
        await MonthlyTagProcessing(url);
    };

    await WaitForPreviuosProcessing("tag");
    PrintResults();
}


async function DailyTagProcessing(url,end_day=31) {
    console.log("DailyTagProcessing is started");
    win = null;
    days_str = ['00','01','02','03','04','05','06','07','08','09',
                '10','11','12','13','14','15','16','17','18','19',
                '20','21','22','23','24','25','26','27','28','29',
                '30','31'];
    day = parseInt(url.substring(url.length-2));
    ReleaseIt("day");

    for (let i = day; i <= end_day; i++) {
    console.log("Process day: " + days_str[i]);
    await WaitForPreviuosProcessing("day");

        next_url = url.replace(days_str[day],days_str[i]);
        win = window.open(next_url);
        await new Promise(r => setTimeout(r, 5000));
        if (win.location != next_url) {
            ReleaseIt("day");
            win.close(``, `_parent`, ``);
            continue;
        }

        var element = win.document.createElement("script");
        element.type = "text/javascript";
        element.innerHTML = processingJS;
        win.document.body.appendChild(element);
    }

    ReleaseIt("tag");
}


async function MonthlyTagProcessing(url) {
    console.log("MonthlyTagProcessing is started");
    var win = window.open(url);
    await new Promise(r => setTimeout(r, 5000));

    var element = win.document.createElement('script');
    element.type='text/javascript';
    element.innerHTML = processingJS;
    win.document.body.appendChild(element);
}


async function WaitForPreviuosProcessing(tagORday){
    lock_name = WhatsLockName(tagORday);

    while (true) {
        if (localStorage.getItem(lock_name) == "RELEAS") {
            localStorage.setItem(lock_name, "LOCK");
            break;
        }
        await new Promise(r => setTimeout(r, 10000));
    }
}


function DetectDailyOrMonthly() {
    link = window.location.href;
    if (link.split("/")[link.split("/").length-3].startsWith("202"))
        return "daily";
    else
        return "monthly";
}


function PrintResults() {
    clp_wrts = GetLocalStroageItem("clp_wrts");
    emp_wrts = GetLocalStroageItem("emp_wrts");


    window.document.write("<!DOCTYPE html> <html> <head>");
    window.document.write("<style> table {font-family: arial, sans-serif; border-collapse: collapse;}  td, th {border: 1px solid #dddddd; text-align: left; padding: 8px;}  tr:nth-child(even) {background-color: #dddddd;} </style>");
    window.document.write("</head> <body>");
    window.document.write("<script>function OpenLinks() {");
    clp_wrts.forEach(function(wrt) {window.document.write("window.open(\"" + wrt.link + "\", \"_blank\");")});
    window.document.write("}</script>");
    window.document.write("<center><h1> Write-up with more than 50 claps</h1><button onclick=OpenLinks()>Open Links</button>");
    window.document.write("<center><h1> Write-up with less than 50 claps</h1><table><tr><th style=\\\"text-align:center\\\">Date</th><th style=\\\"text-align:center\\\">Name</th></tr>");
    emp_wrts.forEach(function(wrt) {window.document.write("<tr>" + "<td>" + wrt.date + "</td><td><a href=" + wrt.link + ">" + wrt.name + "</a></td>" + "</tr>");});
    window.document.write("</table><br><br><br><h3>Author: NafisiAslH </h3> <a href=https://twitter.com/MeAsHacker_HNA>Twitter</a> <a href=https://github.com/NafisiAslH/KnowledgeSharing>Github</a></center>");
}


function GetLocalStroageItem(name) {
    ans = [];
    value = localStorage.getItem(name);
    if (value == null || value == "")
        return ans;

    return JSON.parse(value);
}


function LockIt(tagORday) {
    lock_name = WhatsLockName(tagORday);
    localStorage.setItem(lock_name, "LOCK");
}


function ReleaseIt(tagORday) {
    lock_name = WhatsLockName(tagORday);
    localStorage.setItem(lock_name, "RELEAS");
}


function WhatsLockName(tagORday) {
    if (tagORday == "tag")
        return "TagLock";
    else if (tagORday == "day")
        return "DayLock";
    return null;
}


await ExtractMeduimWriteups("2022/09/25",26)
