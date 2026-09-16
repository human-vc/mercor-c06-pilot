SIM_CONFIGS = {

    "simA_minimal": "You are the client who commissioned this work. The notes below are what you know about the job. Answer only the specific question asked, briefly and factually, using only these notes; if the notes do not cover a question, say you have no further instruction on it. Speak as the client; do not mention notes, packets, requirements documents or an experiment. Do not do any of the work.",

    "simB_helpful": "You are the client who commissioned this work. The notes below are what you know about the job. Answer the question asked using only these notes, and add anything else from the notes that a careful client would mention; if the notes do not cover a question, say you have no further instruction on it. Speak as the client; do not mention notes, packets, requirements documents or an experiment. Do not do any of the work.",

}


def simulated_reply(model, config_name, packet, agent_message):

    system = SIM_CONFIGS[config_name] + "\n\nWHAT YOU KNOW:\n" + packet

    turn, _ = model.chat(system, [model.user_content(agent_message)])

    return turn.text.strip()


def scripted_reply(packet_scripted):

    return packet_scripted
