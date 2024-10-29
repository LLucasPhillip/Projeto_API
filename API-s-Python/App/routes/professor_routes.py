from flask import Blueprint
from ..controllers.professor_controller import criar_professor

professor_bp = Blueprint('professor_bp', __name__)

@professor_bp.route('/', methods=['POST'])
def criar_prof():
    return criar_professor()
