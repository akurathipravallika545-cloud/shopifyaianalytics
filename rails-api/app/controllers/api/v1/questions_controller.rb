class Api::V1::QuestionsController < ApplicationController
  def create
    render json: { answer: "Mock response from Python AI service", confidence: "medium" }
  end
end
