<template>
  <div class="outerBkgd">

    <!-- BACK TO MAIN PAGE TAB -->
    <div class="outerTabRight">
      <div class="rec"></div>
      <div class="tri"></div>
      <div class="txt" @click="close">
        <span>지도로 돌아가기</span>
        <div class="icon">
          <i class="material-icons-round">map</i>
        </div>
      </div>
    </div>

    <!-- ABOUT US TAB -->
    <div class="outerTab">
      <div class="rec"></div>
      <div class="tri"></div>
      <div class="txt">
        <span>About Us</span>
      </div>
    </div>


    <div class="outer">
      <!-- PAGE CONTENT -->
      <div class="inner">
        <Features v-show="mode==='features'" />
        <TechStack v-show="mode==='techStack'" />
        <Members v-show="mode==='members'" />
      </div>

      <!-- BLURRED BOUNDARIES -->
      <div class="blur top"></div>
      <div class="blur bottom"></div>
      
      <!-- POST-ITS -->
      <nav>
        <ul>
          <li 
            :class="{'current': mode==='features'}"
            @click="mode = 'features'"
          >주요 기능</li>
          <li 
            :class="{'current': mode==='techStack'}"
            @click="mode = 'techStack'"
          >기술 스택</li>
          <li 
            :class="{'current': mode==='members'}"
            @click="mode = 'members'"
          >팀원 소개</li>
        </ul>
      </nav>

    </div>
  </div>
</template>


<script>
import { mapMutations } from 'vuex'
import Intro from '~/components/AboutUs/Intro'
import Features from '~/components/AboutUs/Features'
import TechStack from '~/components/AboutUs/TechStack'
import Members from '~/components/AboutUs/Members'

export default {
  components: {
    Intro,
    Features,
    TechStack,
    Members
  },
  data: () => ({
    mode: 'features'
  }),
  methods: {
    ...mapMutations('about', [
      'setShowAboutUs',
    ]),
    close() {
      this.setShowAboutUs(false)
    }
  },
  mounted() {
    $(document).ready(function() {
      
    })
  },
}
</script>

<style lang="scss" scoped>
$folder-yellow: #F4B304;
$folder-yellow-dk: rgb(213, 156, 0);

@mixin viewportMax($screen) {
  @media (max-width: $screen + 'px') {
    @content;
  }
}
@mixin viewportMin($screen) {
  @media (min-width: $screen + 'px') {
    @content;
  }
}


.outerBkgd {
  width: 100%;
  height: 100vh;
  position: absolute;
  top: 0; left: 0;
  z-index: 20;
  background: #DDD;
  font-family: 'Poor Story', cursive;
}

.outerTabRight {
  $outerTabRightWidth: 170px;
  width: 300px;
  height: 70px;
  position: absolute;
  top: 10px;
  right: 10px;
  & > .rec {
    width: $outerTabRightWidth;
    height: 100%;
    background: $folder-yellow-dk;
    float: right;
    border-radius: 0 10px 0 0;
  }
  & > .tri {
    width: 0; height: 0;
    border-bottom: 70px solid $folder-yellow-dk;
    border-left: 70px solid transparent;
    position: absolute;
    right: $outerTabRightWidth;
  }
  & > .txt {
    width: $outerTabRightWidth;
    height: 60px;
    position: absolute;
    top: 0; right: 0;
    color: #333333;
    user-select: none;
    cursor: pointer;
    &:hover i {
      animation: stretch 0.8s ease-in-out infinite alternate;
    }
    & > span {
      position: absolute;
      top: 50%;
      right: 60px;
      transform: translateY(-50%);
      text-transform: uppercase;
      font-size: 18px;
      font-weight: bold;
      white-space: nowrap;
    }
    & > .icon {
      width: 60px; height: 60px;
      position: absolute;
      right: 0px;
      & > i {
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        transform-origin: left;
        font-size: 2.5em;
      }
    }
  }
}
@keyframes stretch {
  0% {transform: scaleX(1) translate(-50%, -50%);}
  100% {transform: scaleX(1.15) translate(-50%, -50%);}
}

.outerTab {
  $outerTabWidth: 240px;
  $outerTabWidthSm: 180px;
  width: 300px;
  height: 60px;
  position: absolute;
  top: 10px;
  left: 10px;
  & > .rec {
    width: $outerTabWidth;
    @include viewportMax(600) {
      width: $outerTabWidthSm;
    };
    height: 100%;
    background: $folder-yellow;
    border-radius: 10px 0 0 0;
  }
  & > .tri {
    width: 0; height: 0;
    border-bottom: 60px solid $folder-yellow;
    border-right: 60px solid transparent;
    position: absolute;
    top: 0;
    left: $outerTabWidth;
    @include viewportMax(600) {
      left: $outerTabWidthSm;
    };
  }
  & > .txt {
    width: $outerTabWidth;
    @include viewportMax(600) {
      width: $outerTabWidthSm;
    };
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    user-select: none;
    color: #333333;
    & > span {
      position: absolute;
      top: 50%; left: 30px;
      transform: translateY(-50%);
      text-transform: uppercase;
      font-family: 'Noto Sans KR', sans-serif;
      font-size: 30px;
      font-weight: 900;
      white-space: nowrap;
    }
  }
}

.outer {
  position: absolute;
  top: 70px; left: 10px;
  bottom: 10px; right: 10px;
  background: $folder-yellow;
  border-radius: 0 10px 10px 10px;
  padding: 15px;
  
}

.inner {
  width: calc(100% - 30px);
  height: calc(100% - 75px);
  background: #EEE;
  border-radius: 3px;
  overflow-y: auto;
  position: absolute;
  left: 15px;
  bottom: 20px;
  padding: 30px 40px 20px;
  @include viewportMax(600) {
    padding: 30px 10px 20px;
  }
  &::-webkit-scrollbar {
    display: initial;
    width: 7px;
    box-shadow: inset 0 0 1px rgba(0, 0, 0, 0.1);
    border-radius: 50px;
    -webkit-border-radius: 50px;
    &:hover {
      box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.15);
    }
  }
  &::-webkit-scrollbar-thumb:vertical {
    border-radius: 50px;
    -webkit-border-radius: 50px;
    background-color: rgba(0, 0, 0, 0.4);
    background-clip: padding-box;
    border: 1px solid rgba(0, 0, 0, 0);
    min-height: 10px;
    &:active {
      background-color: rgba(0, 0, 0, 0.6);
      border-radius: 50px;
      -webkit-border-radius: 50px;
    }
  }
}

.blur {
  width: calc(100% - 40px);
  height: 25px;
  position: absolute;
  left: 15px;
  &.top {
    top: 55px;
    border-radius: 3px 3px 0 0;
    background: linear-gradient(to bottom, #EEE 60%, rgba(238, 238, 238, 0));
  }
  &.bottom {
    bottom: 20px;
    border-radius: 0 0 3px 3px;
    background: linear-gradient(to top, #EEE 60%, rgba(238, 238, 238, 0));
  }
}

nav {
  width: calc(100% - 30px);
  height: 40px;
  line-height: 40px;
  padding: 0 10px;
  position: absolute;
  top: 15px; left: 15px;
  ul {
    list-style: none;
    width: 100%;
    height: 100%;
    li {
      width: 180px;
      @include viewportMax(670) {
        width: calc((100% - 10px) / 3);
      }
      height: 100%;
      float: left;
      border-radius: 10px 10px 0 0;
      text-align: center;
      font-size: 18px;
      margin-right: 5px;
      font-weight: bold;
      white-space: nowrap;
      user-select: none;
      cursor: pointer;
      &:nth-child(1) {
        background: #FEBBC4;
      }
      &:nth-child(2) {
        background: #D8E18E;
      }
      &:last-child {
        margin: 0;
        background: #B1DCEA;
      }
      &:hover {
        height: calc(100% + 2px);
        position: relative;
        top: -2px;
      }
      &.current {
        height: calc(100% + 15px);
        top: 0px;
      }
    }
  }
}


</style>