<script>
import Lenguages from '@/assets/config/lenguages';

export default {
  data() {
    return {
      Lenguages: Lenguages
    }
  },
}
</script>

<template>
  <nav class="navbar fixed-top navbar-expand-lg bg-dark">
    <div class="justify-content-start d-flex">
      <RouterLink to="/" class="col navbar-brand mb-0 h1 pl-3 text-light">
        <img src="@/assets/images/brand.png" height="30" class="mx-3" alt="The Order">
      </RouterLink>
    </div>
    <div class="col justify-content-between px-5" id="navbarNav">
      <ul class="justify-content-end navbar-nav d-flex flex-row">
        <li class="nav-item">
          <div class="dropdown">
            <RouterLink to="/about" class="fa-solid fa-circle-info text-light text-decoration-none"
              :title="Lenguages[Lenguages.selected].about.title" style="margin-right: 24px; margin-top: 12px;">
            </RouterLink>
          </div>
        </li>
      </ul>
    </div>
  </nav>
</template>

<style>

</style>
