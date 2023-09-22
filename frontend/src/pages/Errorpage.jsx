import React from 'react'
import { Link } from 'react-router-dom'

function Errorpage() {
  return (
    <div class="bg-gray-100">
    <div class="min-h-screen flex flex-col items-center justify-center">
        <div class="flex flex-row items-center space-x-4">
            <h1 class="text-4xl w-20 border-r-2 border-black font-bold text-gray-800">404</h1>
            <p class="text-2xl items-center flex text-black-600">Page not found</p>
        </div>
        <Link to={""} class="flex items-center m-4 p-2 bg-blue-400 text-lg text-white justify-center rounded-full px-4 transition-all duration-300 ease-in-out hover:bg-blue-500 hover:text-gray-100 transform active:bg-blue-600 active:text-gray-100">
            Go back to home
        </Link>
    </div>
</div>

  )
}

export default Errorpage