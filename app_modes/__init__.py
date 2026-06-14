from app_modes import chatbot, codegen


MODE_RUNNERS = {
    "chatbot": chatbot.run,
    "codegen": codegen.run,
}


def get_mode_names():
    return sorted(MODE_RUNNERS)


def get_mode_runner(mode):
    return MODE_RUNNERS[mode]
