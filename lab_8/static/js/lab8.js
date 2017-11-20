 // FB initiation function
 window.fbAsyncInit = () => {
  FB.init({
    appId      : '168498080410913',
    cookie     : true,
    xfbml      : true,
    version    : 'v2.11'
  });

  // implementasilah sebuah fungsi yang melakukan cek status login (getLoginStatus)
  // dan jalankanlah fungsi render di bawah, dengan parameter true jika
  // status login terkoneksi (connected)

  // Hal ini dilakukan agar ketika web dibuka dan ternyata sudah login, maka secara
  // otomatis akan ditampilkan view sudah login
  FB.getLoginStatus(function(response) {
    if (response.status === 'connected') {
      // the user is logged in and has authenticated your
      // app, and response.authResponse supplies
      // the user's ID, a valid access token, a signed
      // request, and the time the access token 
      // and signed request each expire
      console.log(response);
      var uid = response.authResponse.userID;
      var accessToken = response.authResponse.accessToken;
      render(true);
    } else if (response.status === 'not_authorized') {
      // the user is logged in to Facebook, 
      // but has not authenticated your app
      console.log(response);
      render(false);
    } else {
      // the user isn't logged in to Facebook.
      console.log(response);
      render(false);
    }
  }
);
};

// Call init facebook. default dari facebook
(function(d, s, id){
   var js, fjs = d.getElementsByTagName(s)[0];
   if (d.getElementById(id)) {return;}
   js = d.createElement(s); js.id = id;
   js.src = "https://connect.facebook.net/en_US/sdk.js";
   fjs.parentNode.insertBefore(js, fjs);
 }(document, 'script', 'facebook-jssdk'));

// Fungsi Render, menerima parameter loginFlag yang menentukan apakah harus
// merender atau membuat tampilan html untuk yang sudah login atau belum
// Ubah metode ini seperlunya jika kalian perlu mengganti tampilan dengan memberi
// Class-Class Bootstrap atau CSS yang anda implementasi sendiri
const render = loginFlag => {
  if (loginFlag) {
    // Jika yang akan dirender adalah tampilan sudah login

    // Memanggil method getUserData (lihat ke bawah) yang Anda implementasi dengan fungsi callback
    // yang menerima object user sebagai parameter.
    // Object user ini merupakan object hasil response dari pemanggilan API Facebook.
    getUserData(user => {
      // Render tampilan profil, form input post, tombol post status, dan tombol logout
      $('#lab8').html(
        '<div class="user-profile">' +
        '<div class="cover"><img src="'+ user.cover.source +'" width="851px"/></div>' +
        '<div class="picture"><img src="' + user.picture.data.url + '" width="168px" height="168px"/></div>' +
        '<div class="name">' + user.name + '</div>' +
        '<div id="logout-btn">' + 
          '<button class="btn btn-primary logout" onclick="facebookLogout()">Logout</button>' +
        '</div>' +
        '<div class="about">' +
          '<div>' +
            '<img src="https://png.icons8.com/user/win10/25/000000"> <b>About Me</b>' +
            '<div>' + user.about + '</div>' +
          '</div>' +
          '<div><img src="https://png.icons8.com/message-filled/win10/25/000000"> <b>E-mail</b>' +
            '<div>' + user.email + '</div>' +
          '</div>' +
          '<div><img src="https://png.icons8.com/gender/win10/25/000000"> <b>Gender</b><div>' + user.gender + '</div>' +
          '</div>' +
        '</div>' +
        '<div class="well">' +
          '<form class="form-horizontal" role="form">' +
            '<div class="form-group" style="padding:14px;">' +
            '<textarea id="postInput" class="form-control" placeholder="What\'s on your mind?"></textarea>' +
            '</div>' +
            '<button class="btn btn-primary pull-right" type="button" onclick="postStatus()">Post</button>' +
          '</form>' +
        '</div>' +
        '<div class="status"></div>' +
      '</div>'
      );

      // Setelah merender tampilan di atas, dapatkan data home feed dari akun yang login
      // dengan memanggil method getUserFeed yang kalian implementasi sendiri.
      // Method itu harus menerima parameter berupa fungsi callback, dimana fungsi callback
      // ini akan menerima parameter object feed yang merupakan response dari pemanggilan API Facebook
      getUserFeed(feed => {
        feed.data.map(value => {
          // Render feed, kustomisasi sesuai kebutuhan.
          if (value.message) {
            $(".status").append(
                '<div class="list-status">' +
                  '<div class="mini-photo">' +
                      '<img class = "img-circle" id="status-photo" src="' + picture +'" style="width:50px;">' +
                      '<strong id="user-name">' + name + '</strong>' +
                  '</div>' +
                  '<div class="statuses">' +
                      value.message  +
                  '</div>' +
                '</div>'
            );
          }
        });
      });
    });
  } else {
    // Tampilan ketika belum login
    $('#lab8').html('<button class="login" onclick="facebookLogin()">Login</button>');
  }
};

const facebookLogin = () => {
  // TODO: Implement Method Ini
  // Pastikan method memiliki callback yang akan memanggil fungsi render tampilan sudah login
  // ketika login sukses, serta juga fungsi ini memiliki segala permission yang dibutuhkan
  // pada scope yang ada. Anda dapat memodifikasi fungsi facebookLogin di atas.
  FB.login(function (response) {
    if (response.authResponse) {
      console.log(response);
      render(true);
    } else {
      console.log(response);
      render(false);
    }
}, {scope: 'public_profile,user_posts,publish_actions,user_about_me,email'});
};

const facebookLogout = () => {
  // TODO: Implement Method Ini
  // Pastikan method memiliki callback yang akan memanggil fungsi render tampilan belum login
  // ketika logout sukses. Anda dapat memodifikasi fungsi facebookLogout di atas.
  FB.getLoginStatus(function(response) {
    if (response.status === 'connected') {
      FB.logout();
      render(false);
    }
 });

};

// TODO: Lengkapi Method Ini
// Method ini memodifikasi method getUserData di atas yang menerima fungsi callback bernama fun
// lalu merequest data user dari akun yang sedang login dengan semua fields yang dibutuhkan di 
// method render, dan memanggil fungsi callback tersebut setelah selesai melakukan request dan 
// meneruskan response yang didapat ke fungsi callback tersebut
// Apakah yang dimaksud dengan fungsi callback?
const getUserData = (fun) => {
  FB.getLoginStatus(function(response) {
    if(response.status === 'connected') {
      FB.api('/me?fields=name, about, email, gender, cover, picture', 'GET', function (response){
        picture = response.picture.data.url;
        name = response.name;
        console.log(response);
        fun(response);
      });
    }
  });
}

const getUserFeed = (fun) => {
  // TODO: Implement Method Ini
  // Pastikan method ini menerima parameter berupa fungsi callback, lalu merequest data Home Feed dari akun
  // yang sedang login dengan semua fields yang dibutuhkan di method render, dan memanggil fungsi callback
  // tersebut setelah selesai melakukan request dan meneruskan response yang didapat ke fungsi callback
  // tersebut
  FB.getLoginStatus(function(response) {
    if(response.status === 'connected') {
      FB.api("/me/feed", 'GET', function (response) {
            console.log(response);
            fun(response);
        }
      );
    }
  });
};

const postFeed = (message) => {
  // Todo: Implement method ini,
  // Pastikan method ini menerima parameter berupa string message dan melakukan Request POST ke Feed
  // Melalui API Facebook dengan message yang diterima dari parameter.
  FB.getLoginStatus(function(response) {
    if(response.status === 'connected') {
      console.log(response);
      FB.api("/me/feed", 'post', {message: message});
      render(true);
    }
  }, {scope: 'publish_actions'});
};

const postStatus = () => {
  const message = $('#postInput').val();
  $('#postInput').val("");
  postFeed(message);
};
