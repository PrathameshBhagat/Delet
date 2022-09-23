<html>
<head>

<link rel="stylesheet" href="m.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script >
function check(){
if(document.getElementsByName("name").length>0&&document.getElementsByName("pno").length>0)
document.getElementByName("msform").submit();

}
</script>
</head>
<body>
<section class="multi_step_form">  
  <form name="msform" id="msform" method="post" action="send.php"> 
    <!-- Tittle -->
    <div class="tittle">
      <h2>Prathamesh's Number Storage</h2>
      
    </div>
    <!-- progressbar -->
    <ul id="progressbar">
      <li class="active">Name </li>
      <li class="active">Add Phone Number</li>
      <li >Information</li>
      <li >Submit</li>
      <li >Add Phone Numbesccr</li>
      <li>Upload Documents</li> 
      <li>Security Questions</li>
    </ul>
    <!-- fieldsets -->
        <fieldset>
      <h3>Name </h3>
      <div class="form-row"> 
        <div class="form-group col-md-6">  
          <input type="text" name="name" class="form-control" placeholder="Prathamesh"> 
        </div>  
        <div class="form-group col-md-6"> 
          <input type="text" name="sname" class="form-control" placeholder="Bhagat">
        </div>  
        <div class="form-group col-md-6"> 
              <input type="text" name="mname" class="form-control" placeholder="Arunika"> 
          </div>
        <div class="form-group col-md-6"> 
          <input type="text" name="fname" class="form-control" placeholder="Vivek">
        </div> 
      </div> 

      <button type="button" class="action-button previous_button">Back</button>
      <button type="button" class="next action-button">Continue</button>  
    </fieldset>
     <fieldset>
      <h3>Setup your phone</h3>
     <div class="form-row"> 
        <div class="form-group col-md-6">  
          <input type="number" name="pno" class="form-control" placeholder="PersonalNo"> 
        </div>  
        <div class="form-group col-md-6"> 
          <input type="number" name="fno" class="form-control" placeholder="Father'sNo">
        </div>  
        <div class="form-group col-md-6"> 
              <input type="number" name="mno" class="form-control" placeholder="Mother'sNo"> 
          </div> 
     <div class="form-group col-md-6"> 
              <input type="number" name="eno" class="form-control" placeholder="Extras No"> 
          </div> 
      </div> 
    
      <button type="button" class="action-button previous_button">Back</button>
      <button type="button" class="next action-button">Continue</button>  
    </fieldset>
    
<fieldset>
      <h3>Date Of Birth</h3>
     <div class="form-row"> 
        <div class="form-group col-md-6">  
              <div class="code_group"> 
        <input type="number" name="d1" class="form-control" placeholder="0">
        <input type="number" name="d2" class="form-control" placeholder="0">-
        <input type="number" name="m1" class="form-control" placeholder="0">
        <input type="number" name="m2" class="form-control" placeholder="0">-
        <input type="number" name="y1" class="form-control" placeholder="0">
        <input type="number" name="y2" class="form-control" placeholder="0">
        <input type="number" name="y3" class="form-control" placeholder="0">
        <input type="number" name="y4" class="form-control" placeholder="0">
      </div> 
    

      <button type="button" class="action-button previous_button">Back</button>
      <button type="button" class="next action-button">Continue</button>  
    </fieldset>

 
  <fieldset>
      <h3>Information</h3>
     <div class="form-row"> 
        <div class="form-group col-md-6">  
          <input type="text" name="Place" class="form-control" placeholder="Common Places"> 
        </div>  
        <div class="form-group col-md-6"> 
          <input type="text" name="Instituiton" class="form-control" placeholder="Past-Instituitons">               
        </div>  
        <div class="form-group col-md-6"> 
              <input type="text" name="cInstitution" class="form-control" placeholder="Current Institution"> 
          </div>
      <div class="form-group col-md-6"> 
              <input type="text" name="fInstitution" class="form-control" placeholder="Future Institution"> 
          </div>
      </div> 
      <button type="button" class="action-button previous_button">Back</button>
      <button type="button" class="next action-button">Continue</button>  
    </fieldset>
 
<fieldset>
      <h3>Submit</h3>
  	<div class="form-group col-md-6"> 
              <input type="number" name="indi" class="form-control" placeholder="Future Institution"> 
          </div>
     <button type="button" class="action-button previous_button">Back</button>
      <button type="button" class="next action-button">Relative</button>  

    <input type="submit"   onclick="check('a')" value="Indivnameual" >      

    </fieldset>
  </form>  
</section> 
</body>
</html>  