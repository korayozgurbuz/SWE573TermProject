/**
 * Created by mk0730 on 12/6/15.
 */
//    Demo json  loaded from dropbox
//    Data = http://codepen.io/nakome/pen/DnEvr.js
//[
//   {
//      "photo":"image url ",
//      "name":"Jhon",
//      "last":"Smith",
//      "email":"jhony@site.com",
//      "phone":"1-555-222-333",
//      "web":"http://jhonSmith.com"
//   },
//   {
//      "photo":"image url",
//      "name":"Carla",
//      "last":"Doe",
//      "email":"carladoe@site.com",
//      "phone":"1-333-111-555",
//      "web":"http://carladoe.com"
//   }
// ]


(function(){

  'use-strict';

  var elem,
      // data-fn
      dataFn = $('[data-fn="contacts"]'),
      // data-url
      thisUrl = dataFn.data('url');


  if (typeof $.table_of_contacts == 'undefined')

    $.table_of_contacts = {};

  $.table_of_contacts.get = {

    init: function() {
      if(dataFn){
        this.getJson();
      }else{
        dataFn.html('No data found.');
      }
    },

    /* = Get data
    ------------------------*/
    getJson: function(url){

      var self = this;

      // loading data before
      dataFn.html('<span class="loading_table">'+
                  'Loading Please Wait ....'+
                  '</span>');

      // No ajax cache
      $.ajaxSetup({ cache: false });

      // Get json
      $.getJSON(thisUrl,function(data){

        // load template
        var out_html = self.tpl();

        $.each(data,function(i,obj){
          // load inner template
          out_html += self.tpl_inner(obj);

        });
        // close tag
        out_html += '</tbody>';
        // render templates
        dataFn.html(out_html);
        // error
      }).error(function(j,t,e){
        // render error.
        dataFn.html('<span class="error_table">'+
                    'Error = '+e+
                    '</span>');

      });
    },

    // head table template
    tpl: function(){
      var html = '<thead>'+
          '<tr>'+
          '<th>Photo</th>'+
          '<th>Name</th>'+
          '<th>Last Name</th>'+
          '<th>Email</th>'+
          '<th>Phone</th>'+
          '<th>Web</th>'+
          '</tr>'+
          '</thead>'+
          '<tbody >';
      return html;
    },
    // inner template
    tpl_inner: function(obj){

      var  html= '<tr>'+
          '<td class="user-photo">'+
          '<img class="user-tumb" src="'+obj.photo+'"/>'+
          '</td>'+
          '<td>'+obj.name+'</td>'+
          '<td>'+obj.last+'</td>'+
          '<td>'+obj.email+'</td>'+
          '<td>'+obj.phone+'</td>'+
          '<td>'+
          '<a href="'+obj.web+'" title="'+
          obj.name + ' ' + obj.last+'">'+
          obj.web +
          '</td>'+
          '</tr>';
      return html;
    }

  };

  // on ready render data
  $(document).ready(function() {
    $.table_of_contacts.get.init();
  });
})().call(this);