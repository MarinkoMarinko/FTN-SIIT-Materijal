import { getAllAuthors } from "../../db/author.js"

const cardsContainer = document.getElementById("cardsContainer")
const searchName = document.getElementById("searchName")
const searchStatus = document.getElementById("searchStatus")
const searchBtn = document.querySelector(".search-advanced .btn-details")

let allAuthors = []

function getStatusClass(status) {
  switch (status) {
    case "Преминуо":
      return "text-bg-dark"
    case "Активан":
      return "text-bg-success"
    case "У пензији":
      return "text-bg-warning"
    default:
      return "text-bg-secondary"
  }
}

document.addEventListener("DOMContentLoaded", async () => {
  const result = await getAllAuthors()

  if (!result.success) {
    cardsContainer.innerHTML = `<p class="text-center text-danger fs-5">${result.error}</p>`
    return
  }

  allAuthors = result.data
  renderAuthors(allAuthors)
})

searchBtn.addEventListener("click", searchAuthors)

function searchAuthors() {
  const nameValue = searchName.value.trim().toLowerCase()
  const statusValue = searchStatus.value

  const filteredAuthors = allAuthors.filter((author) => {
    const fullName = `${author.ime} ${author.prezime}`.toLowerCase()
    const biography = (author.biografija || "").toLowerCase()

    const matchesName =
      nameValue === "" ||
      fullName.includes(nameValue) ||
      biography.includes(nameValue)

    const matchesStatus = statusValue === "" || author.status === statusValue

    return matchesName && matchesStatus
  })

  renderAuthors(filteredAuthors, nameValue)
}

function renderAuthors(authors, searchText = "") {
  cardsContainer.innerHTML = ""

  if (authors.length === 0) {
    cardsContainer.innerHTML = `
            <div class="col-12">
                <p class="text-center text-muted fs-5 mb-0">
                    Нема аутора који одговарају претрази.
                </p>
            </div>
        `
    return
  }

  authors.forEach((author) => {
    const fullName = `${author.ime} ${author.prezime}`

    const highlightedName = highlightText(fullName, searchText)

    const biographyText = author.biografija || ""
    const highlightedBiography = highlightText(biographyText, searchText)

    const highlightedStatus =
      searchStatus.value === ""
        ? author.status
        : `<mark class="search-highlight">${author.status}</mark>`

    cardsContainer.innerHTML += `
            <div class="col-md-6 col-lg-4">
                <div class="card author-card h-100 rounded-4 shadow-sm text-center p-4">
                    <img 
                        src="${author.slike?.[0] || "https://picsum.photos/300/300"}" 
                        alt="${fullName}" 
                        class="author-img rounded-circle mx-auto mb-4"
                    >

                    <div class="card-body p-0 d-flex flex-column">
                        <h2 class="h4 fw-bold mb-3" style="color:#2b1408;">
                            ${highlightedName}
                        </h2>

                        <div class="mb-3">
                            <span class="badge ${getStatusClass(author.status)} px-3 py-2">
                                ${highlightedStatus}
                            </span>
                        </div>

                        <p class="fs-5 lh-lg mb-4" style="color:#6f5a45;">
                            ${highlightedBiography}
                        </p>

                        <div class="mt-auto">
                            <a href="./single_author.html?id=${author.id}" class="btn btn-details rounded-2 px-4">
                                Детаљније
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        `
  })
}

function highlightText(text, searchText) {
  if (searchText === "") {
    return text
  }

  const lowerText = text.toLowerCase()
  const lowerSearch = searchText.toLowerCase()

  const index = lowerText.indexOf(lowerSearch)

  if (index === -1) {
    return text
  }

  return `
        ${text.slice(0, index)}
        <mark class="search-highlight">${text.slice(index, index + searchText.length)}</mark>
        ${text.slice(index + searchText.length)}
    `
}
