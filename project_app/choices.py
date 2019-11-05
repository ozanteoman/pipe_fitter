class ServiceStatus:
    ACTIVE = 0
    INACTIVE = 1
    DELETED = 2

    STATUS = (
        (ACTIVE, "ACTIVE"),
        (INACTIVE, "INACTIVE"),
        (DELETED, "DELETED")
    )


class TopicStatus:
    WAITING_VERIFIED = 0
    WAITING_DONE = 1
    DONE = 2
    DELETED = 3
    CANCELLED = 4
    NOT_VERIFIED = 5

    STATUS = (
        (WAITING_VERIFIED, "Waiting Verified"),
        (WAITING_DONE, "Waiting Done"),
        (DONE, "Done"),
        (DELETED, "Deleted"),
        (CANCELLED, "Cancelled"),
        (NOT_VERIFIED, "Not Verified")
    )


class OrderStatus:
    CANCELLED = 0
    DONE = 1
    ACTIVE = 2

    STATUS = (
        (CANCELLED, "Cancelled"),
        (DONE, "Done"),
        (ACTIVE, "Active")
    )


class UserType:
    EMPLOYEE = 0
    NORMAL = 1

    STATUS = (
        (EMPLOYEE, "Employee"),
        (NORMAL, "Normal")
    )
