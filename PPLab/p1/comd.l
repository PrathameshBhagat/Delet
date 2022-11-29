<?php 
$s =file_get_contents('php://input');
$R="";$p="";//resultant and processing string
$l=$_GET["lang"];
 $star=0;$back=0;$double=0;$single=0;
 $index=0;$rindex=0;//current index and resumed index
function r($h,$e)//replaces keywords
{
    global $p;$p= str_replace($h,$e,$p);
}
function replace($m){
    global $p;$p=$m;//reset p to operate it 
// Remove the ++ and == 
if(!($_GET["comp"]=="javac")) 
{r("+","w3plussign");
r("=","w3equalsign");}
r("script"," ");r("php"," ");
    //OOP common keywords 
r("कक्षा","class",$p);r("वर्ग","class",$p);
r("नई","new");
r("सार्वजनीक","public",$p);r("सार्वजनिक","public",$p);
r("प्रिंट","print",$p);
r("वापस","return",$p);
//pure java keywords
r("स्थिर","static",$p);       
r("रिक्त","void",$p);
r("जरूरी","main",$p);  
r("तंत्र","System",$p);       
r("बाहर","out",$p);
r("आम","default",$p);
r("अंतिम","final",$p);
///////////////////////r("","println");


// Data Types d for double is at last  
r("अंक","int",$p);
r("बाइट","byte",$p);
r("छोटा","short",$p);
r("लंबा","long",$p);
r("फ्लोट","float",$p);
r("बड़ा","double",$p);
r("वर्ण","char",$p);
r("डोर","String",$p);
r("बूलियन","bollean",$p);
// Data Types 

/*
r("","");
r("","");*/
//Control Statments
//r("","");
r("अगर","if",$p);      
r("या","else",$p);
r("बदलो","switch",$p);r("बदले","switch",$p);      
r("यदि","case",$p);
r("केलिए","for",$p);    
r("जब-तक","while",$p);r("जबतक","while",$p);r("जब","while",$p);
r("करो","do",$p);
r("जारी","continue",$p);
r("भंग","break",$p);
r("आम","default",$p);


//single words and booleans
r("ल","l",$p);
r("ब","d",$p);
r("फ","f",$p);
r("सच","true",$p);
    return $p;
}
function pair($symbol,$end){
    global $R;global $s;global $index;global $rindex;
    $R=$R.replace(substr($s,$index,strpos($s,$symbol,$index)-$index));
    $index=strpos($s,$symbol,$index);
    $rindex=$index;
    //if closed the go to next/that index add remaining string without replace        
    if(strpos($s,$end,$index+1)){
        //echo "\n if index before:\t".$index."\trindex:\t".$rindex."\tpos".strpos($s,$end,$index+1);
        $index=strpos($s,$end,$index+1)+1;$R=$R.substr($s,$rindex,$index-$rindex);
    }
    else{
        $nouse=strpos($s,$symbol,$rindex);
        echo "Unclosed ".$symbol." found at : ". $s[$nouse-5].$s[$nouse-4].$s[$nouse-3].$s[$nouse-2].$s[$nouse-1].$symbol.$s[$nouse+2].$s[$nouse+3].$s[$nouse+4]." \t";exit();}
}          

if($l=="java"){
    for (;;)
    {      
    $star=strpos($s,"/*",$index);if(strpos($s,"/*",$index)==false)$star=strlen($s)+3;
    $back=strpos($s,"//",$index);if(strpos($s,"//",$index)==false)$back=strlen($s)+3;
    $double=strpos($s,"\"",$index);if(strpos($s,"\"",$index)==false)$double=strlen($s)+3;
    $single=strpos($s,"'",$index);if(strpos($s,"'",$index)==false)$single=strlen($s)+3;
    $not=strlen($s)+3;
        //do not run if none exist
     if(!(($star==$not)&&($back==$not)&&($double==$not)&&($single==$not)))
       {
        if($star==min($star,$back,$double,$single))    
            pair("/*","*/");
        // //comes first :
        else if($back==min($star,$back,$double,$single))
            { pair("//","\n");}
        // " comes first :
        else if($double==min($star,$back,$double,$single))
            {pair("\"","\"");}
        // ' comes first :break;
        else if($single==min($star,$back,$double,$single))
            {pair("'","'");}
        else ;
    }
    else {$R=$R.replace(substr($s,$index));break;}
}

}  /**/
if($l=="php"){
r("कक्षा","class");r("समूह","class");       
r("सार्वजनीक","public");r("सार्वजनिक","public");

//r("","");
r("अगर","if");       
r("वरना","else");
r("बदलो","switch");r("बदल","switch");       
r("हैतो","case");r("हैतो","case");
r("केलिए","for");r("के लिए","for");     
r("जबतक ","while");r("जबतक ","while");
r("करो","do"); 
    
}
//echo "<br>R:".$R."<br>index: ".$index."<br>s:".$s;
echo $R;
?>
