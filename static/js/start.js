$(document).ready(function(){

    $('.window').windows({
        snapping: true,
        snapSpeed: 500,
        snapInterval: 1100,
        onScroll: function(scrollPos){
            // scrollPos:Number
        },
        onSnapComplete: function($el){
            // after window ($el) snaps into place
        },
        onWindowEnter: function($el){
            // when new window ($el) enters viewport
        }
    });
    /*$(function() {
        $(".dial").knob({
            'width':30,
            'fgColor':"#FFC300",
            'bgColor':"#02C9C9",
            'inputColor':"#E3E3E3",
            'fontWeight':"700",
            'font':"Raleway",
            'fontSize':30,
            'thickness':1
        });
    });*/
    function change(bool, id1, id2) {
        //bg array


        if (bool)
            $('#defil1').attr('src',bgArray[id1]);
        else
            $('#defil2').attr('src',bgArray[id2]);
    }
    $(function(){
        var bgArray=new Array();
        bgArray[0]="../static/images/game_bg/1.png";
        bgArray[1]="../static/images/game_bg/2.png";
        bgArray[2]="../static/images/game_bg/3.png";
        bgArray[3]="../static/images/game_bg/4.png";

        var time = 8000;
        var timeFade = 2500;
        var id1=0;
        var id2=1;

        var bool = true;
        $('#defil2').fadeToggle(1);
        window.setInterval(function(){
            $('#defil1').attr('src',bgArray[id1]);
            $('#defil2').attr('src',bgArray[id2]);
            $('#defil1').fadeToggle(timeFade);
            $('#defil2').fadeToggle(timeFade);
            if (bool)
                if (id1+2>=4) id1=0; else id1+=2;
            else
                if (id2+2>=4) id2=1; else id2+=2;

            bool = !bool;
        },time);
    });
});