async function Processing() {
    if (DetectDailyOrMonthly() == "daily")
        await DayProcessing();
    else
        await MonthlyTagProcessing();
}

async function DayProcessing() {
    console.log("DayProcessing is started");
    clp_wrts = [];
    emp_wrts = [];
    wrt_num = 0;
    base_wrt_xpath = "/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[NUMNUM]";

    while (true) {
        wrt_num++;
        wrt_xpath = base_wrt_xpath.replace("NUMNUM",wrt_num);
        clap_num = GetClapNumber(wrt_xpath);
        if (clap_num == -1)
            break;
        if (clap_num > 50)
            clp_wrts.push(await GetWriteupInfo(wrt_xpath));
        else
            emp_wrts.push(await GetWriteupInfo(wrt_xpath));
    }

    console.log("writeups is procssed.");
    UpdateLocalStroageItem("clp_wrts", clp_wrts);
    UpdateLocalStroageItem("emp_wrts", emp_wrts);
    localStorage.setItem("DayLock", "RELEAS");
    console.log("localstorage is upated");
    window.close(``, `_parent`, ``);
}


async  function MonthlyTagProcessing() {
    console.log("MonthlyTagProcessing is started");
    clp_wrts = [];
    emp_wrts = [];
    base_wrt_xpath = "/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[NUMNUM]";   
    
    await SortLatest();
    await ScrollDown();

    wrt_num=0;
    while (true) {
        wrt_num++;
        wrt_xpath = base_wrt_xpath.replace("NUMNUM",wrt_num);
        clap_num = GetClapNumber(wrt_xpath);
        if (clap_num == -1)
            break;
        if (clap_num > 50)
            clp_wrts.push(await GetWriteupInfo(wrt_xpath));
        else
            emp_wrts.push(await GetWriteupInfo(wrt_xpath));
    }

    console.log("writeups is procssed.");
    UpdateLocalStroageItem("clp_wrts", clp_wrts);
    UpdateLocalStroageItem("emp_wrts", emp_wrts);
    localStorage.setItem("TagLock", "RELEAS");
    console.log("localstorage is upated");
    window.close(``, `_parent`, ``);
}


function DetectDailyOrMonthly() {
    link = window.location.href;
    if (link.split("/")[link.split("/").length-3].startsWith("202"))
        return "daily";
    else
        return "monthly";
}


function GetClapNumber(wrt_xpath) {
    wrt = GetElementByXpath(wrt_xpath);
    if (wrt == null)
        return -1;
    
    btn_xpath = wrt_xpath + "/div/div/div[4]/div[1]/div/span/button";
    btn = GetElementByXpath(btn_xpath);
    
    if (btn == null)
        return 0;
    return btn.textContent;
}


async function GetWriteupInfo(wrt_xpath) {
    name_xpaths = [
        "/div/div/div[2]/a/div/section/div[2]/div/h3",
        "/div/div/div[2]/div/section/div/div/a/h3",
        "/div/div/div[2]/a/div/section/div[2]/div/p[1]/strong",
        "/div/div/div[2]/div/section/div/div/h3/a",
        "/div/div/div[2]/a/div/section/div[2]/div/p[1]",
        "/div/div/div[2]/div/section/div/div/a/p[1]",
        "/div/div/div[2]/a/div/section/div[2]/div/h4",
        "/div/div/div[2]/div/section/div/div/p"
    ];
    a_xpath = wrt_xpath + "/div/div/div[2]/a";
    date_xpath = wrt_xpath + "/div/div/div[1]/div/div/div[2]/div/a";
    
    name_el = null;
    for (let i=0; i<name_xpaths.length; i++) {
        console.log(i);
        name_el = GetElementByXpath(wrt_xpath + name_xpaths[i]);
        if (name_el != null)
            break;
    }
    
    name = name_el.textContent;
    link = GetElementByXpath(a_xpath).href.split("?")[0];
    date = GetElementByXpath(date_xpath).text;

    return {name:name, date:date, link:link};
}


function GetElementByXpath(path) {
    return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}


function UpdateLocalStroageItem(name , writeups) {
    value_from_storage = GetLocalStroageItem(name);
    writeups.forEach(function(writeup) {value_from_storage.push(writeup)});

    output = SortUniqArray(value_from_storage);
    localStorage.setItem(name, JSON.stringify(output));
}


function GetLocalStroageItem(name) {
    ans = [];
    value = localStorage.getItem(name);
    if (value == null || value == "")
        return ans;

    return JSON.parse(value);
}


function SortUniqArray(array) {
    array.sort(function(a, b) {
        return ("" + a.link).localeCompare(b.link);
    });

    for (let i=0; i<array.length-1; i++)
        if (array[i].link == array[i+1].link) {
            array.splice(i+1,1);
            i--;
        }

    array.sort(function(a, b) {
        t = parseInt(a.date.split(" ")[1]);
        s = parseInt(b.date.split(" ")[1]);
        return s-t;
    });

    return array;
}

async function SortLatest() {
    btn1_xpath1="/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[5]/button";
    btn1_xpath2="/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[4]/button";
    btn2_xpath1="/html/body/div[1]/div[2]/div/div[4]/div[1]/ul/li[3]/button";
    
    btn1_el = GetElementByXpath(btn1_xpath1);
    if (btn1_el == null)
        btn1_el = GetElementByXpath(btn1_xpath2);
    btn1_el.click();
    await new Promise(r => setTimeout(r, 1000));
    
    btn2_el = GetElementByXpath(btn2_xpath1);
    btn2_el.click();
    await new Promise(r => setTimeout(r, 1000));

}


async function ScrollDown() {
    for (let i=0; i<10; i++) {
        window.scrollTo(0, document.body.scrollHeight);
        await new Promise(r => setTimeout(r, 3000));
    }
}


Processing()
