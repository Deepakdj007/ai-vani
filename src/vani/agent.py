import logging

from livekit.agents import Agent, AgentSession, JobContext, RoomInputOptions, WorkerOptions, cli
from livekit.agents import llm
from livekit.plugins import sarvam

from vani.config import DEFAULT_LANGUAGE, SARVAM_API_KEY
from vani.prompts import GREETING, echo_response

logger = logging.getLogger("vani.agent")


class EchoAgent(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=GREETING)

    async def on_user_turn_completed(
        self,
        _turn_ctx: llm.ChatContext,
        new_message: llm.ChatMessage,
    ) -> None:
        transcript: str = new_message.text_content or ""
        logger.info("User said: %s", transcript)
        self.session.say(echo_response(transcript))


async def entrypoint(ctx: JobContext) -> None:
    logger.info("Agent connecting to room: %s", ctx.room.name)

    session = AgentSession(
        stt=sarvam.STT(language=DEFAULT_LANGUAGE, api_key=SARVAM_API_KEY),
        tts=sarvam.TTS(target_language_code=DEFAULT_LANGUAGE, api_key=SARVAM_API_KEY),
    )

    await session.start(
        room=ctx.room,
        agent=EchoAgent(),
        room_input_options=RoomInputOptions(),
    )

    session.say(GREETING)


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
