    
$('.larCatDiv.other').on('click',function(event){
    var obj = $(event.target);
    var tmp = $('.larCatDiv.main').html();
    
    changeMidCat(obj,$('.larCatDiv.main'))
    $('.larCatDiv.main').html(obj.html())
    obj.html(tmp);
    
    $(".larCatDiv.other").slideUp();
    
    
});

function changeMidCat(catNum1,catNum2){
    var cat1 = catNum1.children('img').attr("name")
    var cat2 = catNum2.children('img').attr("name")
    $('#'+cat2).css("display","none");
    $('#'+cat1).animate({width:'toggle'},700);
}

$('.larCatDiv.main').on('click',function(evnet){
    $(".larCatDiv.other").slideToggle();
});