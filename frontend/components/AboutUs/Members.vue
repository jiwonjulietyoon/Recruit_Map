<template>
  <section>
    <div class="Title">팀원 소개</div>
    
    <div class="Content">
      <div class="cardContainer" v-for="m in members" :key="m.id">
        <div class="card" :style="{ backgroundImage: 'url(' + m.bg + ')' }">
          <div class="profImg">
            <img :src="m.profImg" :alt="`${m.name} 프로필 이미지`">
          </div>
          <div class="profInfo">
            <p class="role">{{m.role}}</p>
            <div class="nameContainer">
              <div class="name">{{m.name}}</div>
              <div class="github">
                <a :href="m.gitHub" target="_blank">
                  <img :src="require('~/static/github-logo.svg')" alt="GitHub">
                </a>
              </div>
            </div>
          </div>
          <div class="tape top" :style="{ backgroundImage: 'url(' + m.tape + ')' }"></div>
          <div class="tape bottom" :style="{ backgroundImage: 'url(' + m.tape + ')' }"></div>
        </div>
      </div>
    </div>
    
  </section>
</template>

<script>
export default {
  name: "Members",
  data: () => ({
    members: [
      {
        id: 1,
        name: '김도우',
        profImg: "https://avatars2.githubusercontent.com/u/41623836?s=460&v=4",
        gitHub: "https://github.com/dowookims",
        role: "팀장 | 프론트엔드",
        bg: "https://i.imgur.com/GEVWD4r.jpg",
        tape: "https://i.imgur.com/zmNI7JL.jpg"
      },
      {
        id: 2,
        name: '서지욱',
        profImg: "https://avatars1.githubusercontent.com/u/30630564?s=460&v=4",
        gitHub: "https://github.com/jiwookseo",
        role: "백엔드",
        bg: "https://i.imgur.com/nrsbrDz.jpg",
        tape: "https://i.imgur.com/GPUdTnX.jpg"
      },
      {
        id: 3,
        name: '윤지원',
        profImg: "https://avatars1.githubusercontent.com/u/45954965?s=460&v=4",
        gitHub: "https://github.com/jiwonjulietyoon",
        role: "프론트엔드",
        bg: "https://i.imgur.com/xRfemge.jpg",
        tape: "https://i.imgur.com/ahQlxNo.jpg"
      }
    ]
  })
}
</script>

<style lang="scss" scoped>
@import '~/assets/aboutus.scss';

.Content {
  width: 100%;
  // border: 1px solid red;
}

.cardContainer {
  width: calc(100% / 3);
  float: left;
  @include viewportMax(950) {
    width: calc(100% / 2);
  }
  @include viewportMax(650) {
    width: 100%;
  }
  height: auto;
  margin-bottom: 40px;
  // border: 1px solid cyan;
}

.card {
  width: 250px;
  height: 350px;
  border: 1px solid transparent; // needed for some reason
  margin: 0 auto;
  border-radius: 5px;
  position: relative;
}

.profImg {
  width: 200px;
  height: 200px;
  margin: 25px auto 20px;
  background: white;
  img {
    width: 100%; height: 100%;
    object-fit: cover;
    border-radius: 2px;
  }
}

.profInfo {
  width: 200px;
  height: 85px;
  margin: 0 auto;
  padding: 5px 10px;
  user-select: none;
  .role {
    padding-left: 3px;
  }
  .nameContainer {
    .name {
      float: left;
      font-size: 40px;
      font-weight: bold;
    }
    .github {
      float: right;
      width: 50px;
      height: 50px;
      padding-top: 5px;
      a, img {
        width: 90%; height: 90%;
      }
      img:hover {
        animation: bobRight 0.7s ease-in-out infinite alternate;
      }
    }
  }
}

@keyframes bobRight {
  0% {transform: translate(0);}
  100% {transform: translate(5px);}
}


.tape {
  width: 40px;
  height: 80px;
  position: absolute;
  transform: rotate(60deg) skew(5deg);
  opacity: 0.6;
  border-radius: 2px;
  &.top {
    top: -20px; left: 0;
    background: no-repeat center;
  }
  &.bottom {
    bottom: -20px; right: 0;
    background: no-repeat left;
  }
}

</style>