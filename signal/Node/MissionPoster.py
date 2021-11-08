from tqdm import tqdm

from Robot import Session, Mission, Status
from Robot.Actions.parameters import move_to_position
from Utils.Vector import angle


# 多計算一個角度(API要求)
def _xyoSetting(points):
    x, y = points
    x_next = x.copy()
    y_next = y.copy()
    x_next.append(x_next.pop(0))
    y_next.append(y_next.pop(0))
    o = list(map(angle, x, y, x_next, y_next))
    o.insert(0, o[0])
    o[-1] = 0
    x.append(x[0])
    y.append(y[0])
    return x, y, o


# 建立任務
def post(points: tuple):
    x, y, o = _xyoSetting(points)
    name = input('new mission name: ')

    # Get Session ID
    session_id = Status.GET().session_id()

    if session_id is None:
        sessions = Session.GET().array()
        dict_sessions = {s.name(): s.guid() for s in sessions}
        for s in sessions:
            print(s.name())

        while session_id is None:
            try:
                session_id = dict_sessions[input('session name: ')]
            except KeyError:
                print('No Such Session!')

    # 建立body，必要參數有: 1. mission group id 2. 任務名字
    body = Mission.PostMissions('mirconst-guid-0000-0001-missiongroup', name) \
        .session_id(session_id) # 非必要參數: session id
    # 將body放入並 mission post 方法
    newMission = Mission.POST(body)

    # 將點一個個丟到上面建立的任務
    for X, Y, orientation in tqdm(list(zip(x, y, o))):
        body = Mission.PostMission_actions('move_to_position',
                                           move_to_position(X, Y, orientation)) \
            .mission_id(newMission.guid())
        Mission.POST_missionID_actions(newMission.guid(), body)
    return newMission.guid()


if __name__ == '__main__':
    x = [10.42, 12.7, 12.42, 10.70, 10.42, 10.42]
    y = [15.01, 14.98, 13.98, 14.19, 15.01, 15.01]
    post((x, y))
