import React from 'react'

function Intropage() {
  return (
    <div>
        {/* Intro Message */}
      <div class="min-h-screen flex flex-col flex-wrap items-center justify-center">
        <p class="text-3xl md:text-3xl lg:text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-green-700 via-orange-600 to-blue-600">
          One District One Product
        </p>  
        <div class='flex flex-wrap items-center justify-end'>
          <p class="text-1xl md:text-2xl lg:text-2xl font-bold"> 
            The Jammu kashmir initiative 
          </p>
        </div>
      </div>
    </div>
  )
}

export default Intropage